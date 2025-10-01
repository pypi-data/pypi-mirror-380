import json

import pytest

from verse_sdk import verse

verse.init(
    app_name="test_context_managers",
    exporters=[verse.exporters.console()],
)


def parse_spans(out: str) -> list[dict]:
    """Parse the spans from the output."""
    spans = []
    buffer = ""
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        buffer += line
        if buffer.count("{") == buffer.count("}"):
            try:
                span = json.loads(buffer)
                spans.append(span)
            except json.JSONDecodeError:
                pass
            buffer = ""

    spans.reverse()
    return spans


@pytest.mark.asyncio
async def test_context_managers(capfd):
    with verse.trace(name="test_trace") as trace:
        trace.input("test_input")
        trace.output("test_output")

        with verse.span(name="test_span") as span:
            span.input("test_span_input")
            span.output("test_span_output")

            with verse.generation(name="test_generation") as generation:
                generation.model("test_model")
                generation.input("test_generation_input")
                generation.output("test_generation_output")

    out, _ = capfd.readouterr()
    spans = parse_spans(out)
    assert len(spans) == 3

    assert spans[0]["name"] == "test_trace"
    assert spans[0]["attributes"]["input"] == "test_input"
    assert spans[0]["attributes"]["output"] == "test_output"
    trace_id = spans[0]["context"]["trace_id"]

    assert spans[1]["name"] == "test_span"
    assert spans[1]["context"]["trace_id"] == trace_id
    assert spans[1]["attributes"]["input"] == "test_span_input"
    assert spans[1]["attributes"]["output"] == "test_span_output"

    assert spans[2]["name"] == "test_generation"
    assert spans[2]["context"]["trace_id"] == trace_id
    assert spans[2]["attributes"]["gen_ai.request.model"] == "test_model"
    assert spans[2]["attributes"]["gen_ai.prompt"] == "test_generation_input"
    assert spans[2]["attributes"]["gen_ai.completion"] == "test_generation_output"
