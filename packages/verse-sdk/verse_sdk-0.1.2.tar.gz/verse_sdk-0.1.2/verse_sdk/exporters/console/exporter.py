from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import SpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor

from ...processors import ScopeFilterProcessor
from ..base import Exporter
from ..types import ExporterConfig


class ConsoleExporter(Exporter):
    config: ExporterConfig

    def __init__(self, config: ExporterConfig):
        self.config = config

    def create_span_processor(self, resource: Resource) -> SpanProcessor:
        """Create a span processor for the console exporter w/ scope filtering."""
        exporter = ScopeFilterProcessor(
            ConsoleSpanExporter(),
            self.config,
        )

        return SimpleSpanProcessor(exporter)
