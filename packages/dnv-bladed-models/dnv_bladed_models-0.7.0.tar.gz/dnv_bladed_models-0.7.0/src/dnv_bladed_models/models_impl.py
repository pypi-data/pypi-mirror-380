# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Type, TypeVar, Union
from abc import ABC, abstractmethod
from pydantic import BaseModel, ValidationError, root_validator, PrivateAttr
from pydantic.error_wrappers import ErrorWrapper
from pydantic.utils import ROOT_KEY
TPydanticModel = TypeVar('TPydanticModel', bound='BaseModel')
TEntity = TypeVar('TEntity', bound='BladedEntity')

@dataclass(frozen=True)
class TypeInfo:
    discriminated_props: set[Tuple[str, str]]
    discriminated_arrays: set[Tuple[str, str]]
    containers: set[str]
    discriminator: Optional[str] = None

    def merge(self, other: 'TypeInfo') -> 'TypeInfo':
        return TypeInfo(
            self.discriminated_props.union(other.discriminated_props),
            self.discriminated_arrays.union(other.discriminated_arrays),
            self.containers.union(other.containers),
            other.discriminator if self.discriminator is None else self.discriminator)


class BladedEntity(BaseModel, ABC):

    _incoming_fields: set[str] = PrivateAttr(default_factory=lambda: set())
    _type_info: TypeInfo = TypeInfo(set(), set(), set())
   
    @abstractmethod
    def _entity(self) -> bool:
        pass


    @root_validator(pre=True)
    def _remove_underscore_fields(cls, values: Dict[str, Any]):
        remove_underscore_fields(values)
        return values


    @classmethod
    def _model_factory(cls: Type['TPydanticModel'], obj: dict[str, Any]) -> TPydanticModel:
        return super().parse_obj(obj)


    @classmethod
    def parse_obj(cls: Type['TEntity'], obj: dict[str, Any]) -> 'TEntity':
        """
        Create a new model instance from a dictionary of properties.
        """
        obj_as_dict = prepare_model_dict(cls, obj, cls._type_info.discriminated_props, cls._type_info.discriminated_arrays)
        model = cls._model_factory(obj_as_dict)
        model._incoming_fields.update(obj_as_dict.keys())
        return model


    @classmethod
    def __get_validators__(cls):
        yield cls._validator


    @classmethod
    def _validator(cls, data):
        if isinstance(data, cls):
            return data
        return cls.parse_obj(data)


    @property
    def is_insert(self) -> bool:
        """
        Returns true if the model is to be loaded from an external resource by the Bladed application; i.e. the 'insert' field is set with a resource location.
        """
        if 'insert' in self.__fields_set__:
            insert_val = self.__dict__['insert']
            return insert_val is not None and insert_val != ''
        return False

    
    def _find_unused_containers(self) -> Set[str]:
        unused_containers: Set[str] = set()
        for container in self._type_info.containers:
            if container in self.__dict__:
                container_obj = self.__dict__[container]
                if container_obj is not None and len(container_obj) == 0 and container not in self._incoming_fields:
                    if isinstance(container_obj, BladedEntity):
                        if container_obj._is_unused():
                            unused_containers.add(container)
                    else:
                        unused_containers.add(container)
        return unused_containers


    def _is_unused(self) -> bool:
        """
        Returns true if the model has no user-supplied values. This indicates the object should not be rendered in the final JSON output.
        """
        candidate_fields = [x[1] for x in self.__dict__.items() if x[0] != self._type_info.discriminator]
        return (len(candidate_fields) == 0 or all(map(lambda f: f is None, candidate_fields)))


    def _iter( # type: ignore
        self,
        **kwargs: Any
    ):
        if self.is_insert:
            kwargs['exclude'] = None
            kwargs['include'] = set(['insert'])
        else:
            exclude: Optional[Set[str]] = kwargs.get('exclude', set())
            if exclude is None:
                exclude = self._find_unused_containers()
            else:
                exclude.update(self._find_unused_containers())
            kwargs['exclude'] = exclude
        return super()._iter(**kwargs)


def remove_underscore_fields(values: Dict[str, Any]):
    to_remove: Set[str] = set()
    for child_name, child in values.items():
        if child_name.startswith('_'):
            to_remove.add(child_name)
        elif isinstance(child, dict):
            remove_underscore_fields(child)
        elif isinstance(child, list):
            for item in child:
                if isinstance(item, dict):
                    remove_underscore_fields(item)
    for x in to_remove:
        del values[x]


def prepare_dict_for_discriminated_insert(cls, field_name: str, field_obj: dict, discriminator_prop: str):
    if isinstance(field_obj, dict) and '$insert' in field_obj:
        if discriminator_prop in field_obj and field_obj[discriminator_prop] is not None and field_obj['$insert'] is not None:
            exc = ValueError(f"Cannot set both {discriminator_prop} and $insert fields.")
            raise ValidationError([ErrorWrapper(exc, loc=field_name)], cls)
        field_obj[discriminator_prop] = 'Insert'


def prepare_list_for_discriminated_insert(cls, field_name: str, field_obj: dict, discriminator_prop: str):
    if isinstance(field_obj, list):
        i = 0
        for item in field_obj:
            if isinstance(item, dict) and '$insert' in item:
                if discriminator_prop in item and item[discriminator_prop] is not None and item['$insert'] is not None:
                    exc = ValueError(f"Cannot set both {discriminator_prop} and $insert fields.")
                    raise ValidationError([ErrorWrapper(exc, loc=f"{field_name}[{i}]")], cls)
                item[discriminator_prop] = 'Insert'
            i += 1
    

def ensure_dict_for_parse(cls, data) -> dict:
    obj = cls._enforce_dict_if_root(data)
    if not isinstance(obj, dict):
        try:
            obj = dict(obj)
        except (TypeError, ValueError) as e:
            exc = TypeError(f'{cls.__name__} expected dict not {obj.__class__.__name__}')
            raise ValidationError([ErrorWrapper(exc, loc=ROOT_KEY)], cls) from e
    return obj


TParsedObj = TypeVar('TParsedObj', bound=BaseModel)
def prepare_model_dict(cls : Type[TParsedObj], obj: Any, discriminated_props: set[Tuple[str, str]], discriminated_arrays: set[Tuple[str, str]]) -> dict:
    obj_as_dict = ensure_dict_for_parse(cls, obj)
    if any(discriminated_props) or any(discriminated_arrays):
        for field_name, discriminator in discriminated_props:
            if field_name in obj_as_dict:
                prepare_dict_for_discriminated_insert(cls, field_name, obj_as_dict[field_name], discriminator)
        for field_name, discriminator in discriminated_arrays:
            if field_name in obj_as_dict:
                prepare_list_for_discriminated_insert(cls, field_name, obj_as_dict[field_name], discriminator)
    return obj_as_dict


TRawContainer = TypeVar('TRawContainer')
def custom_entries_parser(cls, obj, valid_raw_type: Type[TRawContainer], entry_model: Type, prepare_data: Optional[Callable[[str, TRawContainer], None]] = None):
    data_dict = ensure_dict_for_parse(cls, obj)

    ctor_data = {}
    entry_data = {}
    field_keys = set(val.alias or val.name for val in cls.__fields__.values())
    for key, val in data_dict.items():
        if not key in field_keys and not key.startswith('_') and isinstance(val, valid_raw_type):
            if prepare_data is not None:
                prepare_data(key, val)
            entry_data[key] = val
        else:
            ctor_data[key] = val

    instance = cls(**ctor_data)
    try:
        container = entry_model.parse_obj({ 'entries' : entry_data })
        for key, val in container.entries.items():
            setattr(instance, key, val)
    except ValidationError as e:
        raise ValidationError([ErrorWrapper(e, loc=cls.__name__)], cls)
           
    return instance


