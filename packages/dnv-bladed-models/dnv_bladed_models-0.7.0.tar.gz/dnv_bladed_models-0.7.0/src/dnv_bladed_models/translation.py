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

from .schema_helper import SchemaHelper
from .models_impl import *


class Translation(Component):
    r"""
    An offset between two components, or the origin - [0,0,0] - and the first component in the Assembly tree.  This will be modelled as completely rigid.
    
    Attributes
    ----------
    ComponentType : Literal['Translation'], default='Translation'
        Defines the specific type of Component model in use.  For a `Translation` object, this must always be set to a value of `Translation`.
    
    X : float, default=0
        The translation in the X-direction of the previous component's distal frame of reference.  This will be in the global coordinate system if this is the first component in the Assembly tree.
    
    Y : float, default=0
        The translation in the Y-direction of the previous component's distal frame of reference.  This will be in the global coordinate system if this is the first component in the Assembly tree.
    
    Z : float, default=0
        The translation in the Z-direction of the previous component's distal frame of reference.  This will be in the global coordinate system if this is the first component in the Assembly tree.
    
    Notes
    -----
    
    """
    ComponentType: Literal['Translation'] = Field(alias="ComponentType", default='Translation', allow_mutation=False, const=True) # type: ignore
    X: float = Field(alias="X", default=None)
    Y: float = Field(alias="Y", default=None)
    Z: float = Field(alias="Z", default=None)

    _relative_schema_path = 'Components/Translation.json'
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


Translation.update_forward_refs()
