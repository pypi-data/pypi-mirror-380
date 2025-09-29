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
from dnv_bladed_models.generator_speed_vs_generator_torque import GeneratorSpeedVsGeneratorTorque

from .schema_helper import SchemaHelper
from .models_impl import *


class PartialLoadOperation(BladedModel):
    r"""
    The general parameters of the torque control strategy while the turbine is operating at less than its rated power.  These are used to determine steady-state conditions, such as the initial conditions for a time-domain simulation.
    
    Attributes
    ----------
    OptimalModeGain : float
        The ratio between the generator torque demand and the square of the measured generator speed.
    
    MinimumGeneratorSpeed : float
        The minimum speed at which the generator will be producing power and thus apply a generator torque.
    
    GeneratorSpeedVsGeneratorTorque : List[GeneratorSpeedVsGeneratorTorque]
        A look-up table of the generator torque demand vs the measured generator speed. The table must extend up to FullLoadOperation.GeneratorSpeed which is the range Bladed will use.
    
    Notes
    -----
    
    """
    OptimalModeGain: float = Field(alias="OptimalModeGain", default=None)
    MinimumGeneratorSpeed: float = Field(alias="MinimumGeneratorSpeed", default=None)
    GeneratorSpeedVsGeneratorTorque: List[GeneratorSpeedVsGeneratorTorque] = Field(alias="GeneratorSpeedVsGeneratorTorque", default=list())

    _relative_schema_path = 'Turbine/TurbineOperationalParameters/VariableSpeedPitchRegulatedControlModel/PartialLoadOperation/PartialLoadOperation.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['GeneratorSpeedVsGeneratorTorque',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PartialLoadOperation.update_forward_refs()
