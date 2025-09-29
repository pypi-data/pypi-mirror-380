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
from dnv_bladed_models.angle_range import AngleRange
from dnv_bladed_models.dimensionless_range import DimensionlessRange
from dnv_bladed_models.steady_calculation import SteadyCalculation
from dnv_bladed_models.steady_calculation_outputs import SteadyCalculationOutputs

from .schema_helper import SchemaHelper
from .models_impl import *


class PerformanceCoefficientsCalculation(SteadyCalculation):
    r"""
    Defines a calculation which produces power, torque and thrust coefficients are calculated in a uniform steady wind field.  The rotor is modelled with flexibility as well as prebend and sweep.  However, the rotor is analysed in isolation without any influence from the rest of the turbine structure.
    
    Attributes
    ----------
    SteadyCalculationType : Literal['PerformanceCoefficients'], default='PerformanceCoefficients'
        Defines the specific type of SteadyCalculation model in use.  For a `PerformanceCoefficients` object, this must always be set to a value of `PerformanceCoefficients`.
    
    TipSpeedRatioRange : DimensionlessRange
    
    PitchRange : AngleRange
    
    RotorSpeed : float
        The rotor speed to be considered for the calculation.
    
    Outputs : SteadyCalculationOutputs
    
    Notes
    -----
    
    """
    SteadyCalculationType: Literal['PerformanceCoefficients'] = Field(alias="SteadyCalculationType", default='PerformanceCoefficients', allow_mutation=False, const=True) # type: ignore
    TipSpeedRatioRange: DimensionlessRange = Field(alias="TipSpeedRatioRange", default=None)
    PitchRange: AngleRange = Field(alias="PitchRange", default=None)
    RotorSpeed: float = Field(alias="RotorSpeed", default=None)
    Outputs: SteadyCalculationOutputs = Field(alias="Outputs", default=None)

    _relative_schema_path = 'SteadyCalculation/PerformanceCoefficientsCalculation.json'
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


PerformanceCoefficientsCalculation.update_forward_refs()
