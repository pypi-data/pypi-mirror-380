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


class PitchPositionVsMinimumAndMaximumMoment(BladedModel):
    r"""
    The limits on the torque of the rotary drive as they vary with position.
    
    Attributes
    ----------
    Position : float, default=0
        The position at which the maximum and minimum are applicable for.
    
    Minimum : float, default=0
        The minimum torque of the rotary drive.
    
    Maximum : float, default=0
        The maximum torque of the rotary drive.
    
    Notes
    -----
    
    """
    Position: float = Field(alias="Position", default=None)
    Minimum: float = Field(alias="Minimum", default=None)
    Maximum: float = Field(alias="Maximum", default=None)

    _relative_schema_path = 'Components/PitchSystem/PitchActuator/common/PitchPositionVsMinimumAndMaximumMoment.json'
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


PitchPositionVsMinimumAndMaximumMoment.update_forward_refs()
