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


class RadiusVsDeficit(BladedModel):
    r"""
    A line or row in a look-up table, specifying a value of deficit for a specified radius.
    
    Attributes
    ----------
    Radius : float
        The radius at which the deficit applies.
    
    Deficit : float
        The deficit corresponding to the specified radius.  1.0 or 100% would be a reduction of the wind to zero, whereas 0.0 or 0% would represent no change in the free-field wind speed.
    
    Notes
    -----
    
    """
    Radius: float = Field(alias="Radius", default=None)
    Deficit: float = Field(alias="Deficit", default=None)

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/SteadyWakeDeficit/RadiusVsDeficit/RadiusVsDeficit.json'
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


RadiusVsDeficit.update_forward_refs()
