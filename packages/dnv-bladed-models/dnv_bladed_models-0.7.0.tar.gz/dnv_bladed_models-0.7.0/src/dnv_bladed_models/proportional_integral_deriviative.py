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
from dnv_bladed_models.response_to_demand import ResponseToDemand
class ProportionalIntegralDeriviative_DifferentialGainActionEnum(str, Enum):
    ERROR = "Error"
    FEEDBACK = "Feedback"
    SETPOINT = "Setpoint"

from .schema_helper import SchemaHelper
from .models_impl import *


class ProportionalIntegralDeriviative(ResponseToDemand):
    r"""
    Defines an proportional, integral, deriviative (PID) response to the controller's demands.
    
    Attributes
    ----------
    ResponseToDemandType : Literal['ProportionalIntegralDeriviative'], default='ProportionalIntegralDeriviative'
        Defines the specific type of ResponseToDemand model in use.  For a `ProportionalIntegralDeriviative` object, this must always be set to a value of `ProportionalIntegralDeriviative`.
    
    ProportionalGain : float, default=0
        The gain on the contemporaneous error.
    
    IntegralGain : float, default=0
        The gain on the integral from time zero till the present of the error signal.
    
    DifferentialGain : float, default=0
        The gain the filtered derivative of the error.  The derivative of the error is passed through a low-pass filter.
    
    DifferentialGainAction : ProportionalIntegralDeriviative_DifferentialGainActionEnum, default='Feedback'
        The proportional and integral terms are apllied on error.  Derivative term may also be applied on the feedback or setpoint signals.
    
    DifferentialGainTimeConstant : float, default=0
        The derivative term uses a low-pass filter on input.
    
    DesaturationTimeConstant : float, default=0
        The time constant for when the output exceeds the limits.
    
    Notes
    -----
    
    """
    ResponseToDemandType: Literal['ProportionalIntegralDeriviative'] = Field(alias="ResponseToDemandType", default='ProportionalIntegralDeriviative', allow_mutation=False, const=True) # type: ignore
    ProportionalGain: float = Field(alias="ProportionalGain", default=None)
    IntegralGain: float = Field(alias="IntegralGain", default=None)
    DifferentialGain: float = Field(alias="DifferentialGain", default=None)
    DifferentialGainAction: ProportionalIntegralDeriviative_DifferentialGainActionEnum = Field(alias="DifferentialGainAction", default=None)
    DifferentialGainTimeConstant: float = Field(alias="DifferentialGainTimeConstant", default=None)
    DesaturationTimeConstant: float = Field(alias="DesaturationTimeConstant", default=None)

    _relative_schema_path = 'Components/PitchSystem/PitchController/PitchSystemDemand/ResponseToDemand/ProportionalIntegralDeriviative.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'ResponseToDemandType').merge(ResponseToDemand._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


ProportionalIntegralDeriviative.update_forward_refs()
