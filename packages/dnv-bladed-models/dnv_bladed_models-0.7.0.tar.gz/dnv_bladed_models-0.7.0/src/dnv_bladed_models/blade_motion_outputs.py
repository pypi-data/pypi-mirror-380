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


class BladeMotionOutputs(BladedModel):
    r"""
    Loads selected
    
    Not supported yet.
    
    Attributes
    ----------
    OutOfPlaneDeflection : bool, default=False, Not supported yet
        Which blade deflections to output in the out of plane direction (x, y, z).
    
    InPlaneDeflection : bool, default=False, Not supported yet
        Which blade deflections to output in the in plane direction (x, y, z).
    
    BladeAccelerations : bool, default=False, Not supported yet
        Which blade accelerations to output (x, y, z).
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    OutOfPlaneDeflection: bool = Field(alias="OutOfPlaneDeflection", default=None) # Not supported yet
    InPlaneDeflection: bool = Field(alias="InPlaneDeflection", default=None) # Not supported yet
    BladeAccelerations: bool = Field(alias="BladeAccelerations", default=None) # Not supported yet

    _relative_schema_path = 'Components/Blade/BladeOutputGroupLibrary/BladeOutputGroup/BladeMotionOutputs/BladeMotionOutputs.json'
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


BladeMotionOutputs.update_forward_refs()
