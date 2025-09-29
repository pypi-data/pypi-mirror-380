from importlib.metadata import entry_points
import logging
import sys
from typing import Any

from dqm_ml_core.data_processor import DatametricProcessor

logger = logging.getLogger(__name__)


# TODO once a base class for all registry created, dict shall have dict[str, base_class]
def load_registered_plugins(plugin_group: str, base_class: Any, base_name: str = "default") -> dict[str, Any]:
    try:
        # python 3.10+
        plugin_entry_points = entry_points(group=plugin_group)
    except TypeError:
        # Old version for older python version

        logger.warning(f"Old python version still supported for python 3.6 to 3.9 : {sys.version_info}")

        if sys.version_info < (3, 10, 0) and sys.version_info >= (3, 5, 0):
            plugin_entry_points = entry_points()[plugin_group]
        else:
            logger.warning(f"Impossible to import plugin with python < 3.6 : {sys.version_info}")
            return {}

    registry = {}
    for v in plugin_entry_points:
        # Filter base class registry (not callable)
        if v.name != base_name:
            obj = v.load()
            if base_class is None or issubclass(obj, base_class):
                logger.debug(f"Referencing {plugin_group} - {v.name} class {obj} from {base_class}")
                registry[v.name] = obj
            else:
                logger.error(f"Entry point {plugin_group} - {v.name} class {obj} not derived from {base_class} ignored")

    # return a dict to class builder registry
    return registry


class PluginLoadedRegistry:
    """
    Class to provide access to registered object for metrics, dataloader, or output writter
    """

    metrics_registry: dict[str, Any] = load_registered_plugins("dqm_ml.metrics", DatametricProcessor)
    dataloaders_registry: dict[str, Any] = load_registered_plugins("dqm_ml.dataloaders", None)  # TODO add base class
    outputwiter_registry: dict[str, Any] = load_registered_plugins("dqm_ml.outputwiter", None)  # TODO add base class
