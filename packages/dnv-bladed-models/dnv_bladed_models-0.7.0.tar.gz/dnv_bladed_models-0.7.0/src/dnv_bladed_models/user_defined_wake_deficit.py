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
from dnv_bladed_models.radius_vs_deficit import RadiusVsDeficit
from dnv_bladed_models.steady_wake_deficit import SteadyWakeDeficit

from .schema_helper import SchemaHelper
from .models_impl import *


class UserDefinedWakeDeficit(SteadyWakeDeficit):
    r"""
    A simple model for the reduced velocity of the wind behind another turbine.  This deficit will be applied across a certain region, and this region will not move around during the simulation.  The velocity deficit profile is a look-up table of the radius against the deficit at that radius.
    
    Attributes
    ----------
    SteadyWakeDeficitType : Literal['UserDefined'], default='UserDefined'
        Defines the specific type of SteadyWakeDeficit model in use.  For a `UserDefined` object, this must always be set to a value of `UserDefined`.
    
    RadiusVsDeficit : List[RadiusVsDeficit]
        A list of radii vs the deficit at that radius.  The first value should be at a radius of 0.0, and the largest radius will be the extent of the affected region.  At this point, the deficit is usually 0.0.
    
    Notes
    -----
    
    """
    SteadyWakeDeficitType: Literal['UserDefined'] = Field(alias="SteadyWakeDeficitType", default='UserDefined', allow_mutation=False, const=True) # type: ignore
    RadiusVsDeficit: List[RadiusVsDeficit] = Field(alias="RadiusVsDeficit", default=list())

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/SteadyWakeDeficit/UserDefinedWakeDeficit.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['RadiusVsDeficit',]),
        'SteadyWakeDeficitType').merge(SteadyWakeDeficit._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


UserDefinedWakeDeficit.update_forward_refs()
