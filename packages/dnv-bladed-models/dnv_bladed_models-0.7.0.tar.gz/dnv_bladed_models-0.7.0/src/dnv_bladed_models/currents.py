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
from dnv_bladed_models.near_shore_current import NearShoreCurrent
from dnv_bladed_models.near_surface_current import NearSurfaceCurrent
from dnv_bladed_models.sub_surface_current import SubSurfaceCurrent
from dnv_bladed_models.time_domain_current import TimeDomainCurrent

from .schema_helper import SchemaHelper
from .models_impl import *


class Currents(TimeDomainCurrent):
    r"""
    The definition of the current using simple numerical models.
    
    Not supported yet.
    
    Attributes
    ----------
    CurrentType : Literal['Currents'], default='Currents', Not supported yet
        Defines the specific type of Current model in use.  For a `Currents` object, this must always be set to a value of `Currents`.
    
    NearSurfaceCurrent : NearSurfaceCurrent, Not supported yet
    
    SubSurfaceCurrent : SubSurfaceCurrent, Not supported yet
    
    NearShoreCurrent : NearShoreCurrent, Not supported yet
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    CurrentType: Literal['Currents'] = Field(alias="CurrentType", default='Currents', allow_mutation=False, const=True) # Not supported yet # type: ignore
    NearSurfaceCurrent: NearSurfaceCurrent = Field(alias="NearSurfaceCurrent", default=None) # Not supported yet
    SubSurfaceCurrent: SubSurfaceCurrent = Field(alias="SubSurfaceCurrent", default=None) # Not supported yet
    NearShoreCurrent: NearShoreCurrent = Field(alias="NearShoreCurrent", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Current/Currents.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'CurrentType').merge(TimeDomainCurrent._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


Currents.update_forward_refs()
