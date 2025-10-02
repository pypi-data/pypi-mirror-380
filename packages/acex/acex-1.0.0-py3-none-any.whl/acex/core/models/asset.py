from typing import Optional, Dict, List
from sqlmodel import SQLModel, Field, Relationship


class Ned(SQLModel, table=True):
    name: str = Field(default="cisco_ios_ssh", primary_key=True)
    version: str = Field(default="0.0.1")

class AssetBase(SQLModel):
    vendor: str = Field(default="cisco")
    serial_number: str = Field(default="abc123")
    os: str = Field(default="ios")
    os_version: str = Field(default="12.0.1")
    hardware_model: str = Field(default="")
    ned_id: Optional[str] = None


class Asset(AssetBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    interfaces: List["AssetInterface"] = Relationship(back_populates="asset")


class AssetInterface(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    asset_id: Optional[int] = Field(default=None, foreign_key="asset.id")
    asset: Asset = Relationship(back_populates="interfaces")



class AssetResponse(AssetBase):
    id: int
    meta_data: Dict = Field(default_factory=dict)