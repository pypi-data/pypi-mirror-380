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
from dnv_bladed_models.full_load_operation import FullLoadOperation
from dnv_bladed_models.nominal_hub_wind_speed_vs_minimum_steady_state_pitch_angle import NominalHubWindSpeedVsMinimumSteadyStatePitchAngle
from dnv_bladed_models.partial_load_operation import PartialLoadOperation

from .schema_helper import SchemaHelper
from .models_impl import *


class VariableSpeedPitchRegulatedControlModel(BladedModel):
    r"""
    The operational parameters that Bladed uses to determine the steady state conditions of the turbine. Although some of the values will be made available to the external controller through the API, they will not be used by Bladed during the remainder of a time domain simulation.
    
    Attributes
    ----------
    MinimumSteadyStatePitchAngle : float
        This value represents the minimum allowable blade pitch angle used for determining pitch angle during steady state/initial condition calculation. It is combined with the MaximumSteadyStatePitchAngle to define the allowable pitch range. Additionally, the external controller API can access this value.
    
    MaximumSteadyStatePitchAngle : float
        This value represents the minimum allowable blade pitch angle used for determining pitch angle during steady state/initial condition calculation. It is combined with the MinimumSteadyStatePitchAngle to define the allowable pitch range. Please note that the steady-state algorithm does not support overspeed steady state conditions in cases where rotor speeds exceed the specified value for FullLoadOperation::GeneratorSpeed. Additionally, this value is accessible via the external controller API.
    
    NominalHubWindSpeedVsMinimumSteadyStatePitchAngle : List[NominalHubWindSpeedVsMinimumSteadyStatePitchAngle]
        The look-up table for specifying hub wind speed against the respective minimum pitch angle for pitch scheduling. Wind speeds need to be in monotonic ascending order. Linear interpolation is used between points. If the hub wind speed exceeds the specified value the nearest will be used and a warning message will be written.
    
    PartialLoadOperation : PartialLoadOperation
    
    FullLoadOperation : FullLoadOperation
    
    Notes
    -----
    
    """
    MinimumSteadyStatePitchAngle: float = Field(alias="MinimumSteadyStatePitchAngle", default=None)
    MaximumSteadyStatePitchAngle: float = Field(alias="MaximumSteadyStatePitchAngle", default=None)
    NominalHubWindSpeedVsMinimumSteadyStatePitchAngle: List[NominalHubWindSpeedVsMinimumSteadyStatePitchAngle] = Field(alias="NominalHubWindSpeedVsMinimumSteadyStatePitchAngle", default=list())
    PartialLoadOperation: PartialLoadOperation = Field(alias="PartialLoadOperation", default=None)
    FullLoadOperation: FullLoadOperation = Field(alias="FullLoadOperation", default=None)

    _relative_schema_path = 'Turbine/TurbineOperationalParameters/VariableSpeedPitchRegulatedControlModel/VariableSpeedPitchRegulatedControlModel.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['NominalHubWindSpeedVsMinimumSteadyStatePitchAngle',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


VariableSpeedPitchRegulatedControlModel.update_forward_refs()
