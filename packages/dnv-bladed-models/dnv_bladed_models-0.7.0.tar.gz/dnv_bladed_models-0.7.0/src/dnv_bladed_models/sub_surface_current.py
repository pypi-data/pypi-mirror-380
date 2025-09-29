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


class SubSurfaceCurrent(BladedModel):
    r"""
    The definition of a current whose strength depends on height above the sea bed according to a power law or a user defined relationship.
    
    Not supported yet.
    
    Attributes
    ----------
    VelocityAtSurface : float, Not supported yet
        The current speed at the surface.
    
    Heading : float, Not supported yet
        The direction towards which the current is flowing (measured clockwise from North).
    
    ShearExponent : float, Not supported yet
        The shear exponent of the sub-surface current.  This is typically in the order of 1/7.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    VelocityAtSurface: float = Field(alias="VelocityAtSurface", default=None) # Not supported yet
    Heading: float = Field(alias="Heading", default=None) # Not supported yet
    ShearExponent: float = Field(alias="ShearExponent", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Current/SubSurfaceCurrent/SubSurfaceCurrent.json'
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


SubSurfaceCurrent.update_forward_refs()
