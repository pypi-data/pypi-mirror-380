from pydantic import BaseModel, Field
from typing import Union, Dict

class DataSourceValue(BaseModel):
    value: Union[str, int, None] = None
    ref: Union[str, None] = None

    def resolve(self, data_sources: Dict[str, "DataSource"]):
        if self.ref:
            # ex: "data.ipam_prefix.servers_subnet.prefix"
            parts = self.ref.split(".")
            ds_name, attr = parts[3], parts[-1]
            ds = data_sources.get(ds_name)
            if ds is None:
                raise ValueError(f"Data source '{ds_name}' not found")
            return ds.resolved[attr]
        return self.value