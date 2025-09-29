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
class InitialCondition_InitialConditionTypeEnum(str, Enum):
    GL2010_ICING = "GL2010Icing"
    IEC4_ICING = "IEC4Icing"
    INITIAL_AZIMUTH_POSITION = "InitialAzimuthPosition"
    INITIAL_FLOATING_POSITION = "InitialFloatingPosition"
    INITIAL_PITCH_POSITION = "InitialPitchPosition"
    INITIAL_ROTOR_SPEED = "InitialRotorSpeed"
    INITIAL_YAW_ANGLE = "InitialYawAngle"
    ROTOR_IDLING = "RotorIdling"
    ROTOR_IN_POWER_PRODUCTION = "RotorInPowerProduction"
    ROTOR_PARKED = "RotorParked"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class InitialCondition(BladedModel, ABC):
    r"""
    A condition of the turbine or a component at the beginning of the simulation.  This may change during the simulation.
    
    Attributes
    ----------
    InitialConditionType : InitialCondition_InitialConditionTypeEnum
        Defines the specific type of model in use.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - GL2010Icing
        - IEC4Icing
        - InitialAzimuthPosition
        - InitialFloatingPosition
        - InitialPitchPosition
        - InitialRotorSpeed
        - InitialYawAngle
        - InitialConditionInsert
        - RotorIdlingControlState
        - RotorInPowerProduction
        - RotorParkedControlState
    
    """
    InitialConditionType: InitialCondition_InitialConditionTypeEnum = Field(alias="InitialConditionType", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


InitialCondition.update_forward_refs()
