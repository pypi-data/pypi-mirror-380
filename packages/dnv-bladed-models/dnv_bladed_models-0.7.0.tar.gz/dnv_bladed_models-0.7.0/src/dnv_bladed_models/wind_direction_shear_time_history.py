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
from dnv_bladed_models.time_vs_wind_direction_shear import TimeVsWindDirectionShear
from dnv_bladed_models.wind_direction_shear_variation import WindDirectionShearVariation

from .schema_helper import SchemaHelper
from .models_impl import *


class WindDirectionShearTimeHistory(WindDirectionShearVariation):
    r"""
    A time history of the vertical direction shear (veer).  This is a linear relationship between the height and the local direction, with the direction being its nominal value at the reference height.
    
    Attributes
    ----------
    DirectionShearVariationType : Literal['TimeHistory'], default='TimeHistory'
        Defines the specific type of DirectionShearVariation model in use.  For a `TimeHistory` object, this must always be set to a value of `TimeHistory`.
    
    TimeVsDirectionShear : List[TimeVsWindDirectionShear]
        A list of points specifying the wind veer at the corresponding time.  The wind veer will be interpolated between these points; the wind veer before the first point will be constant at the first point's value; and the wind veer after the last point will remain constant at the last point's value
    
    Notes
    -----
    
    """
    DirectionShearVariationType: Literal['TimeHistory'] = Field(alias="DirectionShearVariationType", default='TimeHistory', allow_mutation=False, const=True) # type: ignore
    TimeVsDirectionShear: List[TimeVsWindDirectionShear] = Field(alias="TimeVsDirectionShear", default=list())

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/WindDirectionShearVariation/WindDirectionShearTimeHistory.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['TimeVsDirectionShear',]),
        'DirectionShearVariationType').merge(WindDirectionShearVariation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


WindDirectionShearTimeHistory.update_forward_refs()
