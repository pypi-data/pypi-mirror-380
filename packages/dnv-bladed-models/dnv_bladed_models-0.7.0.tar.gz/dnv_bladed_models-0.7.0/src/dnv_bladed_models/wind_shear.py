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
class WindShear_WindShearTypeEnum(str, Enum):
    EXPONENTIAL_SHEAR_MODEL = "ExponentialShearModel"
    LOGARITHMIC_SHEAR_MODEL = "LogarithmicShearModel"
    LOOK_UP_SHEAR_MODEL = "LookUpShearModel"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class WindShear(BladedModel, ABC):
    r"""
    The vertical wind shear to apply to the wind field.  This will vary according to the wind shear model selected.
    
    Attributes
    ----------
    WindShearType : WindShear_WindShearTypeEnum
        Defines the specific type of model in use.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - ExponentialShearModel
        - WindShearInsert
        - LogarithmicShearModel
        - LookUpShearModel
    
    """
    WindShearType: WindShear_WindShearTypeEnum = Field(alias="WindShearType", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


WindShear.update_forward_refs()
