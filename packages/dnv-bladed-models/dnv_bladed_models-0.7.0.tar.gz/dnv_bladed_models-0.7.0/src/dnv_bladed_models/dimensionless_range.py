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
from dnv_bladed_models.bladed_model import BladedModel

from .schema_helper import SchemaHelper
from .models_impl import *


class DimensionlessRange(BladedModel):
    r"""
    The range of tip speed ratios to consider.
    
    Attributes
    ----------
    Minimum : float
        The lowest tip speed ratio to consider.
    
    Maximum : float
        The highest tip speed ratio to consider.
    
    Interval : float
        The step size to take from the lowest to the highest tip speed ratio.
    
    Notes
    -----
    
    """
    Minimum: float = Field(alias="Minimum", default=None)
    Maximum: float = Field(alias="Maximum", default=None)
    Interval: float = Field(alias="Interval", default=None)

    _relative_schema_path = 'SteadyCalculation/DimensionlessRange/DimensionlessRange.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


DimensionlessRange.update_forward_refs()
