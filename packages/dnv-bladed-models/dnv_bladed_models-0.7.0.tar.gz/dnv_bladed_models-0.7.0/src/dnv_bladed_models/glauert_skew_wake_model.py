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
from dnv_bladed_models.skew_wake_model import SkewWakeModel

from .schema_helper import SchemaHelper
from .models_impl import *


class GlauertSkewWakeModel(SkewWakeModel):
    r"""
    Settings for the Glauert skew wake model.
    
    Attributes
    ----------
    VelocityCorrectionFactor : float, default=0.75
        The correction factor for quasi-steady velocity in Glauert skew wake model.
    
    TimeCorrectionFactor : float, default=0.5
        The correction factor for time constant in Glauert skew wake model.
    
    Notes
    -----
    
    """
    VelocityCorrectionFactor: float = Field(alias="VelocityCorrectionFactor", default=None)
    TimeCorrectionFactor: float = Field(alias="TimeCorrectionFactor", default=None)

    _relative_schema_path = 'Settings/AerodynamicSettings/AerodynamicModel/MomentumTheoryCorrections/GlauertSkewWakeModel/GlauertSkewWakeModel.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(SkewWakeModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


GlauertSkewWakeModel.update_forward_refs()
