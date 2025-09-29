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
from dnv_bladed_models.air_characteristics import AirCharacteristics
from dnv_bladed_models.bladed_model import BladedModel
from dnv_bladed_models.water_characteristics import WaterCharacteristics

from .schema_helper import SchemaHelper
from .models_impl import *


class Constants(BladedModel):
    r"""
    The physical constants used in the analysis.  The default values are assumed if not provided explicitly.
    
    Attributes
    ----------
    AccelerationDueToGravity : float, default=9.81, >= 0
        The acceleration due to gravity known as g
    
    AirCharacteristics : AirCharacteristics
    
    WaterCharacteristics : WaterCharacteristics, Not supported yet
    
    Notes
    -----
    
    """
    AccelerationDueToGravity: float = Field(alias="AccelerationDueToGravity", default=None, ge=0)
    AirCharacteristics: AirCharacteristics = Field(alias="AirCharacteristics", default=None)
    WaterCharacteristics: WaterCharacteristics = Field(alias="WaterCharacteristics", default=None) # Not supported yet

    _relative_schema_path = 'Constants/Constants.json'
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


Constants.update_forward_refs()
