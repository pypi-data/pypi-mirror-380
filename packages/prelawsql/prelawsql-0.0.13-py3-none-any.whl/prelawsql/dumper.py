from typing import Any

import yaml
from yaml import CSafeDumper as SafeDumper
from yaml.nodes import Node


def represent_ordereddict(
    dumper: yaml.Dumper, data: dict[Any, Any]
) -> yaml.nodes.MappingNode:
    """Custom representer to ensure dictionaries preserve insertion order when dumped to YAML.

    Args:
        dumper (yaml.Dumper): The YAML dumper in use (e.g., CSafeDumper).
        data (dict): The dictionary to represent.

    Returns:
        yaml.nodes.MappingNode: A YAML mapping node preserving the order of items.

    Examples:
        >>> import yaml
        >>> from yaml import CSafeDumper as SafeDumper
        >>> from collections import OrderedDict
        >>> SafeDumper.add_representer(dict, represent_ordereddict)
        >>> SafeDumper.add_representer(OrderedDict, represent_ordereddict)
        >>> data = OrderedDict([("a", 1), ("b", 2), ("c", 3)])
        >>> print(yaml.dump(data, Dumper=SafeDumper, sort_keys=False))
        a: 1
        b: 2
        c: 3
        <BLANKLINE>
    """
    value = []

    for item_key, item_value in data.items():
        node_key = dumper.represent_data(item_key)
        node_value = dumper.represent_data(item_value)

        value.append((node_key, node_value))

    return yaml.nodes.MappingNode("tag:yaml.org,2002:map", value)


SafeDumper.add_representer(dict, represent_ordereddict)  # type: ignore
