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

from .schema_helper import SchemaHelper
from .models_impl import *


class Earthquake(BladedModel):
    r"""
    The definition of a seismic event, or earthquake.
    
    Not supported yet.
    
    Attributes
    ----------
    QuakeFilepath : str, Not supported yet
        The filepath or URI providing a time history of the earthquake accelerations.
    
    StartTime : float, Not supported yet
        The time into the simulation at which the earthquake begins (excluding the lead-in time).
    
    DirectionClockwiseFromNorth : float, Not supported yet
        The angle to the global x-axis that the accelerations in the file will be applied in.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    QuakeFilepath: str = Field(alias="QuakeFilepath", default=None) # Not supported yet
    StartTime: float = Field(alias="StartTime", default=None) # Not supported yet
    DirectionClockwiseFromNorth: float = Field(alias="DirectionClockwiseFromNorth", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/Earthquake/Earthquake.json'
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


Earthquake.update_forward_refs()
