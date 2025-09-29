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
class Brake_BrakeTypeEnum(str, Enum):
    NON_LINEAR_SHAFT_BRAKE = "NonLinearShaftBrake"
    SIMPLE_SHAFT_BRAKE = "SimpleShaftBrake"
    INSERT = "Insert"
class Brake_BrakePositionEnum(str, Enum):
    LOW_SPEED_SHAFT_ROTOR_END = "LOW_SPEED_SHAFT_ROTOR_END"
    LOW_SPEED_SHAFT_GEARBOX_END = "LOW_SPEED_SHAFT_GEARBOX_END"
    HIGH_SPEED_SHAFT_GEARBOX_END = "HIGH_SPEED_SHAFT_GEARBOX_END"
    HIGH_SPEED_SHAFT_GENERATOR_END = "HIGH_SPEED_SHAFT_GENERATOR_END"

from .schema_helper import SchemaHelper
from .models_impl import *


class Brake(BladedModel, ABC):
    r"""
    The common properties of all brakes in the drivetrain.
    
    Attributes
    ----------
    BrakeType : Brake_BrakeTypeEnum
        Defines the specific type of model in use.
    
    BrakePosition : Brake_BrakePositionEnum
        Which shaft the brake is acting on.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - BrakeInsert
        - NonLinearShaftBrake
        - SimpleShaftBrake
    
    """
    BrakeType: Brake_BrakeTypeEnum = Field(alias="BrakeType", default=None)
    BrakePosition: Brake_BrakePositionEnum = Field(alias="BrakePosition", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


Brake.update_forward_refs()
