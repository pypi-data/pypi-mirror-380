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
from dnv_bladed_models.time_domain_current import TimeDomainCurrent
class TurbulentCurrent_CentreTurbulenceFileOnEnum(str, Enum):
    CENTRED_ON_HUB = "CENTRED_ON_HUB"
    BEST_FIT = "BEST_FIT"

from .schema_helper import SchemaHelper
from .models_impl import *


class TurbulentCurrent(TimeDomainCurrent):
    r"""
    The definition of a turbulent flow field, with the values for the turbulence defined in an external file.
    
    Not supported yet.
    
    Attributes
    ----------
    CurrentType : Literal['TurbulentCurrent'], default='TurbulentCurrent', Not supported yet
        Defines the specific type of Current model in use.  For a `TurbulentCurrent` object, this must always be set to a value of `TurbulentCurrent`.
    
    MeanSpeed : float, Not supported yet
        The mean current speed upon which the turbulence will be added.  This must correspond with the mean current speed used to create the turbulence file.
    
    TurbulenceFilepath : str, Not supported yet
        The filepath or URI of the turbulence file.
    
    TurbulenceIntensity : float, Not supported yet
        The turbulence intensity in the longitudinal (global X) direction.  This is used to scale the turbulence provided in the file.
    
    TurbulenceIntensityLateral : float, Not supported yet
        The turbulence intensity in the lateral (global Y) direction.  This is typically in the order of 80% of the longitudinal turbulence intensity.
    
    TurbulenceIntensityVertical : float, Not supported yet
        The turbulence intensity in the vertical (global Z) direction.  This is typically in the order of 50% of the longitudinal turbulence intensity.
    
    CentreTurbulenceFileOn : TurbulentCurrent_CentreTurbulenceFileOnEnum, Not supported yet
        The method used to position the data in the turbulence file relative to the turbine.  If any part of the rotor exceeds this box, the simulation will terminate with an exception.
    
    CentreTurbulenceFileAtHeight : float, Not supported yet
        The height at which to centre the data in the turbulence file.  If any part of the rotor exceeds this box, the simulation will terminate with an exception.
    
    RepeatTurbulenceFile : bool, Not supported yet
        If true, the turbulence file will be \"looped\".  If false, the turbulence will be 0 in all three components once the end of the file has been reached.  Using part of a turbulence file may invalidate its turbulence statistics, and no effort is made by Bladed to ensure coherence at the point when it transitions from the end of the wind file back to the beginning.
    
    TurbulenceFileStartTime : float, default=0, Not supported yet
        The time into turbulent wind file at start of simulation.  This can be used to synchronise the wind file with simulation.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    CurrentType: Literal['TurbulentCurrent'] = Field(alias="CurrentType", default='TurbulentCurrent', allow_mutation=False, const=True) # Not supported yet # type: ignore
    MeanSpeed: float = Field(alias="MeanSpeed", default=None) # Not supported yet
    TurbulenceFilepath: str = Field(alias="TurbulenceFilepath", default=None) # Not supported yet
    TurbulenceIntensity: float = Field(alias="TurbulenceIntensity", default=None) # Not supported yet
    TurbulenceIntensityLateral: float = Field(alias="TurbulenceIntensityLateral", default=None) # Not supported yet
    TurbulenceIntensityVertical: float = Field(alias="TurbulenceIntensityVertical", default=None) # Not supported yet
    CentreTurbulenceFileOn: TurbulentCurrent_CentreTurbulenceFileOnEnum = Field(alias="CentreTurbulenceFileOn", default=None) # Not supported yet
    CentreTurbulenceFileAtHeight: float = Field(alias="CentreTurbulenceFileAtHeight", default=None) # Not supported yet
    RepeatTurbulenceFile: bool = Field(alias="RepeatTurbulenceFile", default=None) # Not supported yet
    TurbulenceFileStartTime: float = Field(alias="TurbulenceFileStartTime", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Current/TurbulentCurrent.json'
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


TurbulentCurrent.update_forward_refs()
