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
from dnv_bladed_models.dynamic_wake import DynamicWake

from .schema_helper import SchemaHelper
from .models_impl import *


class FreeFlowModel(DynamicWake):
    r"""
    The Free-flow dynamic wake model represents a case where there is no induction, and so no momentum calculation.  The lift, drag and moment polars are used directly.  This could be appropriate to use in e.g. parked or idling.  This option might be removed in a future re-design of the aerodynamic settings.
    
    Attributes
    ----------
    DynamicWakeType : Literal['FreeFlowModel'], default='FreeFlowModel'
        Defines the specific type of DynamicWake model in use.  For a `FreeFlowModel` object, this must always be set to a value of `FreeFlowModel`.
    
    Notes
    -----
    
    """
    DynamicWakeType: Literal['FreeFlowModel'] = Field(alias="DynamicWakeType", default='FreeFlowModel', allow_mutation=False, const=True) # type: ignore

    _relative_schema_path = 'Settings/AerodynamicSettings/AerodynamicModel/MomentumTheoryCorrections/DynamicWake/FreeFlowModel.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'DynamicWakeType').merge(DynamicWake._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


FreeFlowModel.update_forward_refs()
