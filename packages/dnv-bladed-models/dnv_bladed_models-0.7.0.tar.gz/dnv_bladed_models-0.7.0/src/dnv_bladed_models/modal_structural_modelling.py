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
from dnv_bladed_models.structural_mode import StructuralMode
from dnv_bladed_models.structural_modelling import StructuralModelling

from .schema_helper import SchemaHelper
from .models_impl import *


class ModalStructuralModelling(StructuralModelling):
    r"""
    The properties for the structural modelling using modal reduction.
    
    Attributes
    ----------
    StructuralModellingType : Literal['ModalStructuralModelling'], default='ModalStructuralModelling'
        Defines the specific type of StructuralModelling model in use.  For a `ModalStructuralModelling` object, this must always be set to a value of `ModalStructuralModelling`.
    
    StructuralModes : List[StructuralMode]
        List of included modes and their associated damping ratios. The presence of any of these objects in the StructuralModes list indicates that the mode should be calculated, even if it does not include a DampingRatio. If no modes are provided, the structure will be considered rigid. Users can add any metadata alongside the DampingRatio, such as _Name or _Mode. Bladed will disregard any metadata as long as it is prefixed with an underscore.
    
    Notes
    -----
    
    """
    StructuralModellingType: Literal['ModalStructuralModelling'] = Field(alias="StructuralModellingType", default='ModalStructuralModelling', allow_mutation=False, const=True) # type: ignore
    StructuralModes: List[StructuralMode] = Field(alias="StructuralModes", default=list())

    _relative_schema_path = 'Components/StructuralModelling/ModalStructuralModelling.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['StructuralModes',]),
        'StructuralModellingType').merge(StructuralModelling._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


ModalStructuralModelling.update_forward_refs()
