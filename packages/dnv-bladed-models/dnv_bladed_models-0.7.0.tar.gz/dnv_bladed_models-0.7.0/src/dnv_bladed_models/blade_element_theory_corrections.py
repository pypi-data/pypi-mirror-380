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


class BladeElementTheoryCorrections(BladedModel):
    r"""
    Properties related to the blade element aspects of the Blade Element Momentum model.
    
    Attributes
    ----------
    UsePrandtlCorrectionForTipLoss : bool, default=True
        If true, a Prandtl correction for tip loss effects will be applied.
    
    UsePrandtlCorrectionForRootLoss : bool, default=False
        If true, a Prandtl correction for hub loss effects will be applied.
    
    UseDragInInduction : bool, default=True
        If true, the drag coefficient will be included in the induction calculations. This mainly influences the BEM solution near the root of the blade, where the drag force is significant.
    
    Notes
    -----
    
    """
    UsePrandtlCorrectionForTipLoss: bool = Field(alias="UsePrandtlCorrectionForTipLoss", default=None)
    UsePrandtlCorrectionForRootLoss: bool = Field(alias="UsePrandtlCorrectionForRootLoss", default=None)
    UseDragInInduction: bool = Field(alias="UseDragInInduction", default=None)

    _relative_schema_path = 'Settings/AerodynamicSettings/AerodynamicModel/BladeElementTheoryCorrections/BladeElementTheoryCorrections.json'
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


BladeElementTheoryCorrections.update_forward_refs()
