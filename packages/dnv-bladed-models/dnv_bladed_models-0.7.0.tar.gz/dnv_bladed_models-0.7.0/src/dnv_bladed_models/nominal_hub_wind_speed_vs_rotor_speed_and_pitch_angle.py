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


class NominalHubWindSpeedVsRotorSpeedAndPitchAngle(BladedModel):
    r"""
    The look-up table for specifying the nominal free-field wind speed at the hub against the turbine's operating condition appropriate for that wind speed.  Wind speeds need to be in monotonic ascending order. Linear interpolation is used between points. The lowest value for the hub wind speed will be taken as the cut-in wind speed for the turbine, and the highest the cut-out wind speed.
    
    Attributes
    ----------
    NominalHubWindSpeed : float
        The nominal free-field wind speed at the hub.
    
    RotorSpeed : float
        The rotor speed to apply for the specified hub wind speed in steady state/initial condition calculations. The generator torque will be calculated to achieve this rotor speed.  If the torque required is negative, a warning will be generated.
    
    PitchAngle : float
        The pitch angle to apply to all blades for the specified hub wind speed in steady state/initial condition calculations.
    
    Notes
    -----
    
    """
    NominalHubWindSpeed: float = Field(alias="NominalHubWindSpeed", default=None)
    RotorSpeed: float = Field(alias="RotorSpeed", default=None)
    PitchAngle: float = Field(alias="PitchAngle", default=None)

    _relative_schema_path = 'Turbine/TurbineOperationalParameters/NominalHubWindSpeedVsRotorSpeedAndPitchAngle/NominalHubWindSpeedVsRotorSpeedAndPitchAngle.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


NominalHubWindSpeedVsRotorSpeedAndPitchAngle.update_forward_refs()
