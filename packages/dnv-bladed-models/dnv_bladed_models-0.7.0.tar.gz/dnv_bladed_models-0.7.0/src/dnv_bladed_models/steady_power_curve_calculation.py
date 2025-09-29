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
from dnv_bladed_models.steady_calculation import SteadyCalculation
from dnv_bladed_models.steady_calculation_outputs import SteadyCalculationOutputs
from dnv_bladed_models.velocity_range import VelocityRange

from .schema_helper import SchemaHelper
from .models_impl import *


class SteadyPowerCurveCalculation(SteadyCalculation):
    r"""
    Defines a calculation which produces power, torque and thrust as a function of wind speed, assuming a uniform steady wind field.  The entire turbine is modelled for this analysis and prebend and sweep included, but without any flexibility.  Most realities such as tower shadow and wind shear are ignored.
    
    Not supported yet.
    
    Attributes
    ----------
    SteadyCalculationType : Literal['SteadyPowerCurve'], default='SteadyPowerCurve', Not supported yet
        Defines the specific type of SteadyCalculation model in use.  For a `SteadyPowerCurve` object, this must always be set to a value of `SteadyPowerCurve`.
    
    WindSpeedRange : VelocityRange
    
    CalculateSpeedAndPitchChange : bool, Not supported yet
        If true, the pitch and speed change schedule will be calculated by Bladed.
    
    PitchAngle : float, Not supported yet
        The pitch angle of all of the turbine blades to be considered for the calculation.
    
    RotorSpeed : float, Not supported yet
        The rotor speed to be considered for the calculation.
    
    Outputs : SteadyCalculationOutputs
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    SteadyCalculationType: Literal['SteadyPowerCurve'] = Field(alias="SteadyCalculationType", default='SteadyPowerCurve', allow_mutation=False, const=True) # Not supported yet # type: ignore
    WindSpeedRange: VelocityRange = Field(alias="WindSpeedRange", default=None)
    CalculateSpeedAndPitchChange: bool = Field(alias="CalculateSpeedAndPitchChange", default=None) # Not supported yet
    PitchAngle: float = Field(alias="PitchAngle", default=None) # Not supported yet
    RotorSpeed: float = Field(alias="RotorSpeed", default=None) # Not supported yet
    Outputs: SteadyCalculationOutputs = Field(alias="Outputs", default=None)

    _relative_schema_path = 'SteadyCalculation/SteadyPowerCurveCalculation.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'SteadyCalculationType').merge(SteadyCalculation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


SteadyPowerCurveCalculation.update_forward_refs()
