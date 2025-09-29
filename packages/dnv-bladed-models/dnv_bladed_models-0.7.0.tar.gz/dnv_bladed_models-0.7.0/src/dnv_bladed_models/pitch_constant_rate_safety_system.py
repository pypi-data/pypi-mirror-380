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

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchConstantRateSafetySystem(PitchControllerRateSafetySystem):
    r"""
    A safety system where the pitch system will seek to move at a constant rate once the safety system has been triggered.
    
    Attributes
    ----------
    PitchSafetySystemType : Literal['ConstantRate'], default='ConstantRate'
        Defines the specific type of PitchSafetySystem model in use.  For a `ConstantRate` object, this must always be set to a value of `ConstantRate`.
    
    Rate : float, default=0
        The constant rate at which the pitch controller will move the pitch system once the safety system has been triggered.
    
    Notes
    -----
    
    """
    PitchSafetySystemType: Literal['ConstantRate'] = Field(alias="PitchSafetySystemType", default='ConstantRate', allow_mutation=False, const=True) # type: ignore
    Rate: float = Field(alias="Rate", default=None)

    _relative_schema_path = 'Components/PitchSystem/PitchController/PitchSafetySystem/PitchConstantRateSafetySystem.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'PitchSafetySystemType').merge(PitchControllerRateSafetySystem._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchConstantRateSafetySystem.update_forward_refs()
