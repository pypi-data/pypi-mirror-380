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
from dnv_bladed_models.irregular_waves import IrregularWaves

from .schema_helper import SchemaHelper
from .models_impl import *


class JonswapPiersonMoskowitz(IrregularWaves):
    r"""
    The definition of Jonswap/Pierson-Moskowitz spectrum waves.
    
    Not supported yet.
    
    Attributes
    ----------
    WavesType : Literal['JonswapPiersonMoskowitz'], default='JonswapPiersonMoskowitz', Not supported yet
        Defines the specific type of Waves model in use.  For a `JonswapPiersonMoskowitz` object, this must always be set to a value of `JonswapPiersonMoskowitz`.
    
    SignificantWaveHeight : float, Not supported yet
        The average height of the highest one third of the waves in the seastate.
    
    SpectralPeakPeriod : float, Not supported yet
        The period of the most energetic component in the wave spectrum.
    
    Peakedness : float, Not supported yet
        The width of the frequency band containing most of the energy in the spectrum.  It should take a value between 1 (Pierson-Moskowitz) and 7.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    WavesType: Literal['JonswapPiersonMoskowitz'] = Field(alias="WavesType", default='JonswapPiersonMoskowitz', allow_mutation=False, const=True) # Not supported yet # type: ignore
    SignificantWaveHeight: float = Field(alias="SignificantWaveHeight", default=None) # Not supported yet
    SpectralPeakPeriod: float = Field(alias="SpectralPeakPeriod", default=None) # Not supported yet
    Peakedness: float = Field(alias="Peakedness", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Waves/JonswapPiersonMoskowitz.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'WavesType').merge(IrregularWaves._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


JonswapPiersonMoskowitz.update_forward_refs()
