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


class StructuralMode(BladedModel):
    r"""
    An object containing the DampingRatio for a particular structural mode. Used by the support structure to include structural modes and their associated DampingRatios, as well as by the blades to define WholeBladeModeDampingRatios. Users can add any metadata alongside the DampingRatio, such as _Name or _Mode. Bladed will disregard any metadata as long as it is prefixed with an underscore.
    
    Attributes
    ----------
    DampingRatio : float
        The damping ratio on the mode.  This is typically in the order of 0.005.  An underdamped mode can lead to numerical instability in the simulation, whereas overdamped mode can affect the veracity of the results.
    
    Notes
    -----
    
    """
    DampingRatio: float = Field(alias="DampingRatio", default=None)

    _relative_schema_path = 'Components/common/StructuralMode.json'
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


StructuralMode.update_forward_refs()
