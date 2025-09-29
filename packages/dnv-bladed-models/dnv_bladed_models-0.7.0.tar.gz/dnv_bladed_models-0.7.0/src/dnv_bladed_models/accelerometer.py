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
from dnv_bladed_models.sensor import Sensor

from .schema_helper import SchemaHelper
from .models_impl import *


class Accelerometer(Sensor):
    r"""
    An accelerometer affixed to a component.
    
    Attributes
    ----------
    SensorType : Literal['Accelerometer'], default='Accelerometer'
        Defines the specific type of Sensor model in use.  For a `Accelerometer` object, this must always be set to a value of `Accelerometer`.
    
    IncludeAccelerationDueToGravity : bool, default=False
        When this feature is enabled, the accelerometer will always record a downwards acceleration due to gravity in addition to the local acceleration of the structure.
    
    Notes
    -----
    
    """
    SensorType: Literal['Accelerometer'] = Field(alias="SensorType", default='Accelerometer', allow_mutation=False, const=True) # type: ignore
    IncludeAccelerationDueToGravity: bool = Field(alias="IncludeAccelerationDueToGravity", default=None)

    _relative_schema_path = 'Components/common/Accelerometer.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'SensorType').merge(Sensor._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


Accelerometer.update_forward_refs()
