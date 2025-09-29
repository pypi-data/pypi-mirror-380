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
from dnv_bladed_models.current_direction_variation import CurrentDirectionVariation
class PresetCurrentDirectionTransient_VariationShapeEnum(str, Enum):
    FULL = "FULL"
    HALF = "HALF"
    IEC_2 = "IEC-2"

from .schema_helper import SchemaHelper
from .models_impl import *


class PresetCurrentDirectionTransient(CurrentDirectionVariation):
    r"""
    A preset transient in the current's direction.
    
    Not supported yet.
    
    Attributes
    ----------
    DirectionVariationType : Literal['PresetTransient'], default='PresetTransient', Not supported yet
        Defines the specific type of DirectionVariation model in use.  For a `PresetTransient` object, this must always be set to a value of `PresetTransient`.
    
    DirectionAtStart : float, Not supported yet
        The direction at the start of the simulation up to the beginning of the transient.  For a full cycle this will also be the value after the transient has completed.
    
    AmplitudeOfVariation : float, Not supported yet
        The maximum amplitude of the variation.
    
    StartTime : float, Not supported yet
        The time into the simulation at which to start the transient (excluding the lead-in time).
    
    DurationOfVariation : float, Not supported yet
        The time taken to complete the transient, whether half-cycle or full-cycle.
    
    VariationShape : PresetCurrentDirectionTransient_VariationShapeEnum, Not supported yet
        The shape of the transient.  This can either be a half-cycle (where the direction remains at the initial direction plus the amplitude after the transient has been completed) or a full-cycle (where the direction returns to its original value).
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    DirectionVariationType: Literal['PresetTransient'] = Field(alias="DirectionVariationType", default='PresetTransient', allow_mutation=False, const=True) # Not supported yet # type: ignore
    DirectionAtStart: float = Field(alias="DirectionAtStart", default=None) # Not supported yet
    AmplitudeOfVariation: float = Field(alias="AmplitudeOfVariation", default=None) # Not supported yet
    StartTime: float = Field(alias="StartTime", default=None) # Not supported yet
    DurationOfVariation: float = Field(alias="DurationOfVariation", default=None) # Not supported yet
    VariationShape: PresetCurrentDirectionTransient_VariationShapeEnum = Field(alias="VariationShape", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Current/CurrentDirectionVariation/PresetCurrentDirectionTransient.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'DirectionVariationType').merge(CurrentDirectionVariation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PresetCurrentDirectionTransient.update_forward_refs()
