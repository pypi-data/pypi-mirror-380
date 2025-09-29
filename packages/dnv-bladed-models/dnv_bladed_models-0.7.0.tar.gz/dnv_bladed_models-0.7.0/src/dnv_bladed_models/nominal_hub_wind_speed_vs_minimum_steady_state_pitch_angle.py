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


class NominalHubWindSpeedVsMinimumSteadyStatePitchAngle(BladedModel):
    r"""
    The look-up table for specifying the nominal free-field wind speed at the hub against the respective minimum pitch angle for pitch scheduling. Wind speeds need to be in monotonic ascending order. Linear interpolation is used between points. If the hub wind speed exceeds the specified value the nearest will be used and a warning message will be written.
    
    Attributes
    ----------
    HubWindSpeed : float
        The nominal free-field wind speed at the hub for which the minimum pitch angle will apply.
    
    MinimumSteadyStatePitchAngle : float
        The minimum pitch angle demand of the blades that the turbine control will apply for the specified wind speed.  The initial conditions may choose a higher pitch angle in order to achieve an equilibrium, but not a lower one.
    
    Notes
    -----
    
    """
    HubWindSpeed: float = Field(alias="HubWindSpeed", default=None)
    MinimumSteadyStatePitchAngle: float = Field(alias="MinimumSteadyStatePitchAngle", default=None)

    _relative_schema_path = 'Turbine/TurbineOperationalParameters/VariableSpeedPitchRegulatedControlModel/NominalHubWindSpeedVsMinimumSteadyStatePitchAngle/NominalHubWindSpeedVsMinimumSteadyStatePitchAngle.json'
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


NominalHubWindSpeedVsMinimumSteadyStatePitchAngle.update_forward_refs()
