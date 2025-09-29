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
from dnv_bladed_models.pitch_controller_rate_safety_system import PitchControllerRateSafetySystem
from dnv_bladed_models.rate_vs_position import RateVsPosition

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchRateVariesWithPosition(PitchControllerRateSafetySystem):
    r"""
    A safety system where the pitch system will adjust its rate dependent on the position of the bearing once the safety system has been triggered.
    
    Attributes
    ----------
    PitchSafetySystemType : Literal['RateVariesWithPosition'], default='RateVariesWithPosition'
        Defines the specific type of PitchSafetySystem model in use.  For a `RateVariesWithPosition` object, this must always be set to a value of `RateVariesWithPosition`.
    
    PositionVsRate : List[RateVsPosition]
        A look-up table of the rate versus the position of the bearing.
    
    Notes
    -----
    
    """
    PitchSafetySystemType: Literal['RateVariesWithPosition'] = Field(alias="PitchSafetySystemType", default='RateVariesWithPosition', allow_mutation=False, const=True) # type: ignore
    PositionVsRate: List[RateVsPosition] = Field(alias="PositionVsRate", default=list())

    _relative_schema_path = 'Components/PitchSystem/PitchController/PitchSafetySystem/PitchRateVariesWithPosition.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['PositionVsRate',]),
        'PitchSafetySystemType').merge(PitchControllerRateSafetySystem._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchRateVariesWithPosition.update_forward_refs()
