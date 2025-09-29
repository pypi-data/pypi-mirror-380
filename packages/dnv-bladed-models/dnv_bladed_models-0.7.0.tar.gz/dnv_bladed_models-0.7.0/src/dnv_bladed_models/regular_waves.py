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
from dnv_bladed_models.waves import Waves

from .schema_helper import SchemaHelper
from .models_impl import *


class RegularWaves(Waves, ABC):
    r"""
    The definition of regular waves.
    
    Not supported yet.
    
    Attributes
    ----------
    DirectionOfApproachClockwiseFromNorth : float, Not supported yet
        The bearing from which waves arrive at the turbine.
    
    WaveHeight : float, Not supported yet
        The wave height, defined from trough to crest.
    
    Period : float, Not supported yet
        The wave period.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    DirectionOfApproachClockwiseFromNorth: float = Field(alias="DirectionOfApproachClockwiseFromNorth", default=None) # Not supported yet
    WaveHeight: float = Field(alias="WaveHeight", default=None) # Not supported yet
    Period: float = Field(alias="Period", default=None) # Not supported yet

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(Waves._type_info)


RegularWaves.update_forward_refs()
