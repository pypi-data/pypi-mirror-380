import csv
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Set

from jsonargparse import CLI
from rich.console import Group
from rich.panel import Panel
from rich.style import Style
from rich.table import Table
from rich.text import Text

from wxo_agentic_evaluation.arg_configs import AnalyzeConfig
from wxo_agentic_evaluation.description_quality_checker import (
    DescriptionQualityInspector,
)
from wxo_agentic_evaluation.metrics.metrics import (
    TextMatchType,
    ToolCallAndRoutingMetrics,
)
from wxo_agentic_evaluation.type import (
    ContentType,
    ExtendedMessage,
    ToolDefinition,
)
from wxo_agentic_evaluation.utils.rich_utils import (
    IncorrectParameterUtils,
    is_ok,
    pretty_print,
    print_done,
    warn,
)
from wxo_agentic_evaluation.utils.utils import (
    add_line_seperator,
    list_run_files,
    load_run_metrics,
)


class Analyzer:
    def __init__(self):
        self.analysis_cache: Dict[str, List[Text]] = (
            {}
        )  # the failing tools cached here won't be re-analyzed.
        # tool_name -> description analysis

    @staticmethod
    def _generate_style_config():
        return Style(
            color="magenta",
            blink=True,
            bold=True,
        )

    def _split_cache(
        self, failing_tools: Set[str]
    ) -> tuple[List[str], List[Text]]:

        tools_to_analyze: List[str] = []
        cached_lines: List[Text] = []
        tools_analyzed: List[str] = []

        for tool_name in sorted(failing_tools):
            cached_analysis = self.analysis_cache.get(tool_name)
            if cached_analysis:
                cached_lines.extend(cached_analysis)
                tools_analyzed.append(tool_name)
            else:
                tools_to_analyze.append(tool_name)

        if tools_analyzed:
            pretty_print(
                content=f"ℹ️ Loading cached analysis since these failing tools: {tools_analyzed} have been analyzed previously.",
                style="bold cyan",
            )

        return (tools_to_analyze, cached_lines)

    def analyze_failing_tool_description_quality(
        self,
        inspector: DescriptionQualityInspector,
        tool_definition_path: str,
        failing_tools: Set[str],
    ) -> List[Text]:
        """
        :param tool_definition_path: Path to the tool definition file.
        :param failing_tools: Set of tool names that failed.
        :return: List of rich `Text` objects containing feedback for the customer.
        """

        pretty_print(
            content=f"⚙️ Checking tool description quality for failing tools: {sorted(failing_tools)}",
            style="bold cyan",
        )

        analysis_for_display: List[Text] = []

        # Step 1: get tools not yet analyzed and cached analysis for tools analyzed previously
        tools_to_analyze, cached_analysis = self._split_cache(failing_tools)
        if cached_analysis:
            analysis_for_display.extend(cached_analysis)

        # Step 2: analyze cache misses
        if tools_to_analyze:

            failing_tool_definitions: List[ToolDefinition] = (
                inspector.extract_tool_desc_from_tool_source(
                    Path(tool_definition_path),
                    tools_to_analyze,
                )
            )

            if not failing_tool_definitions:
                analysis_for_display.append(
                    warn(
                        message=f"No tool definitions(with '@tool' decorators) for failed tools: '{tools_to_analyze}' found in the file: '{tool_definition_path}'"
                    )
                )
                return analysis_for_display

            missing_tools = self._get_tools_not_found_in_source(
                tools_to_analyze, failing_tool_definitions
            )
            if missing_tools:
                analysis_for_display.append(
                    warn(
                        message=f"Missing tool definitions for failed tools: '{missing_tools}' in the file: '{tool_definition_path}'"
                    )
                )

            for tool_definition in failing_tool_definitions:

                tool_analysis = self._analyze_tool_definition(
                    inspector=inspector,
                    tool_definition=tool_definition,
                    tool_definition_path=tool_definition_path,
                )

                self.analysis_cache[tool_definition.tool_name] = tool_analysis
                analysis_for_display.extend(tool_analysis)

        return analysis_for_display

    def render(
        self,
        data: List[ExtendedMessage],
        tool_definition_path: Optional[str],
        meta: Optional[dict] = None,
    ) -> Group:
        """
        Render the conversation history and analysis results.
        :param data: List of ExtendedMessage objects containing the conversation history.
        :param tool_definition_path: Path to the tool definition file.
        :return: A rich Group object containing the conversation and analysis results.
        """
        conversation_lines = []
        reason_lines = []
        failing_tools = []
        added_errors_header = False
        added_missed_header = False

        for entry in data:
            msg = entry.message
            role = msg.role
            content = msg.content
            reason = entry.reason
            tool_name = None
            if (
                msg.type == ContentType.tool_call
                or msg.type == ContentType.tool_response
            ):
                tool_name = json.loads(msg.content)["name"]

            if role == "user":
                label = "👤 User"
            elif role == "assistant" and msg.type == ContentType.tool_call:
                if reason:
                    label = "❌ Tool Call"

                    if reason.get("reason") == "incorrect parameter":
                        failing_tools.append(
                            tool_name
                        )  # create a list of failing tools for description quality analysis.
                else:
                    label = "✅ Tool Call"
            elif role == "assistant":
                label = "🤖 Assistant"
            else:
                label = "📦 Unknown"

            text_line = Text(f"{label}: {content}\n")
            if reason:
                if not added_errors_header:
                    reason_lines.append(
                        Text("\nTool Call Errors:\n", style="bold red")
                    )
                    added_errors_header = True
                text_line.stylize("bold red")
                reason_text = f"❌ {tool_name}: {json.dumps(reason)}\n\n"
                reason_lines.append(Text(reason_text, style="red"))
            conversation_lines.append(text_line)

        if failing_tools and tool_definition_path:

            inspector = DescriptionQualityInspector()

            description_quality_inspection_lines = (
                self.analyze_failing_tool_description_quality(
                    inspector, tool_definition_path, set(failing_tools)
                )
            )

            print_done()

            if description_quality_inspection_lines:
                reason_lines.extend(description_quality_inspection_lines)

        if meta:
            missed = meta.get("missed_tool_calls") or []
            if missed:
                if not added_missed_header:
                    reason_lines.append(
                        Text("\nMissed Calls:\n", style="bold red")
                    )
                    added_missed_header = True
                for tool in missed:
                    reason_lines.append(Text(f"❌ {tool}\n", style="red"))

        conversation_panel = Panel(
            Text().join(conversation_lines),
            title="Conversation History",
            border_style="blue",
        )
        reason_panel = Panel(
            Text().join(reason_lines),
            title="Analysis Results",
            border_style="red",
        )

        return Group(
            conversation_panel,
            reason_panel,
        )

    def analyze(self, config: AnalyzeConfig):
        """
        Analyze the results of the tool calls and routing metrics.
        :param config: AnalyzeConfig object containing user provided paths for analysis.
        """

        def get_summary(summary_file_name: str = "summary_metrics.csv"):
            summary = []

            path_to_summary_file = os.path.join(
                config.data_path, summary_file_name
            )

            with open(path_to_summary_file, "r") as f:
                reader = csv.reader(f)
                header = next(reader)
                for row in reader:
                    summary.append(dict(zip(header, row)))

            return summary

        def get_test_messages(test_case_name):
            test_messages = []
            meta = {}

            test_case_path = os.path.join(
                config.data_path,
                "messages",
                f"{test_case_name}.messages.analyze.json",
            )

            with open(test_case_path, "r", encoding="utf-8") as f:
                temp = json.load(f)
                if temp and isinstance(temp[-1], dict) and "meta" in temp[-1]:
                    meta = temp[-1]["meta"]
                    temp = temp[:-1]

                for entry in temp:
                    msg = ExtendedMessage(**entry)
                    test_messages.append(msg)

            return test_messages, meta

        def get_metrics(test_case_name):
            test_metrics_path = os.path.join(
                config.data_path, "messages", f"{test_case_name}.metrics.json"
            )

            with open(test_metrics_path, "r", encoding="utf-8") as f:
                metrics = ToolCallAndRoutingMetrics(**json.load(f))

            return metrics

        summary = get_summary()

        test_case_with_failed_tools = self._get_test_case_with_failed_tools(
            summary=summary
        )

        if len(test_case_with_failed_tools) == 0:
            header_table = Table(show_header=False, box=None)

            header_table.add_row("No Tool Call Error found!")

            panel = Panel(
                header_table,
                title="[bold green]📋 Analysis Summary[/bold green]",
            )

            pretty_print(panel)

        messages_dir = os.path.join(config.data_path, "messages")

        RUN_NAME_ONLY_RE = re.compile(r"^(?P<parent>.+)\.run(?P<id>\d+)$")
        processed_parents: Set[str] = set()

        overall_runs_performed = 0
        overall_runs_problematic = 0
        overall_text_match_hits = 0
        overall_text_match_den = 0
        overall_journey_vals = []

        for test_case_entry in summary:
            dataset_base = test_case_entry["dataset_name"]

            # If CSV row looks like "<parent>.runN" and we have runs on disk for <parent>, skip the per-run row.
            m = RUN_NAME_ONLY_RE.match(dataset_base)
            if m:
                parent = m.group("parent")
                if list_run_files(messages_dir, parent):
                    continue

            # Avoid processing a parent twice if it appears multiple times in CSV.
            if dataset_base in processed_parents:
                continue

            run_map = list_run_files(messages_dir, dataset_base)

            # ---- SINGLE RUN (legacy or run1 only) ----
            if not run_map or len(run_map) == 1:
                if not run_map:
                    # Legacy single-run files
                    test_messages, meta = get_test_messages(
                        test_case_name=dataset_base
                    )
                    metrics: ToolCallAndRoutingMetrics = get_metrics(
                        test_case_name=dataset_base
                    )
                    runs_performed = 1
                else:
                    run_id = next(iter(run_map))
                    paths = run_map[run_id]
                    runs_performed = 1
                    if not paths["metrics"]:
                        pretty_print(
                            f"❌ {dataset_base}.run{run_id} — metrics file missing.",
                            style="bold red",
                        )
                        # Count it as analyzed & problematic
                        processed_parents.add(dataset_base)
                        ds_table = Table(show_header=False, box=None)
                        ds_table.add_row("Type: Single-run")
                        ds_table.add_row("Status: ❌ Problematic")
                        pretty_print(
                            Panel(
                                ds_table,
                                title=f"📋 Analysis Summary — {dataset_base}",
                                border_style="green",
                            )
                        )
                        overall_runs_performed += 1
                        overall_runs_problematic += 1
                        add_line_seperator(self._generate_style_config())
                        continue

                    metrics = load_run_metrics(paths["metrics"])
                    meta = {}

                    if paths["analyze"]:
                        with open(paths["analyze"], "r", encoding="utf-8") as f:
                            raw = json.load(f)
                        if (
                            raw
                            and isinstance(raw[-1], dict)
                            and "meta" in raw[-1]
                        ):
                            meta = raw[-1]["meta"]
                            raw = raw[:-1]
                        test_messages = [
                            ExtendedMessage(**entry) for entry in raw
                        ]
                    else:
                        test_messages, meta = [], {}

                # --- compute status uniformly (legacy & run1) ---
                had_incorrect_param = (
                    hasattr(metrics, "tool_calls_with_incorrect_parameter")
                    and float(metrics.tool_calls_with_incorrect_parameter or 0)
                    > 0
                )
                low_precision = (
                    hasattr(metrics, "tool_call_precision")
                    and float(
                        metrics.tool_call_precision
                        if metrics.tool_call_precision is not None
                        else 1.0
                    )
                    < 1.0
                )
                low_recall = (
                    hasattr(metrics, "tool_call_recall")
                    and float(
                        metrics.tool_call_recall
                        if metrics.tool_call_recall is not None
                        else 1.0
                    )
                    < 1.0
                )
                runs_problematic = (
                    1
                    if (
                        (
                            hasattr(metrics, "is_success")
                            and not metrics.is_success
                        )
                        or had_incorrect_param
                        or low_precision
                        or low_recall
                    )
                    else 0
                )

                processed_parents.add(dataset_base)

                # ✅ Dataset-level panel (print BEFORE details)
                ds_table = Table(show_header=False, box=None)
                ds_table.add_row("Type: Single-run")
                status = (
                    "❌ Problematic" if runs_problematic else "✅ No problems"
                )
                ds_table.add_row(f"Status: {status}")
                pretty_print(
                    Panel(
                        ds_table,
                        title=f"📋 Analysis Summary — {dataset_base}",
                        border_style="green",
                    )
                )

                # Update overall counters/averages
                overall_runs_performed += runs_performed
                overall_runs_problematic += runs_problematic
                tm = getattr(metrics, "text_match", None)
                tm_val = getattr(tm, "value", None) if tm else None

                if tm_val is not None and tm_val != TextMatchType.na:
                    overall_text_match_den += 1
                    overall_text_match_hits += (
                        tm_val == TextMatchType.text_match
                    )
                if getattr(metrics, "is_success", None) is not None:
                    overall_journey_vals.append(
                        1 if bool(metrics.is_success) else 0
                    )

                # Replay details only if problematic
                if runs_problematic:
                    pretty_print(
                        self._create_header_analysis_panel(
                            dataset_base, metrics
                        )
                    )
                    pretty_print(
                        self.render(
                            test_messages, config.tool_definition_path, meta
                        )
                    )
                    add_line_seperator(self._generate_style_config())

                continue

            # ---- MULTI RUN (two-pass: compute first, then print summary, then details) ----
            processed_parents.add(dataset_base)
            runs_performed = len(run_map)
            runs_problematic = 0
            text_match_hits = 0
            text_match_den = 0
            journey_vals = []

            # First pass: compute aggregates and collect problematic runs to replay later
            deferred_runs = []
            for run_id in sorted(run_map):
                paths = run_map[run_id]
                if not paths["metrics"]:
                    runs_problematic += 1
                    # no analyze file to replay; still counted as problematic
                    continue

                metrics = load_run_metrics(paths["metrics"])

                # Aggregate for per-dataset
                tm = getattr(metrics, "text_match", None)
                tm_val = getattr(tm, "value", None) if tm is not None else None
                if tm_val is not None and tm_val != TextMatchType.na.value:
                    text_match_den += 1
                    text_match_hits += tm_val == TextMatchType.text_match.value

                if getattr(metrics, "is_success", None) is not None:
                    journey_vals.append(1 if bool(metrics.is_success) else 0)

                # Decide if problematic
                had_incorrect_param = (
                    hasattr(metrics, "tool_calls_with_incorrect_parameter")
                    and float(metrics.tool_calls_with_incorrect_parameter or 0)
                    > 0
                )
                low_precision = (
                    hasattr(metrics, "tool_call_precision")
                    and float(
                        metrics.tool_call_precision
                        if metrics.tool_call_precision is not None
                        else 1.0
                    )
                    < 1.0
                )
                low_recall = (
                    hasattr(metrics, "tool_call_recall")
                    and float(
                        metrics.tool_call_recall
                        if metrics.tool_call_recall is not None
                        else 1.0
                    )
                    < 1.0
                )

                is_problem = (
                    (hasattr(metrics, "is_success") and not metrics.is_success)
                    or had_incorrect_param
                    or low_precision
                    or low_recall
                )
                if is_problem:
                    runs_problematic += 1
                    deferred_runs.append(
                        {
                            "title": f"{dataset_base}.run{run_id}",
                            "metrics": metrics,
                            "analyze_path": paths.get("analyze"),
                        }
                    )

            # Print the dataset panel FIRST with both lines inside
            ds_table = Table(show_header=False, box=None)
            ds_table.add_row(f"Type: Multi-run ({runs_performed} runs)")
            ds_table.add_row(
                f"Runs with problems: {runs_problematic} / {runs_performed}"
            )
            status = (
                "❌ Problematic" if runs_problematic > 0 else "✅ No problems"
            )
            ds_table.add_row(f"Status: {status}")
            pretty_print(
                Panel(
                    ds_table,
                    title=f"📋 Analysis Summary — {dataset_base}",
                    border_style="green",
                )
            )

            # Second pass: now replay only the problematic runs (so summary stays at the top)
            for item in deferred_runs:
                pretty_print(
                    self._create_header_analysis_panel(
                        item["title"], item["metrics"]
                    )
                )
                if item["analyze_path"]:
                    with open(item["analyze_path"], "r", encoding="utf-8") as f:
                        raw = json.load(f)
                    meta = {}
                    if raw and isinstance(raw[-1], dict) and "meta" in raw[-1]:
                        meta = raw[-1]["meta"]
                        raw = raw[:-1]
                    test_messages = [ExtendedMessage(**entry) for entry in raw]

                    pretty_print(
                        self.render(
                            test_messages, config.tool_definition_path, meta
                        )
                    )
                add_line_seperator(self._generate_style_config())

            # Update overall aggregates
            overall_runs_performed += runs_performed
            overall_runs_problematic += runs_problematic
            overall_text_match_hits += text_match_hits
            overall_text_match_den += text_match_den
            overall_journey_vals.extend(journey_vals)

        # --- Overall summary ---
        overall_lines = [
            f"Test cases analyzed: {len(processed_parents)}",
            f"Total runs executed: {overall_runs_performed}",
            f"Problematic runs: {overall_runs_problematic} ({round((overall_runs_problematic/overall_runs_performed)*100,1) if overall_runs_performed else 0}%)",
        ]

        if overall_text_match_den:
            tm_pct = round(
                (overall_text_match_hits / overall_text_match_den) * 100, 2
            )
            overall_lines.append(f"Avg text-match success: {tm_pct}%")
        else:
            overall_lines.append("Avg text-match success: N/A")

        if overall_journey_vals:
            js_pct = round(
                (sum(overall_journey_vals) / len(overall_journey_vals)) * 100, 2
            )
            overall_lines.append(f"Avg journey success: {js_pct}%")
        else:
            overall_lines.append("Avg journey success: N/A")

        pretty_print(
            Panel(
                Text("\n".join(overall_lines)),
                title="📋 Overall Summary",
                border_style="cyan",
            )
        )

    def _create_header_analysis_panel(
        self, test_case_name: str, metrics: ToolCallAndRoutingMetrics
    ) -> Panel:
        header_table = Table(show_header=False, box=None)

        header_table.add_row(f"Test Case Name: {test_case_name}")
        header_table.add_row(
            f"Expected Tool Calls: {metrics.expected_tool_calls}"
        )
        header_table.add_row(
            f"Correct Tool Calls: {metrics.correct_tool_calls}"
        )
        header_table.add_row(f"Text Match: {metrics.text_match.value}")
        header_table.add_row(f"Journey Success: {metrics.is_success}")

        header_panel = Panel(
            header_table, title="[bold green]Test Case Summary[/bold green]"
        )

        return header_panel

    def _get_test_case_with_failed_tools(self, summary) -> List:

        test_case_with_failed_tools = []

        for entry in summary:
            test_case_name = entry["dataset_name"]

            if test_case_name.lower().strip() == "summary (average)":
                continue

            is_success = str(entry["is_success"]).strip().lower() == "true"

            tip = float(
                entry.get("tool_calls_with_incorrect_parameter", 0) or 0
            )
            tcp = float(entry.get("tool_call_precision", 1) or 1)
            tcr = float(entry.get("tool_call_recall", 1) or 1)

            # Apply the 4 checks
            if (not is_success) or (tip > 0) or (tcp < 1.0) or (tcr < 1.0):
                test_case_with_failed_tools.append(entry)

        return test_case_with_failed_tools

    def _get_tools_not_found_in_source(
        self,
        tools_to_analyze: List[str],
        failing_tool_definitions: List[ToolDefinition],
    ) -> Set[str]:

        return set(tools_to_analyze) - {
            tool_def.tool_name for tool_def in failing_tool_definitions
        }

    def _analyze_tool_definition(
        self,
        inspector: DescriptionQualityInspector,
        tool_definition: ToolDefinition,
        tool_definition_path: str,
    ) -> List[Text]:

        tool_name = tool_definition.tool_name
        tool_desc = tool_definition.tool_description

        tool_analysis = []

        # missing description
        if tool_desc is None:
            tool_analysis.extend(
                IncorrectParameterUtils.format_missing_description_message(
                    tool_name=tool_name,
                    tool_definition_path=tool_definition_path,
                )
            )
            return tool_analysis

        # bad description
        if inspector.detect_bad_description(tool_definition):
            tool_analysis.extend(
                IncorrectParameterUtils.format_bad_description_message(
                    tool_name=tool_name, tool_desc=tool_desc
                )
            )
            return tool_analysis

        # good description
        tool_analysis.append(
            is_ok(
                message=f"The description for the `{tool_name}` looks sufficient."
            )
        )
        return tool_analysis


if __name__ == "__main__":
    dummy_analyzer = Analyzer()
    dummy_analyzer.analyze(CLI(AnalyzeConfig, as_positional=False))
