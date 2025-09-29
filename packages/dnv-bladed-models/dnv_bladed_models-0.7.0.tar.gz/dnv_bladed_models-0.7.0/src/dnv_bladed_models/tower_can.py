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
from dnv_bladed_models.tower_can_modelling import TowerCanModelling
class TowerCan_TowerCanTypeEnum(str, Enum):
    EXPLICIT_TOWER_CAN = "ExplicitTowerCan"
    SIMPLE_TOWER_CAN = "SimpleTowerCan"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class TowerCan(BladedModel, ABC):
    r"""
    The common properties for a single can in the tower
    
    Attributes
    ----------
    TowerCanType : TowerCan_TowerCanTypeEnum
        Defines the specific type of model in use.
    
    Modelling : TowerCanModelling
    
    CanHeight : float
        The height of the tower can, assuming that it is mounted vertically.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - ExplicitTowerCan
        - TowerCanInsert
        - SimpleTowerCan
    
    """
    TowerCanType: TowerCan_TowerCanTypeEnum = Field(alias="TowerCanType", default=None)
    Modelling: TowerCanModelling = Field(alias="Modelling", default=None)
    CanHeight: float = Field(alias="CanHeight", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


TowerCan.update_forward_refs()
