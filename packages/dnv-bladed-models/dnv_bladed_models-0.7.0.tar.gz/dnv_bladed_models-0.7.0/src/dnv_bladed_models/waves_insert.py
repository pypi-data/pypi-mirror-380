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
from dnv_bladed_models.waves import Waves

from .schema_helper import SchemaHelper
from .models_impl import *


class WavesInsert(BladedEntity):
    r"""
    A Waves is to be inserted from an external resource. The exact type of Waves is not currently known.
    
    Attributes
    ----------
    WavesType : Literal['Insert'], default='Insert'
        For internal use when reading & writing JSON.
    
    insert : str
        A path to a resource from which a valid JSON model object can be resolved. All properties will be taken from the resolved object; no properties can be specified in-line.

    Notes
    -----
    
    """
    WavesType: Literal['Insert'] = Field(alias="WavesType", default='Insert', allow_mutation=False, const=True) # type: ignore
    insert: str = Field(alias="$insert", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'WavesType').merge(BladedEntity._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    @property
    def is_insert(self) -> bool:
        """
        Returns true if the model is to be loaded from an external resource by the Bladed application; i.e. the 'insert' field is set with a resource location.
        """
        return True


    def _entity(self) -> bool:
        return True


WavesInsert.update_forward_refs()
