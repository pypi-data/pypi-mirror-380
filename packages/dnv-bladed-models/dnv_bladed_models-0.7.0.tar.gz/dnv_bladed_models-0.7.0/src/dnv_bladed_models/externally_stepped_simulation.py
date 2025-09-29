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
from dnv_bladed_models.hardware_tracking import HardwareTracking

from .schema_helper import SchemaHelper
from .models_impl import *


class ExternallySteppedSimulation(BladedModel):
    r"""
    The definition of a Bladed real time simulation.  This will be run with Bladed as an external library (i.e. a dynamic link library (dll) on Windows, or a shared object (so) on Linux).  An external process must call functions within the Bladed external library to \"step\" the simulation, and thereby keep it synchronised with the external controlling process.
    
    Not supported yet.
    
    Attributes
    ----------
    TimeStep : float, Not supported yet
        The real time simulation time step, as set by the external process that is calling Bladed in real time mode.
    
    TimeStepMultiplier : float, Not supported yet
        The real time simulation time step multiplier.
    
    HardwareTracking : HardwareTracking, Not supported yet
    
    OutputRealTimeDataFromStart : bool, Not supported yet
        If true, realtime data will be output as soon as Bladed is running.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    TimeStep: float = Field(alias="TimeStep", default=None) # Not supported yet
    TimeStepMultiplier: float = Field(alias="TimeStepMultiplier", default=None) # Not supported yet
    HardwareTracking: HardwareTracking = Field(alias="HardwareTracking", default=None) # Not supported yet
    OutputRealTimeDataFromStart: bool = Field(alias="OutputRealTimeDataFromStart", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/ExternallySteppedSimulation/ExternallySteppedSimulation.json'
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


ExternallySteppedSimulation.update_forward_refs()
