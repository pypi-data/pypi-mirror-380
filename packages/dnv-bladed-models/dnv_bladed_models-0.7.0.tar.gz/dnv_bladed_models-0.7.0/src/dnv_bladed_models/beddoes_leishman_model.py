# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


# coding: utf-8

from __future__ import annotations

from abc import ABC

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
from dnv_bladed_models.dynamic_stall import DynamicStall

from .schema_helper import SchemaHelper
from .models_impl import *


class BeddoesLeishmanModel(DynamicStall, ABC):
    r"""
    The common properties for the Beddoes Leishman dynamic stall models.
    
    Attributes
    ----------
    UseKirchoffFlow : bool, default=False
        If true,the normal force coefficient is computed using the dynamic separation position in Kirchoff's equation directly.  If false, the dynamic separation position is used to linearly interpolate between fully separated and fully attached flow. In normal operating conditions this setting will not lead to significant differences, but it has been found that in parked/idling cases (where the blade experiences high angles of attack) this option will improve the aerodynamic damping of the blade. The explanation for the damping differences is given in the aerodynamic validation document on the User Portal.
    
    UseImpulsiveContributions : bool, default=False
        Enabling the impulsive contributions in lift and moment coefficient.
    
    PressureLagTimeConstant : float, default=1.7
        The lag between the pressure and the lift.
    
    VortexLiftTimeConstant : float, default=6
        The rate of decay of the vortex induced lift that is generated when aerofoils undergo a rapid change in angle of attack towards positive or negative stall.
    
    VortexTravelTimeConstant : float, default=7.5
        The time constant that controls the duration of the vortex induced lift that is generated when aerofoils undergo a rapid change in angle of attack towards positive or negative stall.
    
    AttachedFlowConstantA1 : float, default=0.165
        The constant A1 for the Beddoes-Leishman type dynamic stall model to control the attached flow states.
    
    AttachedFlowConstantA2 : float, default=0.335
        The constant A2 for the Beddoes-Leishman type dynamic stall model to control the attached flow states.
    
    AttachedFlowConstantB1 : float, default=0.0455
        The constant B1 for the Beddoes-Leishman type dynamic stall model to control the attached flow states.
    
    AttachedFlowConstantB2 : float, default=0.3
        The constant B2 for the Beddoes-Leishman type dynamic stall model to control the attached flow states.
    
    Notes
    -----
    
    """
    UseKirchoffFlow: bool = Field(alias="UseKirchoffFlow", default=None)
    UseImpulsiveContributions: bool = Field(alias="UseImpulsiveContributions", default=None)
    PressureLagTimeConstant: float = Field(alias="PressureLagTimeConstant", default=None)
    VortexLiftTimeConstant: float = Field(alias="VortexLiftTimeConstant", default=None)
    VortexTravelTimeConstant: float = Field(alias="VortexTravelTimeConstant", default=None)
    AttachedFlowConstantA1: float = Field(alias="AttachedFlowConstantA1", default=None)
    AttachedFlowConstantA2: float = Field(alias="AttachedFlowConstantA2", default=None)
    AttachedFlowConstantB1: float = Field(alias="AttachedFlowConstantB1", default=None)
    AttachedFlowConstantB2: float = Field(alias="AttachedFlowConstantB2", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(DynamicStall._type_info)


BeddoesLeishmanModel.update_forward_refs()
