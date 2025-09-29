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


class LookUpTableElement(BladedModel):
    r"""
    
    
    Not supported yet.
    
    Attributes
    ----------
    DistanceFromFocalPoint : float, Not supported yet
        The distance either side of the nominal focal distance that the sample was collected from.  If there isn't a value provided for a distance of 0.0, the weighting will be assumed to be 1.0 (100%).
    
    ProportionOfSignal : float, Not supported yet
        The proportion of the signal to take at the corresponding distance from the nominal focal distance, also known as the weighting.  This should range from 1.0 (100%) down to 0.0 (0%).
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    DistanceFromFocalPoint: float = Field(alias="DistanceFromFocalPoint", default=None) # Not supported yet
    ProportionOfSignal: float = Field(alias="ProportionOfSignal", default=None) # Not supported yet

    _relative_schema_path = 'Components/Lidar/LookUpTableElement/LookUpTableElement.json'
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


LookUpTableElement.update_forward_refs()
