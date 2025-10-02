from typing import Optional, Dict, List, Union
from sqlmodel import SQLModel, Field
from ipaddress import IPv4Interface
from pydantic import validator

from acex.core.models import ExternalValue

class Interface(SQLModel): ...

class PhysicalInterface(SQLModel):
    @validator("switchport_mode")
    def validate_switchport_mode(cls, v):
        if v is not None and v not in ("access", "trunk"):
            raise ValueError("switchport_mode must be 'access' or 'trunk' if set")
        return v
    type: str = Field(default="")
    index: int = Field(default=0)
    enabled: bool = Field(default=True)
    description: Optional[str] = None
    mac_address: Optional[str] = None
    ipv4_address: Optional[Union[IPv4Interface, ExternalValue]] = None
    speed: Optional[int] = None  # Speed in KBps
    switchport: Optional[bool] = None
    switchport_mode: Optional[str] = None  # e.g., 'access', 'trunk'
    switchport_untagged_vlan: Optional[int] = None
    switchport_trunk_vlans: Optional[List[int]] = None


class VirtualInterface(Interface):
    pass

