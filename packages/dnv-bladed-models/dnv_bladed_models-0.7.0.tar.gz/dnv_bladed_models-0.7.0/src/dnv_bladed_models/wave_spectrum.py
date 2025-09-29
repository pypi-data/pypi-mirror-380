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
from dnv_bladed_models.vector3_d import Vector3D
from dnv_bladed_models.waves import Waves
class WaveSpectrum_WaveCurrentInteractionMethodEnum(str, Enum):
    TYPE1 = "Type1"
    TYPE2A = "Type2a"
    TYPE2B = "Type2b"
    TYPE2C_I = "Type2c_i"
    TYPE2C_II = "Type2c_ii"

from .schema_helper import SchemaHelper
from .models_impl import *


class WaveSpectrum(Waves):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    WavesType : Literal['WaveSpectrum'], default='WaveSpectrum', Not supported yet
        Defines the specific type of Waves model in use.  For a `WaveSpectrum` object, this must always be set to a value of `WaveSpectrum`.
    
    PhaseOrigin : Vector3D
    
    SeaStateFilepath : str, Not supported yet
        The location of .SEA file describing the simulation seastate.
    
    WaveCurrentInteractionMethod : WaveSpectrum_WaveCurrentInteractionMethodEnum, default='Type1', Not supported yet
        The method to be used in combining waves and currents to obtain overall water particle kinematics.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    WavesType: Literal['WaveSpectrum'] = Field(alias="WavesType", default='WaveSpectrum', allow_mutation=False, const=True) # Not supported yet # type: ignore
    PhaseOrigin: Vector3D = Field(alias="PhaseOrigin", default=None)
    SeaStateFilepath: str = Field(alias="SeaStateFilepath", default=None) # Not supported yet
    WaveCurrentInteractionMethod: WaveSpectrum_WaveCurrentInteractionMethodEnum = Field(alias="WaveCurrentInteractionMethod", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Waves/WaveSpectrum.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'WavesType').merge(Waves._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


WaveSpectrum.update_forward_refs()
