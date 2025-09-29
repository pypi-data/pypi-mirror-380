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


class TimeVsVoltageChange(BladedModel):
    r"""
    A single point in the time vs voltage time history.
    
    Not supported yet.
    
    Attributes
    ----------
    Time : float, Not supported yet
        The time after the disturbance starts.  The first point in the series should be at Time=0.0.
    
    VoltageChange : float, Not supported yet
        The change in voltage at the corresponding time.  0.0 would represent no disturbance in the voltage.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    Time: float = Field(alias="Time", default=None) # Not supported yet
    VoltageChange: float = Field(alias="VoltageChange", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Event/TimeVsVoltageChange/TimeVsVoltageChange.json'
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


TimeVsVoltageChange.update_forward_refs()
