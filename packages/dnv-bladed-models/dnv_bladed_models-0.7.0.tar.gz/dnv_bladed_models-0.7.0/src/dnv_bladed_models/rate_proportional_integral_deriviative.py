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
from dnv_bladed_models.transducer_behaviour import TransducerBehaviour
class RateProportionalIntegralDeriviative_DifferentialGainActionEnum(str, Enum):
    ERROR = "Error"
    FEEDBACK = "Feedback"
    SETPOINT = "Setpoint"

from .schema_helper import SchemaHelper
from .models_impl import *


class RateProportionalIntegralDeriviative(TransducerBehaviour):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    TransducerBehaviourType : Literal['RateProportionalIntegralDeriviative'], default='RateProportionalIntegralDeriviative', Not supported yet
        Defines the specific type of TransducerBehaviour model in use.  For a `RateProportionalIntegralDeriviative` object, this must always be set to a value of `RateProportionalIntegralDeriviative`.
    
    ProportionalGain : float, default=0, Not supported yet
        The gain on the contemporaneous error.
    
    IntegralGain : float, default=0, Not supported yet
        The gain on the integral from time zero till the present of the error signal.
    
    DifferentialGain : float, default=0, Not supported yet
        The gain the filtered derivative of the error. The derivative of the error is passed through a low-pass filter.
    
    DifferentialGainAction : RateProportionalIntegralDeriviative_DifferentialGainActionEnum, default='Feedback', Not supported yet
        Proportional and integral terms are applied on error.  The derivative term may also be applied on the feedback or setpoint signals.
    
    DifferentialGainTimeConstant : float, default=0, Not supported yet
        The derivative term uses a low-pass filter on input.
    
    DesaturationTimeConstant : float, default=0, Not supported yet
        The time constant for when the output exceeds the limits.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    TransducerBehaviourType: Literal['RateProportionalIntegralDeriviative'] = Field(alias="TransducerBehaviourType", default='RateProportionalIntegralDeriviative', allow_mutation=False, const=True) # Not supported yet # type: ignore
    ProportionalGain: float = Field(alias="ProportionalGain", default=None) # Not supported yet
    IntegralGain: float = Field(alias="IntegralGain", default=None) # Not supported yet
    DifferentialGain: float = Field(alias="DifferentialGain", default=None) # Not supported yet
    DifferentialGainAction: RateProportionalIntegralDeriviative_DifferentialGainActionEnum = Field(alias="DifferentialGainAction", default=None) # Not supported yet
    DifferentialGainTimeConstant: float = Field(alias="DifferentialGainTimeConstant", default=None) # Not supported yet
    DesaturationTimeConstant: float = Field(alias="DesaturationTimeConstant", default=None) # Not supported yet

    _relative_schema_path = 'Turbine/BladedControl/MeasuredSignalProperties/common/RateProportionalIntegralDeriviative.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'TransducerBehaviourType').merge(TransducerBehaviour._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


RateProportionalIntegralDeriviative.update_forward_refs()
