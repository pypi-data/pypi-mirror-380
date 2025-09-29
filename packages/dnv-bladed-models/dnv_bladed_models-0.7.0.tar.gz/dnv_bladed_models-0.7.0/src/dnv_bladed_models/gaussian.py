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
from dnv_bladed_models.steady_wake_deficit import SteadyWakeDeficit

from .schema_helper import SchemaHelper
from .models_impl import *


class Gaussian(SteadyWakeDeficit):
    r"""
    A simple model for the reduced velocity of the wind behind another turbine.  This deficit will be applied across a certain region, and this region will not move around during the simulation.  The velocity deficit profile will be based on a Gaussian distribution, scaled by a maximum deficit and the radius of the region affected.
    
    Attributes
    ----------
    SteadyWakeDeficitType : Literal['Gaussian'], default='Gaussian'
        Defines the specific type of SteadyWakeDeficit model in use.  For a `Gaussian` object, this must always be set to a value of `Gaussian`.
    
    CentrelineVelocityDeficit : float
        The maximum deficit within the affected region, occurring in the centre.  1.0 or 100% would be a reduction of the wind to zero, whereas 0.0 or 0% would represent no change in the free-field wind speed.
    
    WidthOfDeficit : float
        The width of the region within which there is a velocity deficit.
    
    Notes
    -----
    
    """
    SteadyWakeDeficitType: Literal['Gaussian'] = Field(alias="SteadyWakeDeficitType", default='Gaussian', allow_mutation=False, const=True) # type: ignore
    CentrelineVelocityDeficit: float = Field(alias="CentrelineVelocityDeficit", default=None)
    WidthOfDeficit: float = Field(alias="WidthOfDeficit", default=None)

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/SteadyWakeDeficit/Gaussian.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'SteadyWakeDeficitType').merge(SteadyWakeDeficit._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


Gaussian.update_forward_refs()
