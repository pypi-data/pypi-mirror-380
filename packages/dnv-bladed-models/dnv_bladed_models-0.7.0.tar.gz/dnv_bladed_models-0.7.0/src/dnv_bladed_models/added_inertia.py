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
class AddedInertia_AddedInertiaTypeEnum(str, Enum):
    POINT_INERTIA = "PointInertia"
    SIX_BY_SIX_INERTIA = "SixBySixInertia"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class AddedInertia(BladedModel, ABC):
    r"""
    The common properties of inertias added to the tower component.
    
    Attributes
    ----------
    AddedInertiaType : AddedInertia_AddedInertiaTypeEnum
        Defines the specific type of model in use.
    
    IgnoreGravityLoads : bool, default=False
        If true, the loads due to gravity on this inertia will be ignored.
    
    HeightUpTower : float, default=0
        The height measured from the bottom of the tower, assuming that the tower is mounted vertically.
    
    SnapToNearestNode : bool
        If true, the inertias will be added to the nearest structural node, which may be at a significantly different height to that specified.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - AddedInertiaInsert
        - PointInertia
        - SixBySixInertia
    
    """
    AddedInertiaType: AddedInertia_AddedInertiaTypeEnum = Field(alias="AddedInertiaType", default=None)
    IgnoreGravityLoads: bool = Field(alias="IgnoreGravityLoads", default=None)
    HeightUpTower: float = Field(alias="HeightUpTower", default=None)
    SnapToNearestNode: bool = Field(alias="SnapToNearestNode", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


AddedInertia.update_forward_refs()
