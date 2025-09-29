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
from dnv_bladed_models.foundation import Foundation

from .schema_helper import SchemaHelper
from .models_impl import *


class LinearFoundation(Foundation):
    r"""
    A foundation represented by a linear stiffness and mass matrix at a single point.
    
    Attributes
    ----------
    FoundationType : Literal['LinearFoundation'], default='LinearFoundation'
        Defines the specific type of Foundation model in use.  For a `LinearFoundation` object, this must always be set to a value of `LinearFoundation`.
    
    StiffnessMatrix : List[List[float]]
        A 6x6 matrix representing the linear and rotational stiffnesses of an object or joint.
    
    MassMatrix : List[List[float]]
        A 6x6 matrix representing the mass and rotational inertias of an object.  These are symmetric matrices for all real-world objects.
    
    Notes
    -----
    
    """
    FoundationType: Literal['LinearFoundation'] = Field(alias="FoundationType", default='LinearFoundation', allow_mutation=False, const=True) # type: ignore
    StiffnessMatrix: List[List[float]] = Field(alias="StiffnessMatrix", default=list())
    MassMatrix: List[List[float]] = Field(alias="MassMatrix", default=list())

    _relative_schema_path = 'Components/Tower/Foundation/LinearFoundation.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['StiffnessMatrix','MassMatrix',]),
        'FoundationType').merge(Foundation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


LinearFoundation.update_forward_refs()
