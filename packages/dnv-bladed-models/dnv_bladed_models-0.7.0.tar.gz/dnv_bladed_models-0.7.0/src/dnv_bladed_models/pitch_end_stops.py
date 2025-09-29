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


class PitchEndStops(BladedModel):
    r"""
    The pitch angles of end-stops at fine pitch (minimum) and feather pitch (maximum).
    
    Attributes
    ----------
    MinimumAngle : float
        The position of the end-stop in the fine pitch direction.
    
    MaximumAngle : float
        The position of the end-stop in the feather pitch direction.
    
    StiffnessOnceExceeded : float
        The stiffness of both end-stops.  Force is only applied when position has exceeded the end-stop position.
    
    Notes
    -----
    
    """
    MinimumAngle: float = Field(alias="MinimumAngle", default=None)
    MaximumAngle: float = Field(alias="MaximumAngle", default=None)
    StiffnessOnceExceeded: float = Field(alias="StiffnessOnceExceeded", default=None)

    _relative_schema_path = 'Components/PitchSystem/PitchEndStops/PitchEndStops.json'
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


PitchEndStops.update_forward_refs()
