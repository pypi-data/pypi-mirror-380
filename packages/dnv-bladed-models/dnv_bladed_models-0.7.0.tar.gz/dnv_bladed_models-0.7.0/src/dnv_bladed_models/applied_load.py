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
from dnv_bladed_models.vector3_d import Vector3D
class AppliedLoad_AppliedLoadTypeEnum(str, Enum):
    BLADE_POINT_LOADING = "BladePointLoading"
    TOWER_POINT_LOADING = "TowerPointLoading"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class AppliedLoad(BladedModel, ABC):
    r"""
    The common properties of a point loading time history.
    
    Attributes
    ----------
    AppliedLoadType : AppliedLoad_AppliedLoadTypeEnum
        Defines the specific type of model in use.
    
    StartTime : float
        The time into the simulation at which to start applying the loading (excluding the lead-in time).
    
    LoadingFilepath : str
        A filepath or URI containing one or six degree of loading data.  In the case of the six degrees of freedom, these will be applied in the component's coordinate system.  Where a single degree of freedom is provided, SingleDirectionLoading must also be specified.
    
    DirectionOfLoading : Vector3D
    
    OnComponentInAssembly : str, regex=^Assembly.(.+)$
        A qualified, dot-separated path to a component in the assembly tree to which to apply the force.  i.e. `Assembly.<name1>.<name2>`
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - BladePointLoading
        - AppliedLoadInsert
        - TowerPointLoading
    
    """
    AppliedLoadType: AppliedLoad_AppliedLoadTypeEnum = Field(alias="AppliedLoadType", default=None)
    StartTime: float = Field(alias="StartTime", default=None)
    LoadingFilepath: str = Field(alias="LoadingFilepath", default=None)
    DirectionOfLoading: Vector3D = Field(alias="DirectionOfLoading", default=None)
    OnComponentInAssembly: str = Field(alias="@OnComponentInAssembly", default=None, regex='^Assembly.(.+)$')

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


AppliedLoad.update_forward_refs()
