# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


# coding: utf-8

from __future__ import annotations

from datetime import date, datetime  # noqa: F401
from enum import Enum, IntEnum

import os
import re  # noqa: F401
from typing import Annotated, Any, Dict, List, Literal, Optional, Set, Type, Union, Callable, Iterable  # noqa: F401
from pathlib import Path
from typing import TypeVar
Model = TypeVar('Model', bound='BaseModel')
StrBytes = Union[str, bytes]

from pydantic import AnyUrl, BaseModel, EmailStr, Field, validator, root_validator, Extra,PrivateAttr  # noqa: F401
from pydantic import ValidationError
from pydantic.error_wrappers import ErrorWrapper
from pydantic.utils import ROOT_KEY
from json import encoder
from dnv_bladed_models.bladed_model import BladedModel

from .schema_helper import SchemaHelper
from .models_impl import *


class InterpolatedAerofoilLibrary(BladedModel):
    r"""
    A library of interpolated aerofoils, each of which has a 2D interpolation over thickness and Reynold's number.
    
    Attributes
    ----------
    Notes
    -----
    
    """

    _relative_schema_path = 'Components/Blade/InterpolatedAerofoilLibrary/InterpolatedAerofoilLibrary.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.allow
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def items(self) -> list[tuple[str, List[str]]]:
        """
        Returns a list of key-value pairs for all of the user-supplied entries currently in the model.
        """
        return [(k, self.__dict__[k]) for k in self.__dict__ if k not in self.__fields__]


    def keys(self) -> list[str]:
        """
        Returns a list of keys for all of the user-supplied entries currently in the model.
        """
        return [k for k in self.__dict__ if k not in self.__fields__]


    def values(self) -> list[List[str]]:
        """
        Returns a list of model objects for all of the user-supplied entries currently in the model.
        """
        return [self.__dict__[k] for k in self.__dict__ if k not in self.__fields__]


    def __len__(self):
        return len([k for k in self.__dict__ if k not in self.__fields__])


    def __contains__(self, item):
        for k in self.__dict__:
            if k not in self.__fields__ and k == item:
                return True
        return False


    def __getitem__(self, key: Union[str, int]) -> List[str]:
        if isinstance(key, int):
            keys = self.keys()
            if len(keys) == 0:
                raise KeyError(f"There are currently no entries in the model object.")
            if key < 0 or key >= len(keys):
                raise KeyError(f"Invalid index specified: {key} (0 >= i < {len(keys)})")
            key = keys[key]
        elif isinstance(key, str):
            if key in self.__fields__:
                raise KeyError(f"Item accessors can only be used for custom entries. '{key}' is a pre-defined model property.")
            if not key in self.__dict__:
                raise KeyError(f"There is no entry with key '{key}'.")
        return getattr(self, key)


    def __setitem__(self, key: str, value: List[str]):
        if not isinstance(key, str):
            raise KeyError(f"Custom entries can only be added with string keys")
        if key in self.__fields__:
            raise KeyError(f"Item accessors can only be used for custom entries. '{key}' is a pre-defined model property.")
        if not isinstance(value, List):
            raise TypeError(f"Entries must be of type 'List[str]'; received '{type(value).__name__}'")
        setattr(self, key, value)


    def __delitem__(self, key: Union[str, int]):
        if isinstance(key, int):
            keys = self.keys()
            if len(keys) == 0:
                raise KeyError(f"There are currently no entries in the model object.")
            if key < 0 or key >= len(keys):
                raise KeyError(f"Invalid index specified: {key} (0 >= i < {len(keys)})")
            key = keys[key]
        elif isinstance(key, str):
            if key in self.__fields__:
                raise KeyError(f"Item accessors can only be used for custom entries. '{key}' is a pre-defined model property.")
            if not key in self.__dict__:
                raise KeyError(f"There is no entry with key '{key}'.")
        delattr(self, key)


    def __setattr__(self, name: str, value: List[str]):
        if not name in self.__fields__ and not isinstance(value, List):
            raise TypeError(f"Entries must be of type 'List[str]'; received '{type(value).__name__}'")
        super().__setattr__(name, value)



    class __CustomEntries__(BaseModel):
        entries: Dict[str, List[str]]


    @classmethod
    def _model_factory(cls: Type['Model'], obj: dict[str, Any]) -> Model:
        return custom_entries_parser(cls, obj, List, InterpolatedAerofoilLibrary.__CustomEntries__)

    def _entity(self) -> bool:
        return True


InterpolatedAerofoilLibrary.update_forward_refs()
InterpolatedAerofoilLibrary.__CustomEntries__.update_forward_refs()
