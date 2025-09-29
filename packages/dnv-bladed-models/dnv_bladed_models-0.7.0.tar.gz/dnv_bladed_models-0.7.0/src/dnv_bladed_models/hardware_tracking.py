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


class HardwareTracking(BladedModel):
    r"""
    Options for tracking external hardware using BHTM (Bladed Hardware Test Module) or similar external package.
    
    Not supported yet.
    
    Attributes
    ----------
    TrackPitchActuator : bool, default=False, Not supported yet
        If true, Bladed will accept data about the pitch system from an external source, and simulate the rest of the turbine in Bladed.
    
    TrackGenerator : bool, Not supported yet
        If true, Bladed will accept data about the generator from an external source, and simulate the rest of the turbine in Bladed.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    TrackPitchActuator: bool = Field(alias="TrackPitchActuator", default=None) # Not supported yet
    TrackGenerator: bool = Field(alias="TrackGenerator", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/ExternallySteppedSimulation/HardwareTracking/HardwareTracking.json'
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


HardwareTracking.update_forward_refs()
