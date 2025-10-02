
from ipaddress import IPv4Interface, IPv6Interface
from pydantic import BaseModel

import json, hashlib
from typing import Dict, Any

import json, hashlib
from typing import Type

from acex.core.configuration.datasource_value import DataSourceValue

class ConfigComponent:
    type: str = "component"
    model_cls: Type[BaseModel] = None  # sätts i subklasser
    primary_key_field: str = "name"      # kan överridas i subklass

    def __init__(self, **kwargs):

        # Set primary key
        try:
            self._key = kwargs.get(str(self.__class__.primary_key_field))
        except AttributeError as e:
            raise ValueError(f"Missing required key attribute in {self.__class__.__name__}: {e}")

        # Set path to component
        self.path = f"{self.type}.{self._key}"

    @property
    def model(self):
        """
        Returnera objektet som den modell som ska returneras.
        Sätter bara attribut som definierats upp i modellen.
        """
        as_dict = {}

        # Set primary key in response:
        as_dict[self.__class__.primary_key_field] = self._key

        # Set type
        as_dict["type"] = self.__class__.type

        for attr in self.__class__.model_cls().model_fields:
            value = getattr(self, attr, None)
            if value is not None:
                as_dict[attr] = value

        m = self.__class__.model_cls(**as_dict)
        return self.__class__.model_cls(**as_dict)


    def attributes(self):
        if not self.model:
            return {}
        result = {}
        for k, v in self.model.dict().items():
            if isinstance(v, DataSourceValue):
                # lämna som ref tills resolve körs
                result[k] = v
            else:
                result[k] = v
        return result

    def resolve_attributes(self, data_sources: dict):
        for k, v in self.attributes().items():
            if isinstance(v, DataSourceValue):
                resolved_value = v.resolve(data_sources)
                setattr(self.model, k, resolved_value)


    def hash(self):
        canonical = json.dumps({
            "type": self.type,
            "primary_key": self._key,
            "attributes": {k: str(v) for k, v in self.attributes().items()}
        }, sort_keys=True)
        return hashlib.sha256(canonical.encode()).hexdigest()


    def to_json(self):
        """
        Serialisera alla attribut och deras värden till en dict.
        DataSourceValue serialiseras som sitt value/ref (ej resolvat).
        Nested ConfigComponent serialiseras rekursivt.
        """
        result = {}
        for k, v in self.model.dict().items():
            if isinstance(v, ConfigComponent):
                result[k] = v.to_json()
            elif isinstance(v, list):
                result[k] = [item.to_json() if isinstance(item, ConfigComponent) else str(item) if isinstance(item, (IPv4Interface, IPv6Interface)) else item for item in v]
            elif isinstance(v, (IPv4Interface, IPv6Interface)):
                result[k] = str(v)
            elif hasattr(v, "dict") and callable(v.dict):
                # t.ex. pydantic submodell
                result[k] = v.dict()
            elif hasattr(v, "to_json") and callable(v.to_json):
                result[k] = v.to_json()
            elif hasattr(v, "value") and hasattr(v, "ref"):
                # DataSourceValue
                result[k] = {"value": v.value, "ref": v.ref}
            else:
                result[k] = v
        return result


    def __repr__(self):
        return f"<{self.__class__.__name__} pk={self._key} path={self.path}>"







# class ConfigComponent: 

#     def __init__(self, *args, **kwargs): 
        
#         # Getting the primary sort key based on cls var
#         # from child class definition. 
#         # _key attribute is used for sorting components in configuration
#         self._key_name = self.__class__.KEY
#         self._model = self.__class__.MODEL

#         if self._key_name in kwargs:
#             self._key = kwargs.get(self._key_name)
#         else:
#             raise ValueError(f"Missing required key attribute '{self._key_name}' for {self.__class__.__name__}")

#     def validate(self):
#         """
#         Validaes the component's attributes against its model.
#         Check all typing and constraints.
#         """
#         try:
#             self._model(**self.__dict__)
#         except Exception as e:
#             raise ValueError(f"Validation error in {self.__class__.__name__}: {e}")


#     def process(self):
#         """
#         Process body, for instance compute derived attributes 
#         such as ip address/subnetmask/prefixlen from ip interface.
#         """
#         model_representation = self._model(**self.__dict__)

#         for k, v in model_representation.__dict__.items():
#             if isinstance(v, (IPv4Interface, IPv6Interface)):
#                 new_value = {
#                     "ip_address": str(v.ip),
#                     "subnet_mask": str(v.network.netmask),
#                     "prefix_len": v.network.prefixlen
#                 }
#                 setattr(self, k, new_value)


#     def to_json(self):
#         self.validate()
#         self.process()
#         response = {}

#         # Based on the model injected in child component definition
#         valid_attributes = self._model.model_fields.keys()

#         # Insert sorting key first
#         response[self._key_name] = self._key

#         for key in valid_attributes:
#             value = getattr(self, key, None)

#             if key.startswith('_') or value is None:
#                 continue

#             if isinstance(value, ConfigComponent):
#                 response[key] = value.to_json()
#             elif isinstance(value, list):
#                 response[key] = [v.to_json() if isinstance(v, ConfigComponent) else v for v in value]
#             elif isinstance(value, IPv4Interface):
#                 response[key] = f"IP ADDRESS: {str(value)}"
#             else:
#                 response[key] = value

#         # if attribute is not in the model, add it to custom_attributes
#         for key, value in self.__dict__.items():
#             if key in valid_attributes:
#                 continue
#             if key.startswith('_') or value is None:
#                 continue

#             response["custom_attributes"] = {}

#             if isinstance(value, ConfigComponent):
#                 response["custom_attributes"][key] = value.to_json()
#             elif isinstance(value, list):
#                 response["custom_attributes"][key] = [v.to_json() if isinstance(v, ConfigComponent) else v for v in value]
#             else:
#                 response["custom_attributes"][key] = value

#         return response