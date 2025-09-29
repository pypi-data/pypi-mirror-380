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
from dnv_bladed_models.component import Component
from dnv_bladed_models.rotational_stiffness import RotationalStiffness
from dnv_bladed_models.translational_stiffness import TranslationalStiffness

from .schema_helper import SchemaHelper
from .models_impl import *


class Flexibility(Component):
    r"""
    A generic component representing a flexibility between two other nodes.  The proximal and distal nodes can have flexibility in up to six degrees of freedom.  The hinge is assumed to be rigid in any direction where the properties are not specified.
    
    Attributes
    ----------
    ComponentType : Literal['Flexibility'], default='Flexibility'
        Defines the specific type of Component model in use.  For a `Flexibility` object, this must always be set to a value of `Flexibility`.
    
    AlongX : TranslationalStiffness
    
    AlongY : TranslationalStiffness
    
    AlongZ : TranslationalStiffness
    
    AboutX : RotationalStiffness
    
    AboutY : RotationalStiffness
    
    AboutZ : RotationalStiffness
    
    Notes
    -----
    
    """
    ComponentType: Literal['Flexibility'] = Field(alias="ComponentType", default='Flexibility', allow_mutation=False, const=True) # type: ignore
    AlongX: TranslationalStiffness = Field(alias="AlongX", default=None)
    AlongY: TranslationalStiffness = Field(alias="AlongY", default=None)
    AlongZ: TranslationalStiffness = Field(alias="AlongZ", default=None)
    AboutX: RotationalStiffness = Field(alias="AboutX", default=None)
    AboutY: RotationalStiffness = Field(alias="AboutY", default=None)
    AboutZ: RotationalStiffness = Field(alias="AboutZ", default=None)

    _relative_schema_path = 'Components/Flexibility.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'ComponentType').merge(Component._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


Flexibility.update_forward_refs()
