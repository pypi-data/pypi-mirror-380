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
class WindDirectionShearVariation_DirectionShearVariationTypeEnum(str, Enum):
    PRESET_TRANSIENT = "PresetTransient"
    TIME_HISTORY = "TimeHistory"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class WindDirectionShearVariation(BladedModel, ABC):
    r"""
    A defined variation in the direction wind shear.  This is a linear relationship between the height and the local direction, with the direction being its nominal value at the reference height.
    
    Attributes
    ----------
    DirectionShearVariationType : WindDirectionShearVariation_DirectionShearVariationTypeEnum
        Defines the specific type of model in use.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - WindDirectionShearVariationInsert
        - PresetWindDirectionShearTransient
        - WindDirectionShearTimeHistory
    
    """
    DirectionShearVariationType: WindDirectionShearVariation_DirectionShearVariationTypeEnum = Field(alias="DirectionShearVariationType", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


WindDirectionShearVariation.update_forward_refs()
