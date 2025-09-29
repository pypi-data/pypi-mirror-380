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
from dnv_bladed_models.dynamic_wake import DynamicWake

from .schema_helper import SchemaHelper
from .models_impl import *


class OyeDynamicWake(DynamicWake):
    r"""
    The Oye dynamic wake model captures the lag in induction in response to a change of inflow conditions.  It is the most accurate model for linearisation and time domain, but it does increase linearisation time significantly as it introduces extra states.
    
    Attributes
    ----------
    DynamicWakeType : Literal['OyeDynamicWake'], default='OyeDynamicWake'
        Defines the specific type of DynamicWake model in use.  For a `OyeDynamicWake` object, this must always be set to a value of `OyeDynamicWake`.
    
    DynamicTangentialInduction : bool, default=True
        If false, the tangential induction will be solved by iteration on each time step, as per the Pitt and Peters model.
    
    OyeTimeLagMultiplier : float, default=1
        The time constant for the Oye dynamic wake model.
    
    Notes
    -----
    
    """
    DynamicWakeType: Literal['OyeDynamicWake'] = Field(alias="DynamicWakeType", default='OyeDynamicWake', allow_mutation=False, const=True) # type: ignore
    DynamicTangentialInduction: bool = Field(alias="DynamicTangentialInduction", default=None)
    OyeTimeLagMultiplier: float = Field(alias="OyeTimeLagMultiplier", default=None)

    _relative_schema_path = 'Settings/AerodynamicSettings/AerodynamicModel/MomentumTheoryCorrections/DynamicWake/OyeDynamicWake.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'DynamicWakeType').merge(DynamicWake._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


OyeDynamicWake.update_forward_refs()
