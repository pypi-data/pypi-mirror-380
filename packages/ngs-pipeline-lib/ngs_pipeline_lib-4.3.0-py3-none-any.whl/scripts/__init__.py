import importlib
import logging
import sys

from pydantic import BaseSettings

from ngs_pipeline_lib.cli import cli

from .docker import build, push

logger = logging.getLogger("ngs-run")


class RunSettings(BaseSettings):
    process_package: str = "src"


def run():
    settings = RunSettings()
    # TODO : check for best practices to enable current dir in the python path
    sys.path.insert(0, ".")
    importlib.import_module(settings.process_package, package=".")

    try:
        cli()
    except ValueError as e:
        logger.error(
            "Specified module doesn't contain any @cli.command. Check your PROCESS_PACKAGE env var"
        )
        raise e
