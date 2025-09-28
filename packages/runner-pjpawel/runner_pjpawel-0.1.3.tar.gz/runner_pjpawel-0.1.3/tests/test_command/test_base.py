import pytest

from src.runner_pjpawel.command.base import (
    CommandResult,
    CommandResultLevel,
    RunnerRuntimeError,
)
from src.runner_pjpawel.command.common import ShellCommand
from .util import RuntimeExceptionCommand


# CommandResult tests
def test_command_result_ok():
    msg = "dummy"
    result = CommandResult.new_ok(msg)

    assert result.level == CommandResultLevel.OK
    assert result.msg == msg
    assert result.additional_info == []


def test_command_result_error():
    msg = "dummy1"
    result = CommandResult.new_error(msg)

    assert result.level == CommandResultLevel.ERROR
    assert result.msg == msg
    assert result.additional_info == []


def test_command_result_critical():
    msg = "dummy2"
    result = CommandResult.new_critical(msg)

    assert result.level == CommandResultLevel.CRITICAL
    assert result.msg == msg
    assert result.additional_info == []


def test_command_result_str():
    msg = "dummy"
    result = CommandResult.new_ok(msg)

    assert str(result) == "CommandResult(0)"

