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
class DynamicWake_DynamicWakeTypeEnum(str, Enum):
    EQUILIBRIUM_WAKE_MODEL = "EquilibriumWakeModel"
    FREE_FLOW_MODEL = "FreeFlowModel"
    FROZEN_WAKE_MODEL = "FrozenWakeModel"
    OYE_DYNAMIC_WAKE = "OyeDynamicWake"
    PITT_AND_PETERS_MODEL = "PittAndPetersModel"
    INSERT = "Insert"
class DynamicWake_AreaAveragingMethodEnum(str, Enum):
    OVER_ANNULUS = "OVER_ANNULUS"
    NONE = "NONE"

from .schema_helper import SchemaHelper
from .models_impl import *


class DynamicWake(BladedModel, ABC):
    r"""
    Common properties for all dynamic wake models.
    
    Attributes
    ----------
    DynamicWakeType : DynamicWake_DynamicWakeTypeEnum
        Defines the specific type of model in use.
    
    AreaAveragingMethod : DynamicWake_AreaAveragingMethodEnum, default='OVER_ANNULUS'
        With the \"over annulus\" method, the dynamic wake is calculated over the entire annular ring.  Induced velocities are averaged over the number of blades.  If \"none\" is selected, the annulus is divided into segments to which separate dynamic wakes are applied.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - EquilibriumWakeModel
        - FreeFlowModel
        - FrozenWakeModel
        - DynamicWakeInsert
        - OyeDynamicWake
        - PittAndPetersModel
    
    """
    DynamicWakeType: DynamicWake_DynamicWakeTypeEnum = Field(alias="DynamicWakeType", default=None)
    AreaAveragingMethod: DynamicWake_AreaAveragingMethodEnum = Field(alias="AreaAveragingMethod", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


DynamicWake.update_forward_refs()
