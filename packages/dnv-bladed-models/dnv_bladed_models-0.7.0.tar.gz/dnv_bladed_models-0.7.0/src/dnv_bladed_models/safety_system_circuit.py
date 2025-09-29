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


class SafetySystemCircuit(BladedModel):
    r"""
    A safety system circuit, which defines the actions that will be taken if it is triggered.
    
    Not supported yet.
    
    Attributes
    ----------
    PitchAction : bool, Not supported yet
        If true, the pitch system will be asked to activate its own safety system.
    
    ApplyShaftBrake1 : bool, Not supported yet
        If true, the third shaft brake will be activated.
    
    ApplyShaftBrake2 : bool, Not supported yet
        If true, the third shaft brake will be activated.
    
    ApplyShaftBrake3 : bool, Not supported yet
        If true, the third shaft brake will be activated.
    
    DisconnectGenerator : bool, Not supported yet
        If true, the generator will be disconnected from the grid.
    
    ApplyGeneratorBrake : bool, Not supported yet
        If true, the generator brake will be activated.
    
    DisconnectYawDrive : bool, Not supported yet
        If true, the yaw drive will be disconnected.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    PitchAction: bool = Field(alias="PitchAction", default=None) # Not supported yet
    ApplyShaftBrake1: bool = Field(alias="ApplyShaftBrake1", default=None) # Not supported yet
    ApplyShaftBrake2: bool = Field(alias="ApplyShaftBrake2", default=None) # Not supported yet
    ApplyShaftBrake3: bool = Field(alias="ApplyShaftBrake3", default=None) # Not supported yet
    DisconnectGenerator: bool = Field(alias="DisconnectGenerator", default=None) # Not supported yet
    ApplyGeneratorBrake: bool = Field(alias="ApplyGeneratorBrake", default=None) # Not supported yet
    DisconnectYawDrive: bool = Field(alias="DisconnectYawDrive", default=None) # Not supported yet

    _relative_schema_path = 'Turbine/BladedControl/SafetySystem/SafetyCircuitLibrary/SafetySystemCircuit/SafetySystemCircuit.json'
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


SafetySystemCircuit.update_forward_refs()
