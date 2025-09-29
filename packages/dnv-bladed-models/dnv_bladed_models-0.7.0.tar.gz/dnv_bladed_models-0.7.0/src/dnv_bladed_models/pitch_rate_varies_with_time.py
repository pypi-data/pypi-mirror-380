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
from dnv_bladed_models.rate_vs_time import RateVsTime

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchRateVariesWithTime(PitchControllerRateSafetySystem):
    r"""
    A safety system where the pitch system will adjust its rate dependent on the time after which the safety system has been triggered.
    
    Attributes
    ----------
    PitchSafetySystemType : Literal['RateVariesWithTime'], default='RateVariesWithTime'
        Defines the specific type of PitchSafetySystem model in use.  For a `RateVariesWithTime` object, this must always be set to a value of `RateVariesWithTime`.
    
    TimeVsRate : List[RateVsTime]
        A look-up table of the rate versus the time after the safety system has been triggered.
    
    Notes
    -----
    
    """
    PitchSafetySystemType: Literal['RateVariesWithTime'] = Field(alias="PitchSafetySystemType", default='RateVariesWithTime', allow_mutation=False, const=True) # type: ignore
    TimeVsRate: List[RateVsTime] = Field(alias="TimeVsRate", default=list())

    _relative_schema_path = 'Components/PitchSystem/PitchController/PitchSafetySystem/PitchRateVariesWithTime.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['TimeVsRate',]),
        'PitchSafetySystemType').merge(PitchControllerRateSafetySystem._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchRateVariesWithTime.update_forward_refs()
