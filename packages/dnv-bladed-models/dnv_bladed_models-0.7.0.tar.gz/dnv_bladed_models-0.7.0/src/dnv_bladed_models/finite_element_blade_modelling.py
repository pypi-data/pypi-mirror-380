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
from dnv_bladed_models.blade_modelling import BladeModelling
from dnv_bladed_models.structural_mode import StructuralMode

from .schema_helper import SchemaHelper
from .models_impl import *


class FiniteElementBladeModelling(BladeModelling):
    r"""
    The properties for the structural modelling of the blade using finite element analysis without modal reduction.
    
    Attributes
    ----------
    BladeModellingType : Literal['FiniteElementBladeModelling'], default='FiniteElementBladeModelling'
        Defines the specific type of BladeModelling model in use.  For a `FiniteElementBladeModelling` object, this must always be set to a value of `FiniteElementBladeModelling`.
    
    WholeBladeModeDampingRatios : List[StructuralMode]
        List of known whole-blade mode damping ratios. The whole-blade damping ratios will be converted into finite element degrees of freedom by Bladed. If the list is incomplete, meaning it lacks damping ratios for all modes, Bladed will assign frequency-proportional damping based on the damping ratio of the highest defined mode. The list must contain at least one entry.
    
    Notes
    -----
    
    """
    BladeModellingType: Literal['FiniteElementBladeModelling'] = Field(alias="BladeModellingType", default='FiniteElementBladeModelling', allow_mutation=False, const=True) # type: ignore
    WholeBladeModeDampingRatios: List[StructuralMode] = Field(alias="WholeBladeModeDampingRatios", default=list())

    _relative_schema_path = 'Components/Blade/BladeModelling/FiniteElementBladeModelling.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['WholeBladeModeDampingRatios',]),
        'BladeModellingType').merge(BladeModelling._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


FiniteElementBladeModelling.update_forward_refs()
