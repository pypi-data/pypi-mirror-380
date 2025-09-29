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
from dnv_bladed_models.bladed_model import BladedModel
class Component_ComponentTypeEnum(str, Enum):
    BLADE = "Blade"
    DRIVETRAIN_AND_NACELLE = "DrivetrainAndNacelle"
    EXTERNAL_MODULE_COMPONENT = "ExternalModuleComponent"
    FIXED_SPEED_ACTIVE_DAMPER = "FixedSpeedActiveDamper"
    FLEXIBILITY = "Flexibility"
    INDEPENDENT_PITCH_HUB = "IndependentPitchHub"
    LIDAR = "Lidar"
    LINEAR_PASSIVE_DAMPER = "LinearPassiveDamper"
    PENDULUM_DAMPER = "PendulumDamper"
    PITCH_SYSTEM = "PitchSystem"
    RIGID_BODY_POINT_INERTIA = "RigidBodyPointInertia"
    RIGID_BODY_SIXBY_SIX_INERTIA = "RigidBodySixbySixInertia"
    ROTATION = "Rotation"
    SUPERELEMENT = "Superelement"
    TOWER = "Tower"
    TRANSLATION = "Translation"
    VARIABLE_SPEED_ACTIVE_DAMPER = "VariableSpeedActiveDamper"
    VARIABLE_SPEED_GENERATOR = "VariableSpeedGenerator"
    YAW_SYSTEM = "YawSystem"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class Component(BladedModel, ABC):
    r"""
    The common properties of all components.
    
    Attributes
    ----------
    ComponentType : Component_ComponentTypeEnum
        Defines the specific type of model in use.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - Blade
        - DrivetrainAndNacelle
        - ExternalModuleComponent
        - FixedSpeedActiveDamper
        - Flexibility
        - IndependentPitchHub
        - ComponentInsert
        - Lidar
        - LinearPassiveDamper
        - PendulumDamper
        - PitchSystem
        - RigidBodyPointInertia
        - RigidBodySixbySixInertia
        - Rotation
        - Superelement
        - Tower
        - Translation
        - VariableSpeedActiveDamper
        - VariableSpeedGenerator
        - YawSystem
    
    """
    ComponentType: Component_ComponentTypeEnum = Field(alias="ComponentType", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


Component.update_forward_refs()
