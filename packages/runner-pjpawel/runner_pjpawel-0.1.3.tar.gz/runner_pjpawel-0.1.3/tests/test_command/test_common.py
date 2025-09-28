import logging
import pytest

from src.runner_pjpawel.command.base import (
    CommandResultLevel, RunnerRuntimeError,
)
from src.runner_pjpawel.command.common import ShellCommand, GroupCommand
from tests.test_command.util import RuntimeExceptionCommand, get_stdout_logger



def test_shell_command_uname():
    shell = ShellCommand("uname")
    res = shell.process()

    assert res.level == CommandResultLevel.OK
    assert res.msg == "Linux\n"
    assert res.additional_info == [""]


def test_runtime_error_thrown():
    cmd = RuntimeExceptionCommand()
    with pytest.raises(RunnerRuntimeError):
        cmd.process()

def test_group_command():
    logger_name = "tgc"
    get_stdout_logger(logger_name, logging.DEBUG)
    group = GroupCommand(logger_name=logger_name, log_level=logging.DEBUG)
    c1 = ShellCommand("uname -a", logger_name=logger_name, log_level=logging.DEBUG)
    group.add_command(c1)
    c2 = ShellCommand("ls -al", logger_name=logger_name, log_level=logging.DEBUG)
    group.add_command(c2)

    rs = group.process()
    assert rs.level == CommandResultLevel.OK


def test_group_command_restart():
    group = GroupCommand(error_strategy="restart")
    c1 = RuntimeExceptionCommand()
    group.add_command(c1)
    c2 = ShellCommand("ls -al")
    group.add_command(c2)

    group.process()
