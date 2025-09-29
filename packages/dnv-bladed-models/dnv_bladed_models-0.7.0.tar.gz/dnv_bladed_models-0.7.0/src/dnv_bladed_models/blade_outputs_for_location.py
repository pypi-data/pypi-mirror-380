# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


# coding: utf-8

from __future__ import annotations

from abc import ABC

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
class BladeOutputsForLocation_BladeOutputsForLocationTypeEnum(str, Enum):
    OUTPUTS_FOR_CROSS_SECTION = "OutputsForCrossSection"
    OUTPUTS_FOR_POSITION = "OutputsForPosition"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class BladeOutputsForLocation(BladedModel, ABC):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    BladeOutputsForLocationType : BladeOutputsForLocation_BladeOutputsForLocationTypeEnum, Not supported yet
        Defines the specific type of model in use.
    
    Loads : bool, default=False, Not supported yet
        An array of blade station indices to output loads for (exclusive with BLOADS_POS).
    
    Motion : bool, default=False, Not supported yet
        An array of blade station indices to output deflections for (exclusive with BDEFLS_POS).
    
    Aerodynamics : bool, Not supported yet
        Whether to output loads on this node
    
    Hydrodynamics : bool, default=False, Not supported yet
        An array of blade radii to output water kinematics for (tidal only).
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    This class is an abstraction, with the following concrete implementations:
        - BladeOutputsForLocationInsert
        - BladeOutputsForCrossSection
        - BladeOutputsForPosition
    
    """
    BladeOutputsForLocationType: BladeOutputsForLocation_BladeOutputsForLocationTypeEnum = Field(alias="BladeOutputsForLocationType", default=None) # Not supported yet
    Loads: bool = Field(alias="Loads", default=None) # Not supported yet
    Motion: bool = Field(alias="Motion", default=None) # Not supported yet
    Aerodynamics: bool = Field(alias="Aerodynamics", default=None) # Not supported yet
    Hydrodynamics: bool = Field(alias="Hydrodynamics", default=None) # Not supported yet

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


BladeOutputsForLocation.update_forward_refs()
