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
from dnv_bladed_models.damper_force_or_torque_vs_rate import DamperForceOrTorqueVsRate
from dnv_bladed_models.pitch_controller_torque_safety_system import PitchControllerTorqueSafetySystem
from dnv_bladed_models.spring_force_or_torque_vs_position import SpringForceOrTorqueVsPosition

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchActuationLimited(PitchControllerTorqueSafetySystem):
    r"""
    A safety system where the movement is limited by the available torque.
    
    Attributes
    ----------
    PitchSafetySystemType : Literal['ActuationLimited'], default='ActuationLimited'
        Defines the specific type of PitchSafetySystem model in use.  For a `ActuationLimited` object, this must always be set to a value of `ActuationLimited`.
    
    AppliedForceOrTorque : float, default=0
        The constant actuator torque (for a rotary system) or linear force (for a linear syste) applied during safety system pitch action.
    
    SpringForceOrTorqueVsPosition : List[SpringForceOrTorqueVsPosition]
        A look-up of the torque or force applied by a spring in the safety system at a given position.
    
    DamperForceOrTorqueVsRate : List[DamperForceOrTorqueVsRate]
        A look-up of the torque or force applied by a damper in the safety system for a given rate.
    
    Notes
    -----
    
    """
    PitchSafetySystemType: Literal['ActuationLimited'] = Field(alias="PitchSafetySystemType", default='ActuationLimited', allow_mutation=False, const=True) # type: ignore
    AppliedForceOrTorque: float = Field(alias="AppliedForceOrTorque", default=None)
    SpringForceOrTorqueVsPosition: List[SpringForceOrTorqueVsPosition] = Field(alias="SpringForceOrTorqueVsPosition", default=list())
    DamperForceOrTorqueVsRate: List[DamperForceOrTorqueVsRate] = Field(alias="DamperForceOrTorqueVsRate", default=list())

    _relative_schema_path = 'Components/PitchSystem/PitchController/PitchSafetySystem/PitchActuationLimited.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['SpringForceOrTorqueVsPosition','DamperForceOrTorqueVsRate',]),
        'PitchSafetySystemType').merge(PitchControllerTorqueSafetySystem._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchActuationLimited.update_forward_refs()
