# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


# coding: utf-8

from __future__ import annotations

from abc import ABC

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
from dnv_bladed_models.vector3_d import Vector3D
class NacelleSensor_NacelleSensorTypeEnum(str, Enum):
    ACCELEROMETER = "Accelerometer"
    INCLINOMETER = "Inclinometer"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class NacelleSensor(BladedModel, ABC):
    r"""
    The common properties of a sensor mounted on the nacelle.  This can be mounted anywhere on the structure.
    
    Attributes
    ----------
    NacelleSensorType : NacelleSensor_NacelleSensorTypeEnum
        Defines the specific type of model in use.
    
    OffsetFromOrigin : Vector3D
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - NacelleAccelerometer
        - NacelleInclinometer
        - NacelleSensorInsert
    
    """
    NacelleSensorType: NacelleSensor_NacelleSensorTypeEnum = Field(alias="NacelleSensorType", default=None)
    OffsetFromOrigin: Vector3D = Field(alias="OffsetFromOrigin", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


NacelleSensor.update_forward_refs()
