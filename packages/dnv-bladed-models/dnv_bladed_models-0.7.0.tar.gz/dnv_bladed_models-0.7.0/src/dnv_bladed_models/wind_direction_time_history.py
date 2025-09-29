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
from dnv_bladed_models.time_vs_wind_direction import TimeVsWindDirection
from dnv_bladed_models.wind_direction_variation import WindDirectionVariation

from .schema_helper import SchemaHelper
from .models_impl import *


class WindDirectionTimeHistory(WindDirectionVariation):
    r"""
    A time history of the wind direction.
    
    Attributes
    ----------
    DirectionVariationType : Literal['TimeHistory'], default='TimeHistory'
        Defines the specific type of DirectionVariation model in use.  For a `TimeHistory` object, this must always be set to a value of `TimeHistory`.
    
    TimeVsDirection : List[TimeVsWindDirection]
        A list of points specifying the direction at the corresponding time.  The direction will be interpolated between these points; the direction before the first point will be constant at the first point's value; and the direction after the last point will remain constant at the last point's value
    
    Notes
    -----
    
    """
    DirectionVariationType: Literal['TimeHistory'] = Field(alias="DirectionVariationType", default='TimeHistory', allow_mutation=False, const=True) # type: ignore
    TimeVsDirection: List[TimeVsWindDirection] = Field(alias="TimeVsDirection", default=list())

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/WindDirectionVariation/WindDirectionTimeHistory.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['TimeVsDirection',]),
        'DirectionVariationType').merge(WindDirectionVariation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


WindDirectionTimeHistory.update_forward_refs()
