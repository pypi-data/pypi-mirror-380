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


class AerodynamicProperties(BladedModel):
    r"""
    The aerodynamic properties of the blade cross-section.  These are defined in the QuarterChordCoordinateSystem, which specifies the position and orientation of the aerofoil.
    
    Attributes
    ----------
    Chord : float
        The chord of the blade at this cross-section, measured from leading to trailing edge.  The cross-section will be positioned so that the aerofoil's quarter-chord position coincides with the origin of the QuarterChordCoordinateSystem.
    
    ThicknessToChordRatio : float
        The ratio between the thickness and the chord length at the cross-section.  This would be 1.0 for a cylinder, and in the order of 0.1 (or 10%) for a typical slender aerofoil section.
    
    AerodynamicData : str, regex=^(AerofoilLibrary|InterpolatedAerofoilLibrary|AileronAerofoilLibrary).(.+)$
        A reference to an aerofoil, interpolated aerofoil, or aileron aerofoil to use for this cross-section.  The value must be the key of an aerofoil definition in either the AerofoilLibrary, InterpolatedAerofoilLibrary or AileronAerofoilLibrary.  i.e.  `AerofoilLibrary.<key>` or `InterpolatedAerofoilLibrary.<key>` or `AileronAerofoilLibrary.<key>`
    
    Notes
    -----
    
    """
    Chord: float = Field(alias="Chord", default=None)
    ThicknessToChordRatio: float = Field(alias="ThicknessToChordRatio", default=None)
    AerodynamicData: str = Field(alias="@AerodynamicData", default=None, regex='^(AerofoilLibrary|InterpolatedAerofoilLibrary|AileronAerofoilLibrary).(.+)$')

    _relative_schema_path = 'Components/Blade/CrossSection/AerodynamicProperties/AerodynamicProperties.json'
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


AerodynamicProperties.update_forward_refs()
