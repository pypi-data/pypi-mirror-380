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
from dnv_bladed_models.external_controller import ExternalController
from dnv_bladed_models.measured_signal_properties import MeasuredSignalProperties
from dnv_bladed_models.safety_system import SafetySystem

from .schema_helper import SchemaHelper
from .models_impl import *


class BladedControl(BladedModel):
    r"""
    A definition of how the turbine is controlled.
    
    Attributes
    ----------
    SignalProperties : MeasuredSignalProperties, Not supported yet
    
    ControlDiscreteTimeStep : float, default=0.1
        The minimum timestep to be used across all of the controllers.  Controllers do not need to be called on every timestep (see the 'TimeStepMultiplier' parameter, below).
    
    Controllers : List[ExternalController]
        A list of externally-defined controllers.  These will be run in the order they are specified, but can be run at different multiples of the timestep set above.  If no controllers are specified, there will be no control action taken throughout the simulation.  No control demands will be calculated or acted upon, although the rotor speed may well accelerate.  The friction of the pitch systems may also be overcome, resulting in a change in the pitch angles.
    
    SafetySystem : SafetySystem, Not supported yet
    
    Notes
    -----
    
    """
    SignalProperties: MeasuredSignalProperties = Field(alias="SignalProperties", default=None) # Not supported yet
    ControlDiscreteTimeStep: float = Field(alias="ControlDiscreteTimeStep", default=None)
    Controllers: List[ExternalController] = Field(alias="Controllers", default=list())
    SafetySystem: SafetySystem = Field(alias="SafetySystem", default=None) # Not supported yet

    _relative_schema_path = 'Turbine/BladedControl/BladedControl.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['Controllers',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


BladedControl.update_forward_refs()
