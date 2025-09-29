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
from dnv_bladed_models.blade_outputs_for_location import BladeOutputsForLocation

from .schema_helper import SchemaHelper
from .models_impl import *


class BladeOutputsForCrossSection(BladeOutputsForLocation):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    BladeOutputsForLocationType : Literal['OutputsForCrossSection'], default='OutputsForCrossSection', Not supported yet
        Defines the specific type of BladeOutputsForLocation model in use.  For a `OutputsForCrossSection` object, this must always be set to a value of `OutputsForCrossSection`.
    
    SectionReference : str, Not supported yet
        The cross-section at which to produce the outputs for.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    BladeOutputsForLocationType: Literal['OutputsForCrossSection'] = Field(alias="BladeOutputsForLocationType", default='OutputsForCrossSection', allow_mutation=False, const=True) # Not supported yet # type: ignore
    SectionReference: str = Field(alias="@SectionReference", default=None) # Not supported yet

    _relative_schema_path = 'Components/Blade/BladeOutputGroupLibrary/BladeOutputGroup/BladeOutputsForLocation/BladeOutputsForCrossSection.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'BladeOutputsForLocationType').merge(BladeOutputsForLocation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


BladeOutputsForCrossSection.update_forward_refs()
