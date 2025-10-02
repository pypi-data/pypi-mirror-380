
from acex.core.configuration.components import ConfigComponent
from acex.core.configuration.components.interfaces import (
    Loopback,
    Physical
)

from acex.core.models import ExternalValue

from typing import Dict

class Configuration:
    def __init__(self, logical_node_id):
        self.components: Dict[str, ConfigComponent] = {}
        self.logical_node_id = logical_node_id

    def add(self, component: ConfigComponent):
        """
        Lagrar komponent i Configuration object, 
        använder path som nyckel. Varje komponent måste ha
        en hashbar path.
        """
        # For all external values, set reference!
        for k,v in component.attributes().items():
            if isinstance(v, ExternalValue):
                
                v.ref = self.path_to_component(component)

        # Add to config object
        self.components[component.path] = component

    def path_to_component(self, component):
        return f"logical_nodes.{self.logical_node_id}.{component.path}"

    def to_json(self):
        """
        Serialisera alla komponenter till en dict (utan att resolva DataSourceValue).
        Nyckeln är component.path.
        """
        return {component.path: component.to_json() for component in self.components.values()}

