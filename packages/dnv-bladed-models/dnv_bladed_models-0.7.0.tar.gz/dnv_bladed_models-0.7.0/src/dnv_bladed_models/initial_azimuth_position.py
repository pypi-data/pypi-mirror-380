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
from dnv_bladed_models.initial_position import InitialPosition

from .schema_helper import SchemaHelper
from .models_impl import *


class InitialAzimuthPosition(InitialPosition):
    r"""
    The initial position of a rotor.  If there is only one rotor, then AssemblyReference can be omitted.
    
    Attributes
    ----------
    InitialConditionType : Literal['InitialAzimuthPosition'], default='InitialAzimuthPosition'
        Defines the specific type of InitialCondition model in use.  For a `InitialAzimuthPosition` object, this must always be set to a value of `InitialAzimuthPosition`.
    
    AngleOfFirstBladeToVertical : float
        The starting azimuth angle of the specified rotor or turbine.
    
    Notes
    -----
    
    """
    InitialConditionType: Literal['InitialAzimuthPosition'] = Field(alias="InitialConditionType", default='InitialAzimuthPosition', allow_mutation=False, const=True) # type: ignore
    AngleOfFirstBladeToVertical: float = Field(alias="AngleOfFirstBladeToVertical", default=None)

    _relative_schema_path = 'TimeDomainSimulation/InitialCondition/InitialAzimuthPosition.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'InitialConditionType').merge(InitialPosition._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


InitialAzimuthPosition.update_forward_refs()
