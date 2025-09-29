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
from dnv_bladed_models.meandering_wake import MeanderingWake
from dnv_bladed_models.position_of_upwind_turbine import PositionOfUpwindTurbine
from dnv_bladed_models.wake_properties_of_upstream_turbine import WakePropertiesOfUpstreamTurbine

from .schema_helper import SchemaHelper
from .models_impl import *


class DynamicUpstreamWake(BladedModel):
    r"""
    
    
    Attributes
    ----------
    RadialStepSize : float, default=0.05
        The resolution of the wake deficit profile in the radial direction.
    
    NumberOfRadialPoints : int, default=50
        The total number of points in the radial wake deficit profile.
    
    StreamwiseStep : float, default=0.1
        The integration step in streamwise direction for the propagation of the wake.
    
    MixingLength : float, default=1.323
        The length scale of the part of ambient turbulence which affects the wake deficit evolution.
    
    ShearCalibrationConstant : float, default=0.008
        The calibration factor for self-generated turbulence.  IEC edition 4 recommends a value of 0.008.
    
    AmbientCalibrationConstant : float, default=0.023
        The calibration factor for influence of ambient turbulence.  IEC edition 4 recommends a value of 0.023.
    
    PositionOfUpwindTurbine : PositionOfUpwindTurbine
    
    WakePropertiesOfUpstreamTurbine : WakePropertiesOfUpstreamTurbine
    
    MeanderingWake : MeanderingWake
    
    Notes
    -----
    
    """
    RadialStepSize: float = Field(alias="RadialStepSize", default=None)
    NumberOfRadialPoints: int = Field(alias="NumberOfRadialPoints", default=None)
    StreamwiseStep: float = Field(alias="StreamwiseStep", default=None)
    MixingLength: float = Field(alias="MixingLength", default=None)
    ShearCalibrationConstant: float = Field(alias="ShearCalibrationConstant", default=None)
    AmbientCalibrationConstant: float = Field(alias="AmbientCalibrationConstant", default=None)
    PositionOfUpwindTurbine: PositionOfUpwindTurbine = Field(alias="PositionOfUpwindTurbine", default=None)
    WakePropertiesOfUpstreamTurbine: WakePropertiesOfUpstreamTurbine = Field(alias="WakePropertiesOfUpstreamTurbine", default=None)
    MeanderingWake: MeanderingWake = Field(alias="MeanderingWake", default=None)

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/DynamicUpstreamWake/DynamicUpstreamWake.json'
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


DynamicUpstreamWake.update_forward_refs()
