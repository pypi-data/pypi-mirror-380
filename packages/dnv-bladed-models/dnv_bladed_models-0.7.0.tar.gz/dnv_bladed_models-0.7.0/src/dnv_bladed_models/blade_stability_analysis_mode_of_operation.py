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
from dnv_bladed_models.velocity_range import VelocityRange
class BladeStabilityAnalysisModeOfOperation_BladeStabilityAnalysisModeOfOperationTypeEnum(str, Enum):
    IDLING = "Idling"
    PARKED = "Parked"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class BladeStabilityAnalysisModeOfOperation(BladedModel, ABC):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    BladeStabilityAnalysisModeOfOperationType : BladeStabilityAnalysisModeOfOperation_BladeStabilityAnalysisModeOfOperationTypeEnum, Not supported yet
        Defines the specific type of model in use.
    
    PitchAngle : float, default=0, Not supported yet
        The constant pitch angle used in both parked and free spin case.  This value is only used for blade stability analysis and not for model linearisation or Campbell diagram.  Blade set angle or pitch angle imbalances are ignored, and any pitch limits are not used.
    
    WindSpeedRange : VelocityRange
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    This class is an abstraction, with the following concrete implementations:
        - BladeStabilityAnalysisIdling
        - BladeStabilityAnalysisModeOfOperationInsert
        - BladeStabilityAnalysisParked
    
    """
    BladeStabilityAnalysisModeOfOperationType: BladeStabilityAnalysisModeOfOperation_BladeStabilityAnalysisModeOfOperationTypeEnum = Field(alias="BladeStabilityAnalysisModeOfOperationType", default=None) # Not supported yet
    PitchAngle: float = Field(alias="PitchAngle", default=None) # Not supported yet
    WindSpeedRange: VelocityRange = Field(alias="WindSpeedRange", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


BladeStabilityAnalysisModeOfOperation.update_forward_refs()
