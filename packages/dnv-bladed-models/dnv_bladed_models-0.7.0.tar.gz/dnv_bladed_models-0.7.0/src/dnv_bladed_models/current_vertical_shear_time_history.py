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
from dnv_bladed_models.current_vertical_shear_variation import CurrentVerticalShearVariation
from dnv_bladed_models.time_vs_current_vertical_shear import TimeVsCurrentVerticalShear

from .schema_helper import SchemaHelper
from .models_impl import *


class CurrentVerticalShearTimeHistory(CurrentVerticalShearVariation):
    r"""
    A time history of the current 's vertical shear.
    
    Not supported yet.
    
    Attributes
    ----------
    VerticalShearVariationType : Literal['TimeHistory'], default='TimeHistory', Not supported yet
        Defines the specific type of VerticalShearVariation model in use.  For a `TimeHistory` object, this must always be set to a value of `TimeHistory`.
    
    TimeVsVerticalShear : List[TimeVsCurrentVerticalShear], Not supported yet
        A list of points specifying the current's shear at the corresponding time.  The shear will be interpolated between these points; the shear before the first point will be constant at the first point's value; and the shear after the last point will remain constant at the last point's value
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    VerticalShearVariationType: Literal['TimeHistory'] = Field(alias="VerticalShearVariationType", default='TimeHistory', allow_mutation=False, const=True) # Not supported yet # type: ignore
    TimeVsVerticalShear: List[TimeVsCurrentVerticalShear] = Field(alias="TimeVsVerticalShear", default=list()) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Current/CurrentVerticalShearVariation/CurrentVerticalShearTimeHistory.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['TimeVsVerticalShear',]),
        'VerticalShearVariationType').merge(CurrentVerticalShearVariation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


CurrentVerticalShearTimeHistory.update_forward_refs()
