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
from dnv_bladed_models.pitch_safety_limit_switches import PitchSafetyLimitSwitches
from dnv_bladed_models.standard_pitch_limit_switches import StandardPitchLimitSwitches

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchLimitSwitches(BladedModel):
    r"""
    The definition of the limit switches for the standard control system and the safety system.
    
    Attributes
    ----------
    Safety : PitchSafetyLimitSwitches
    
    Standard : StandardPitchLimitSwitches
    
    Notes
    -----
    
    """
    Safety: PitchSafetyLimitSwitches = Field(alias="Safety", default=None)
    Standard: StandardPitchLimitSwitches = Field(alias="Standard", default=None)

    _relative_schema_path = 'Components/PitchSystem/PitchLimitSwitches/PitchLimitSwitches.json'
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


PitchLimitSwitches.update_forward_refs()
