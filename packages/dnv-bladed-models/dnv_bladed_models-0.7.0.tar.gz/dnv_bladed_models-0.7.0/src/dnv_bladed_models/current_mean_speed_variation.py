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
class CurrentMeanSpeedVariation_MeanSpeedVariationTypeEnum(str, Enum):
    PRESET_TRANSIENT = "PresetTransient"
    TIME_HISTORY = "TimeHistory"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class CurrentMeanSpeedVariation(BladedModel, ABC):
    r"""
    A defined variation in the current's mean speed.
    
    Not supported yet.
    
    Attributes
    ----------
    MeanSpeedVariationType : CurrentMeanSpeedVariation_MeanSpeedVariationTypeEnum, Not supported yet
        Defines the specific type of model in use.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    This class is an abstraction, with the following concrete implementations:
        - CurrentMeanSpeedVariationInsert
        - PresetCurrentMeanSpeedTransient
        - CurrentMeanSpeedTimeHistory
    
    """
    MeanSpeedVariationType: CurrentMeanSpeedVariation_MeanSpeedVariationTypeEnum = Field(alias="MeanSpeedVariationType", default=None) # Not supported yet

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


CurrentMeanSpeedVariation.update_forward_refs()
