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
from dnv_bladed_models.frequency_vs_spectral_density import FrequencyVsSpectralDensity
from dnv_bladed_models.irregular_waves import IrregularWaves

from .schema_helper import SchemaHelper
from .models_impl import *


class UserDefinedWaves(IrregularWaves):
    r"""
    A look-up table for a user-defined wave spectrum.
    
    Not supported yet.
    
    Attributes
    ----------
    WavesType : Literal['UserDefined'], default='UserDefined', Not supported yet
        Defines the specific type of Waves model in use.  For a `UserDefined` object, this must always be set to a value of `UserDefined`.
    
    FrequencyVsSpectralDensity : List[FrequencyVsSpectralDensity], Not supported yet
        List of FrequencyVsSpectralDensity
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    WavesType: Literal['UserDefined'] = Field(alias="WavesType", default='UserDefined', allow_mutation=False, const=True) # Not supported yet # type: ignore
    FrequencyVsSpectralDensity: List[FrequencyVsSpectralDensity] = Field(alias="FrequencyVsSpectralDensity", default=list()) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Waves/UserDefinedWaves.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['FrequencyVsSpectralDensity',]),
        'WavesType').merge(IrregularWaves._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


UserDefinedWaves.update_forward_refs()
