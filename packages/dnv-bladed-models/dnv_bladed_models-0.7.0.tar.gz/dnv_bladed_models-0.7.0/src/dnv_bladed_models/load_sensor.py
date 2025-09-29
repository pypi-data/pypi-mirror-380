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


class LoadSensor(Sensor):
    r"""
    A load sensor affixed to a component.  This will provide six channels of loading information to the external controller, one for each orthogonal force or moment.
    
    Attributes
    ----------
    SensorType : Literal['LoadSensor'], default='LoadSensor'
        Defines the specific type of Sensor model in use.  For a `LoadSensor` object, this must always be set to a value of `LoadSensor`.
    
    Notes
    -----
    
    """
    SensorType: Literal['LoadSensor'] = Field(alias="SensorType", default='LoadSensor', allow_mutation=False, const=True) # type: ignore

    _relative_schema_path = 'Components/common/LoadSensor.json'
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


LoadSensor.update_forward_refs()
