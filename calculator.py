from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    ConsoleSpanExporter,
    SimpleSpanProcessor,
)


trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

span_processor = SimpleSpanProcessor(ConsoleSpanExporter())
trace.get_tracer_provider().add_span_processor(span_processor)


class IntCalculator:
    """Integer Calculator class."""

    def add(self, a: int, b: int) -> int:
        """Add two integer numbers."""
        return a + b

    def subtract(self, a: int, b: int) -> int:
        """Subtract two integer numbers."""
        return a - b

    def multiply(self, a: int, b: int) -> int:
        """Multiply two integer numbers."""
        return a * b


with tracer.start_as_current_span("calculator-span"):
    calculator = IntCalculator()
    a = 2
    b = 3

    print(f"Sum of {a} and {b} is {calculator.add(a, b)}")
    print(f"Difference of {a} and {b} is {calculator.subtract(a, b)}")
    print(f"Product of {a} and {b} is {calculator.multiply(a, b)}")
