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
from dnv_bladed_models.applied_load import AppliedLoad

from .schema_helper import SchemaHelper
from .models_impl import *


class BladePointLoading(AppliedLoad):
    r"""
    A time history of point loading applied to a blade.
    
    Attributes
    ----------
    AppliedLoadType : Literal['BladePointLoading'], default='BladePointLoading'
        Defines the specific type of AppliedLoad model in use.  For a `BladePointLoading` object, this must always be set to a value of `BladePointLoading`.
    
    DistanceAlongBlade : float
        The distance along the reference axis of the blade to apply the loading.
    
    Notes
    -----
    
    """
    AppliedLoadType: Literal['BladePointLoading'] = Field(alias="AppliedLoadType", default='BladePointLoading', allow_mutation=False, const=True) # type: ignore
    DistanceAlongBlade: float = Field(alias="DistanceAlongBlade", default=None)

    _relative_schema_path = 'TimeDomainSimulation/AppliedLoad/BladePointLoading.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'AppliedLoadType').merge(AppliedLoad._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


BladePointLoading.update_forward_refs()
