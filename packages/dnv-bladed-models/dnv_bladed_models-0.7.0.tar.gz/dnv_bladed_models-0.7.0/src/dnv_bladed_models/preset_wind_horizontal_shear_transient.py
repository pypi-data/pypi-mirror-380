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
from dnv_bladed_models.wind_horizontal_shear_variation import WindHorizontalShearVariation
class PresetWindHorizontalShearTransient_VariationShapeEnum(str, Enum):
    FULL = "FULL"
    HALF = "HALF"
    IEC_2 = "IEC-2"

from .schema_helper import SchemaHelper
from .models_impl import *


class PresetWindHorizontalShearTransient(WindHorizontalShearVariation):
    r"""
    A preset transient in the horizontal wind shear.
    
    Attributes
    ----------
    HorizontalShearVariationType : Literal['PresetTransient'], default='PresetTransient'
        Defines the specific type of HorizontalShearVariation model in use.  For a `PresetTransient` object, this must always be set to a value of `PresetTransient`.
    
    HorizontalShearAtStart : float
        The horizontal wind shear at the start of the simulation up to the beginning of the transient.  For a full cycle this will also be the value after the transient has completed.
    
    AmplitudeOfVariation : float
        The maximum amplitude of the variation.
    
    StartTime : float
        The time into the simulation at which to start the transient (excluding the lead-in time).
    
    DurationOfVariation : float
        The time taken to complete the transient, whether half-cycle or full-cycle.
    
    VariationShape : PresetWindHorizontalShearTransient_VariationShapeEnum
        The shape of the transient.  This can either be a half-cycle (where the wind shear remains at the initial wind shear plus the amplitude after the transient has been completed) or a full-cycle (where the wind shear returns to its original value).
    
    Notes
    -----
    
    """
    HorizontalShearVariationType: Literal['PresetTransient'] = Field(alias="HorizontalShearVariationType", default='PresetTransient', allow_mutation=False, const=True) # type: ignore
    HorizontalShearAtStart: float = Field(alias="HorizontalShearAtStart", default=None)
    AmplitudeOfVariation: float = Field(alias="AmplitudeOfVariation", default=None)
    StartTime: float = Field(alias="StartTime", default=None)
    DurationOfVariation: float = Field(alias="DurationOfVariation", default=None)
    VariationShape: PresetWindHorizontalShearTransient_VariationShapeEnum = Field(alias="VariationShape", default=None)

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/WindHorizontalShearVariation/PresetWindHorizontalShearTransient.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'HorizontalShearVariationType').merge(WindHorizontalShearVariation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PresetWindHorizontalShearTransient.update_forward_refs()
