
from acex.core.configuration.components.base_component import ConfigComponent
from acex.core.models.interfaces import PhysicalInterface, VirtualInterface




# class InterfaceBase(ConfigComponent):
#     def __init__(self, name: str, vlan: int, mode: str = "access", enabled: bool = True):
#         super().__init__(type="interface", name=name, attributes={
#             "vlan": vlan, "mode": mode, "enabled": enabled
#         })


class Physical(ConfigComponent):
    type = "physical_interface"
    primary_key_field = "index"
    model_cls = PhysicalInterface


# class Physical(InterfaceBase): 
#     KEY = "index"
#     MODEL = PhysicalInterface


# class Virtual(InterfaceBase):
#     KEY = "index"
#     MODEL = VirtualInterface


class Loopback(): ...
# class Vlan(Virtual):  ...




