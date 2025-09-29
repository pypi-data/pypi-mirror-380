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
from dnv_bladed_models.steady_calculation_with_component_outputs import SteadyCalculationWithComponentOutputs
from dnv_bladed_models.velocity_range import VelocityRange

from .schema_helper import SchemaHelper
from .models_impl import *


class SteadyOperationalLoadsCalculation(SteadyCalculation):
    r"""
    Defines a calculation which produces all the loads in a steady, uniform wind field.  The entire turbine is modelled for this analysis and prebend and sweep included, as well as flexibility.  Most realities such as tower shadow and wind shear are ignored.
    
    Attributes
    ----------
    SteadyCalculationType : Literal['SteadyOperationalLoads'], default='SteadyOperationalLoads'
        Defines the specific type of SteadyCalculation model in use.  For a `SteadyOperationalLoads` object, this must always be set to a value of `SteadyOperationalLoads`.
    
    WindSpeedRange : VelocityRange
    
    Outputs : SteadyCalculationWithComponentOutputs
    
    Notes
    -----
    
    """
    SteadyCalculationType: Literal['SteadyOperationalLoads'] = Field(alias="SteadyCalculationType", default='SteadyOperationalLoads', allow_mutation=False, const=True) # type: ignore
    WindSpeedRange: VelocityRange = Field(alias="WindSpeedRange", default=None)
    Outputs: SteadyCalculationWithComponentOutputs = Field(alias="Outputs", default=None)

    _relative_schema_path = 'SteadyCalculation/SteadyOperationalLoadsCalculation.json'
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


SteadyOperationalLoadsCalculation.update_forward_refs()
