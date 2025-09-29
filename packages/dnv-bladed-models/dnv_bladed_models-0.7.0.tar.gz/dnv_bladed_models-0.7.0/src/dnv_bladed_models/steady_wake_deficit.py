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
class SteadyWakeDeficit_SteadyWakeDeficitTypeEnum(str, Enum):
    GAUSSIAN = "Gaussian"
    USER_DEFINED = "UserDefined"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class SteadyWakeDeficit(BladedModel, ABC):
    r"""
    A simple model for the reduced velocity of the wind behind another turbine.  This deficit will be applied across a certain region, and this region will not move around during the simulation.
    
    Attributes
    ----------
    SteadyWakeDeficitType : SteadyWakeDeficit_SteadyWakeDeficitTypeEnum
        Defines the specific type of model in use.
    
    HorizontalOffsetFromHub : float
        The horizontal (global Y) offset of the upwind turbine from the turbine being simulated.
    
    VerticalOffsetFromHub : float
        The vertical (global Z) offset of the upwind turbine from the turbine being simulated.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - Gaussian
        - SteadyWakeDeficitInsert
        - UserDefinedWakeDeficit
    
    """
    SteadyWakeDeficitType: SteadyWakeDeficit_SteadyWakeDeficitTypeEnum = Field(alias="SteadyWakeDeficitType", default=None)
    HorizontalOffsetFromHub: float = Field(alias="HorizontalOffsetFromHub", default=None)
    VerticalOffsetFromHub: float = Field(alias="VerticalOffsetFromHub", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


SteadyWakeDeficit.update_forward_refs()
