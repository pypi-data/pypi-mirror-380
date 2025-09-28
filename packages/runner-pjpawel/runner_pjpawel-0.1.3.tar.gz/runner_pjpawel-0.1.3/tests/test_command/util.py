import logging
import sys

from src.runner_pjpawel.command.base import (
    BaseCommand,
    CommandResult,
    RunnerRuntimeError,
)


class RuntimeExceptionCommand(BaseCommand):

    def _do_work(self) -> CommandResult | None:
        raise RunnerRuntimeError(CommandResult.new_error(), 5)


def get_stdout_logger(name: str = __name__, level=logging.INFO) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid adding duplicate handlers if called multiple times
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)

        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger
