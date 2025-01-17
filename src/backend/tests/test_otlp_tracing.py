import sys
import os
import pytest
from unittest.mock import patch, MagicMock

# Add the backend directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from otlp_tracing import configure_oltp_tracing  # Import directly since it's in backend


@patch("otlp_tracing.OTLPSpanExporter")
@patch("otlp_tracing.BatchSpanProcessor")
@patch("otlp_tracing.TracerProvider")
@patch("otlp_tracing.trace")
@patch("otlp_tracing.Resource")
def test_configure_oltp_tracing(
    mock_resource, mock_trace, mock_tracer_provider, mock_batch_processor, mock_otlp_exporter
):
    # Mock objects
    mock_resource.return_value = {"service.name": "macwe"}
    mock_tracer_provider_instance = MagicMock()
    mock_tracer_provider.return_value = mock_tracer_provider_instance
    mock_batch_processor.return_value = MagicMock()
    mock_otlp_exporter.return_value = MagicMock()

    # Call the function
    endpoint = "mock-endpoint"
    tracer_provider = configure_oltp_tracing(endpoint=endpoint)

    # Assertions
    mock_tracer_provider.assert_called_once_with(resource={"service.name": "macwe"})
    mock_otlp_exporter.assert_called_once()
    mock_batch_processor.assert_called_once_with(mock_otlp_exporter.return_value)
    mock_tracer_provider_instance.add_span_processor.assert_called_once_with(
        mock_batch_processor.return_value
    )
    mock_trace.set_tracer_provider.assert_called_once_with(mock_tracer_provider_instance)

    assert tracer_provider == mock_tracer_provider_instance