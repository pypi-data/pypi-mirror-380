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
from dnv_bladed_models.alpha_line import AlphaLine
from dnv_bladed_models.bladed_model import BladedModel

from .schema_helper import SchemaHelper
from .models_impl import *


class Aerofoil(BladedModel):
    r"""
    The definition of a single 2D aerodynamic aerofoil section.
    
    Attributes
    ----------
    ChordwiseOriginForForcesAndMoments : float, default=0.25
        The fraction of the chord from the leading edge to the position about which Cl, Cd, and Cm have been calculated.  This is traditionally 0.25 (25%), but can be any location so long as it is consistent with the provided aerodynamic data.
    
    AerodynamicPerformance : List[AlphaLine]
        The relationship between angle of attack, and the lift and drag coefficients.
    
    ReynoldsNumber : float
        The Reynolds number at which the aerodynamic properties were obtained.
    
    ThicknessToChordRatio : float
        The ratio between the thickness and the chord length of the measured aerofoil.
    
    Notes
    -----
    
    """
    ChordwiseOriginForForcesAndMoments: float = Field(alias="ChordwiseOriginForForcesAndMoments", default=None)
    AerodynamicPerformance: List[AlphaLine] = Field(alias="AerodynamicPerformance", default=list())
    ReynoldsNumber: float = Field(alias="ReynoldsNumber", default=None)
    ThicknessToChordRatio: float = Field(alias="ThicknessToChordRatio", default=None)

    _relative_schema_path = 'Components/Blade/AerofoilLibrary/Aerofoil/Aerofoil.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['AerodynamicPerformance',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


Aerofoil.update_forward_refs()
