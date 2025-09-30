from contextlib import contextmanager
import logging
from typing import Any

from kcai._version_ import version


logger = logging.getLogger(__name__)


@contextmanager
def optional_dependencies(error: str = "ignore"):
    assert error in {"raise", "warn", "ignore"}
    try:
        yield None
    except ImportError as e:
        if error == "raise":
            raise e
        if error == "warn":
            msg = f'Missing optional dependency "{e.name}". Use pip to install.'
            print(f"Warning: {msg}")


def display_version(arg_list: list[str] | None = None):
    print(f"Klarity Craft version : {version}")


def display_list_of(arg_list: list[str] | None = None):
    # TODO : we display all but we can filter / use extra parameters
    print("Available plugin")
    # for key, value in PluginLoadedRegistry.metrics_registry.items():
    #    print(f"- {key} - {value}")


def get_available_command() -> dict[str, Any]:
    command_list = {"version": display_version, "list": display_list_of}
    optional_dep_mode = "warn"

    # We import available command for kcai_artefact cli
    with optional_dependencies(optional_dep_mode):
        #from kcai_artefact._version_ import version as pipeline_version
        #from kcai_artefact.cli import execute

        #logger.debug(f"Different kcai_artefact version {pipeline_version}")
        #command_list["process"] = execute

    return command_list
