import pytest

from climate_ref_core.exceptions import (
    InvalidDiagnosticException,
    InvalidExecutorException,
    InvalidProviderException,
)


@pytest.mark.parametrize(
    "exception_cls, message",
    [
        (InvalidProviderException, "provider"),
        (InvalidDiagnosticException, "diagnostic"),
        (InvalidExecutorException, "executor"),
    ],
)
def test_exception_message(exception_cls, message):
    exception = exception_cls("test", "test_message")
    assert str(exception) == f"Invalid {message}: 'test'\n test_message"
