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
class Foundation_FoundationTypeEnum(str, Enum):
    LINEAR_FOUNDATION = "LinearFoundation"
    SIMPLIFIED_LINEAR_FOUNDATION = "SimplifiedLinearFoundation"
    INSERT = "Insert"

from .schema_helper import SchemaHelper
from .models_impl import *


class Foundation(BladedModel, ABC):
    r"""
    FOUNDATION\"
    
    Attributes
    ----------
    FoundationType : Foundation_FoundationTypeEnum
        Defines the specific type of model in use.
    
    UseFiniteElementDeflectionsForFoundationLoads : bool, default=False
        When this feature is enabled, support structure deflections calculated from the underlying finite element model are used to evaluate the foundation applied loads. The effect of these foundation loads is included when evaluating the turbine dynamic response.  This model is only active for time domain simulations. The foundation applied loads are calculated from the finite element deflections from the previous time step. This means that time step convergence studies may be required to ensure the accuracy of this model.  When this feature is enabled, the support structure node deflection outputs will be based on the finite element model rather than the modal deflections that are normally used. This ensures consistency between the foundation applied loads and the support structure node deflections.
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - FoundationInsert
        - LinearFoundation
        - SimplifiedLinearFoundation
    
    """
    FoundationType: Foundation_FoundationTypeEnum = Field(alias="FoundationType", default=None)
    UseFiniteElementDeflectionsForFoundationLoads: bool = Field(alias="UseFiniteElementDeflectionsForFoundationLoads", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


Foundation.update_forward_refs()
