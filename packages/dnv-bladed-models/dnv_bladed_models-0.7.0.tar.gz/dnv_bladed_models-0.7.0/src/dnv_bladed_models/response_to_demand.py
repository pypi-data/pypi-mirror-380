# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


# coding: utf-8

from __future__ import annotations

from abc import ABC

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
from dnv_bladed_models.pitch_acceleration_limits import PitchAccelerationLimits
from dnv_bladed_models.pitch_rate_limits import PitchRateLimits
class ResponseToDemand_ResponseToDemandTypeEnum(str, Enum):
    FIRST_ORDER_RESPONSE = "FirstOrderResponse"
    IMMEDIATE_RESPONSE = "ImmediateResponse"
    PROPORTIONAL_INTEGRAL_DERIVIATIVE = "ProportionalIntegralDeriviative"
    SECOND_ORDER_RESPONSE = "SecondOrderResponse"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class ResponseToDemand(BladedModel, ABC):
    r"""
    The common properties of all control responses.
    
    Attributes
    ----------
    ResponseToDemandType : ResponseToDemand_ResponseToDemandTypeEnum
        Defines the specific type of model in use.
    
    RateLimits : PitchRateLimits
    
    AccelerationLimits : PitchAccelerationLimits
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - FirstOrderResponse
        - ImmediateResponse
        - ResponseToDemandInsert
        - ProportionalIntegralDeriviative
        - SecondOrderResponse
    
    """
    ResponseToDemandType: ResponseToDemand_ResponseToDemandTypeEnum = Field(alias="ResponseToDemandType", default=None)
    RateLimits: PitchRateLimits = Field(alias="RateLimits", default=None)
    AccelerationLimits: PitchAccelerationLimits = Field(alias="AccelerationLimits", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


ResponseToDemand.update_forward_refs()
