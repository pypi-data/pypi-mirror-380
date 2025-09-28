import logging
import subprocess
import threading
from typing import Callable

from .base import BaseCommand, CommandResult, CommandResultLevel, RunnerRuntimeError, ErrorStrategy


class ShellCommand(BaseCommand):
    def __init__(self, cmd, cwd=None, **kwargs):
        super().__init__(**kwargs)
        self.cwd = cwd
        self.cmd = cmd

    def _do_work(self) -> CommandResult | None:
        process = subprocess.Popen(
            self.cmd,
            cwd=self.cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = process.communicate()
        level = (
            CommandResultLevel.OK
            if process.returncode == 0
            else CommandResultLevel.ERROR
        )
        self._log(logging.DEBUG, f"Process return code: {process.returncode}. Stdout: {stdout}, stderr: {stderr}")
        return CommandResult(level, stdout, [stderr])


class GroupCommand(BaseCommand):
    """
    DEVELOPMENT PENDING
    GroupCommand treats all commands as one.
    So depends on set strategy, it will retry, omit all process or throw error if one of command fails.
    It is possible to define reset callback that must have arguments BaseCommand (processed that failed) and CommandResult (result) that returns None or BaseCommand to be executed
    """

    commands: list[BaseCommand]
    reset_callback: Callable[[BaseCommand, CommandResult], None | BaseCommand] | None
    iteration: int = 0

    def __init__(self, commands=None, reset_callback=None, **kwargs):
        super().__init__(**kwargs)
        self.commands = [] if commands is None else commands
        self.reset_callback = reset_callback

    def add_command(self, command: BaseCommand):
        self.commands.append(command)

    def set_commands(self, commands: list[BaseCommand]):
        self.commands = commands

    def get_number_of_works(self) -> int:
        return sum(command.number_of_works for command in self.commands)

    def _do_work(self) -> CommandResult | None:
        self._log(logging.DEBUG, f"Starting group command with {self.get_number_of_works()} commands")
        i = 0
        try:
            self._log(logging.INFO, f"Starting iteration {i}")
            while i < len(self.commands):
                self.commands[i].process()
        except RunnerRuntimeError as rre:
            if self.reset_callback is not None:
                command = self.reset_callback(self.commands[i], rre.result)
                if command is not None:
                    command.process()
            match self.error_strategy:
                case ErrorStrategy.OMIT:
                    return
                case ErrorStrategy.STOP:
                    raise rre
                case ErrorStrategy.RESTART:
                    self.iteration += 1
                    self._do_work()


class ParallelCommand(GroupCommand):
    """
    DEVELOPMENT PENDING
    Creates two threads and run them parallelly
    """

    def __init__(self, commands: list[BaseCommand], **kwargs):
        if kwargs.get("number_of_works") is not None:
            kwargs["number_of_works"] = sum(
                command.number_of_works for command in commands
            )
        super().__init__(**kwargs)
        self.commands = commands

    def _do_work(self) -> CommandResult | None:
        threads = []
        for command in self.commands:
            thread = threading.Thread(target=command.process)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()  # TODO: get results and output


class CyclicCommand(BaseCommand):
    """
    DEVELOPMENT PENDING
    Handles jobs that should be run more than once
    """

    def __init__(self, command: BaseCommand, cycles: int, **kwargs):
        if kwargs.get("number_of_works") is not None:
            kwargs["number_of_works"] = command.number_of_works * cycles
        super().__init__(**kwargs)
        self.command = command
        self.cycles = cycles

    def _do_work(self) -> CommandResult | None:
        for _ in range(self.cycles):
            self.command.process()  # TODO: handle error


class ThreadCommand(BaseCommand):
    cmd: Callable
    args: list = []
    timeout: float | None

    def __init__(
        self, command: Callable, args=None, timeout: float | None = None, **kwargs
    ):
        super().__init__(**kwargs)
        if args is None:
            args = []
        self.cmd = command
        self.args = args
        self.timeout = timeout

    def _do_work(self) -> CommandResult | None:
        thread = threading.Thread(target=self.cmd, args=self.args)
        thread.start()
        thread.join(self.timeout)
        if thread.is_alive():
            return CommandResult.new_error("Thread timeout")
        return CommandResult.new_ok()
