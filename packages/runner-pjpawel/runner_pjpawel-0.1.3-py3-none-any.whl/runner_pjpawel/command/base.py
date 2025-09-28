import logging
import subprocess
import threading
from enum import IntEnum, StrEnum, auto
from typing import Callable, Self

from ..counter import Counter, Timer


class CommandResultLevel(IntEnum):
    OK = 0
    ERROR = 1
    CRITICAL = 2


class CommandResult:
    level: CommandResultLevel
    msg: str | None
    additional_info: list

    def __init__(
        self, level: CommandResultLevel, msg: str | None = None, additional_info=None
    ):
        self.level = level
        self.msg = msg
        if additional_info is None:
            additional_info = []
        self.additional_info = additional_info

    @staticmethod
    def new_ok(msg: str | None = None, additional_info=None):
        return CommandResult(CommandResultLevel.OK, msg, additional_info)

    @staticmethod
    def new_error(msg: str | None = None, additional_info=None):
        return CommandResult(CommandResultLevel.ERROR, msg, additional_info)

    @staticmethod
    def new_critical(msg: str | None = None, additional_info=None):
        return CommandResult(CommandResultLevel.CRITICAL, msg, additional_info)

    def __str__(self):
        return f"CommandResult({self.level})"

    def __repr__(self):
        return f"CommandResult({self.level.__repr__()})"


class RunnerRuntimeError(RuntimeError):

    def __init__(self, result: CommandResult, retry: int):
        self.result = result
        self.retry = retry

    def __str__(self):
        return f"RunnerRuntimeException({self.result.__str__()}, {self.retry})"

    def __repr__(self):
        return f"RunnerRuntimeException({self.result.__repr__()}, {self.retry})"


class ErrorStrategy(StrEnum):
    RESTART = auto()
    STOP = auto()
    OMIT = auto()


class ConditionResult(IntEnum):
    OK = 0
    STOP = 1

class BaseCommand:
    number_of_works: int
    log_level: int
    logger_name: str | None
    error_strategy: ErrorStrategy
    error_callback: Callable[[Self, CommandResult], Self | None] | None
    condition: Callable[[], CommandResult] | None # TODO: change signature

    def __init__(self, **kwargs):
        self.logger = None
        self.log_level = int(kwargs.get("log_level", logging.WARNING))
        self.logger_name = kwargs.get("logger_name", None)
        self.error_strategy = ErrorStrategy(
            kwargs.get("error_strategy", "stop").lower()
        )

    def process(self):
        return self._do_process()

    def _do_process(self, iteration: int = 1):
        if iteration > 3:
            return CommandResult.new_critical("Cannot run process. ", {"command": self})
        timer = Timer()
        try:
            result = self._do_work()
            if result is None:
                result = CommandResult.new_ok()
            timer.add_checkpoint("Done working")
        except RunnerRuntimeError as ree:
            timer.add_checkpoint("RuntimeException thrown")
            timer.stop()
            self._log(logging.ERROR, f"Runner stoped due to error {ree}")
            raise ree
        except Exception as e:
            result = CommandResult(
                CommandResultLevel.ERROR, "Unexcepted exception caught", [e]
            )
        match result.level:
            case CommandResultLevel.OK:
                self._increment_counter()
                timer.stop()
                self._log(logging.DEBUG, "Result OK")
                self._log_timer(timer)
                return result
            case CommandResultLevel.ERROR:
                match self.error_strategy:
                    case ErrorStrategy.OMIT:
                        timer.stop()
                        self._log(logging.INFO, "Omitting error")
                        self._log_timer(timer)
                        return result
                    case ErrorStrategy.RESTART:
                        timer.stop()
                        self._log(
                            logging.INFO, f"Restarting process, attempt {iteration}"
                        )
                        self._log_timer(timer)
                        return self._do_process(iteration + 1)
                    case ErrorStrategy.STOP:
                        timer.stop()
                        self._log(logging.INFO, f"Process stopped with result {result}")
                        self._log_timer(timer)
                        return result
            case CommandResultLevel.CRITICAL:
                timer.stop()
                self._log(logging.CRITICAL, f"Process critical error {result}")
                self._log_timer(timer)
                raise RunnerRuntimeError(result, iteration)

    def _do_work(self) -> CommandResult | None:
        raise NotImplementedError("Subclasses must implement this method")

    def _increment_counter(self):
        Counter.increment()

    def get_number_of_works(self) -> int:
        return 1

    def _log_timer(self, timer: Timer):
        self._log(logging.DEBUG, f"Timer: {timer}")

    def _log(self, level: int, message: str):
        if self.logger is None:
            if self.logger_name:
                self.logger = logging.getLogger(self.logger_name)
            else:
                return
        # if self.log_level <= level:
            # self.logger.log(level, self._format_log(message))
        self.logger.log(level, self._format_log(message))

    def _format_log(self, message: str):
        return "Class: {0}, Work: {1}: {2}".format(
            self.__class__.__name__, Counter.get_count(), message
        )
