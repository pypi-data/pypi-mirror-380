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
from dnv_bladed_models.emergency_stop_button import EmergencyStopButton
from dnv_bladed_models.generator_overpower import GeneratorOverpower
from dnv_bladed_models.generator_overspeed import GeneratorOverspeed
from dnv_bladed_models.generator_short_circuit import GeneratorShortCircuit
from dnv_bladed_models.nacelle_vibration import NacelleVibration
from dnv_bladed_models.rotor_overspeed import RotorOverspeed
from dnv_bladed_models.safety_circuit_library import SafetyCircuitLibrary

from .schema_helper import SchemaHelper
from .models_impl import *


class SafetySystem(BladedModel):
    r"""
    The definition of the turbine's safety system.  This supersedes the turbine's controller requests.
    
    Not supported yet.
    
    Attributes
    ----------
    SafetyCircuitLibrary : SafetyCircuitLibrary, Not supported yet
    
    GeneratorOverspeed : GeneratorOverspeed, Not supported yet
    
    RotorOverspeed : RotorOverspeed, Not supported yet
    
    GeneratorOverpower : GeneratorOverpower, Not supported yet
    
    NacelleVibration : NacelleVibration, Not supported yet
    
    GeneratorShortCircuit : GeneratorShortCircuit, Not supported yet
    
    EmergencyStopButton : EmergencyStopButton, Not supported yet
    
    OnlyActivateOnceLoggingHasCommenced : bool, Not supported yet
        If true, the safety system will be inactivated during the lead in time when there is no logging.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    SafetyCircuitLibrary: SafetyCircuitLibrary = Field(alias="SafetyCircuitLibrary", default=SafetyCircuitLibrary()) # Not supported yet
    GeneratorOverspeed: GeneratorOverspeed = Field(alias="GeneratorOverspeed", default=None) # Not supported yet
    RotorOverspeed: RotorOverspeed = Field(alias="RotorOverspeed", default=None) # Not supported yet
    GeneratorOverpower: GeneratorOverpower = Field(alias="GeneratorOverpower", default=None) # Not supported yet
    NacelleVibration: NacelleVibration = Field(alias="NacelleVibration", default=None) # Not supported yet
    GeneratorShortCircuit: GeneratorShortCircuit = Field(alias="GeneratorShortCircuit", default=None) # Not supported yet
    EmergencyStopButton: EmergencyStopButton = Field(alias="EmergencyStopButton", default=None) # Not supported yet
    OnlyActivateOnceLoggingHasCommenced: bool = Field(alias="OnlyActivateOnceLoggingHasCommenced", default=None) # Not supported yet

    _relative_schema_path = 'Turbine/BladedControl/SafetySystem/SafetySystem.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['SafetyCircuitLibrary',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


SafetySystem.update_forward_refs()
