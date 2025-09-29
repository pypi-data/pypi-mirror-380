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
from dnv_bladed_models.bladed_model import BladedModel

from .schema_helper import SchemaHelper
from .models_impl import *


class SlippingClutch(BladedModel):
    r"""
    Slipping clutch model
    
    Attributes
    ----------
    Friction : float
        The friction of the clutch once in motion.
    
    Stiction : float
        The stiction or static friction of the clutch which opposes the initial movement.
    
    HighSpeedShaftInertia : float
        The rotational inertia of the high-speed shaft up to the clutch.  This is only relevant if there is a slipping clutch present, as otherwise it can be considered part of the generator.
    
    Notes
    -----
    
    """
    Friction: float = Field(alias="Friction", default=None)
    Stiction: float = Field(alias="Stiction", default=None)
    HighSpeedShaftInertia: float = Field(alias="HighSpeedShaftInertia", default=None)

    _relative_schema_path = 'Components/DrivetrainAndNacelle/SlippingClutch/SlippingClutch.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


SlippingClutch.update_forward_refs()
