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

from .schema_helper import SchemaHelper
from .models_impl import *


class AerodynamicInformationCalculation(SteadyCalculation):
    r"""
    Defines a calculation which produces the aerodynamic parameters of the rotor in a steady flow, including local aerodynamic loading at each blade station.  The rotor is modelled as being completely rigid in this calculation, without prebend and sweep.  The rotor is analysed in isolation without any influence from the rest of the turbine structure.
    
    Attributes
    ----------
    SteadyCalculationType : Literal['AerodynamicInformation'], default='AerodynamicInformation'
        Defines the specific type of SteadyCalculation model in use.  For a `AerodynamicInformation` object, this must always be set to a value of `AerodynamicInformation`.
    
    HubWindSpeed : float
        The wind speed at hub height.
    
    PitchAngle : float
        The pitch angle of all of the blades on the rotor or rotors.
    
    RotorSpeed : float
        The rotor speed to model during the calculation.
    
    Outputs : SteadyCalculationOutputs
    
    Notes
    -----
    
    """
    SteadyCalculationType: Literal['AerodynamicInformation'] = Field(alias="SteadyCalculationType", default='AerodynamicInformation', allow_mutation=False, const=True) # type: ignore
    HubWindSpeed: float = Field(alias="HubWindSpeed", default=None)
    PitchAngle: float = Field(alias="PitchAngle", default=None)
    RotorSpeed: float = Field(alias="RotorSpeed", default=None)
    Outputs: SteadyCalculationOutputs = Field(alias="Outputs", default=None)

    _relative_schema_path = 'SteadyCalculation/AerodynamicInformationCalculation.json'
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


AerodynamicInformationCalculation.update_forward_refs()
