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
class PitchSafetySystem_PitchSafetySystemTypeEnum(str, Enum):
    ACTUATION_LIMITED = "ActuationLimited"
    CONSTANT_RATE = "ConstantRate"
    RATE_DEMAND_SET_BY_EXTERNAL_CONTROLLER = "RateDemandSetByExternalController"
    RATE_VARIES_WITH_POSITION = "RateVariesWithPosition"
    RATE_VARIES_WITH_TIME = "RateVariesWithTime"
    TORQUE_SET_BY_EXTERNAL_CONTROLLER = "TorqueSetByExternalController"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchSafetySystem(BladedModel, ABC):
    r"""
    The common properties of a pitch controller's safety system.
    
    Attributes
    ----------
    PitchSafetySystemType : PitchSafetySystem_PitchSafetySystemTypeEnum
        Defines the specific type of model in use.
    
    AlwaysUseBackupPower : bool, default=False
        Backup power is normally only used in a grid loss.  If true, this will trigger a switch to backup power torque limits in all safety system pitch action events.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - PitchActuationLimited
        - PitchConstantRateSafetySystem
        - PitchSafetySystemInsert
        - PitchRateDemandSetByExternalController
        - PitchRateVariesWithPosition
        - PitchRateVariesWithTime
        - PitchTorqueSetByExternalController
    
    """
    PitchSafetySystemType: PitchSafetySystem_PitchSafetySystemTypeEnum = Field(alias="PitchSafetySystemType", default=None)
    AlwaysUseBackupPower: bool = Field(alias="AlwaysUseBackupPower", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


PitchSafetySystem.update_forward_refs()
