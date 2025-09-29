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


class ExternalModule(BladedModel):
    r"""
    A specialised External Module component.  This is in the form of an external library (a dynamic link library on Windows, or a shared object on Linux).  This acts as a component in the Bladed assembly, and creates multibody objects to attach to the previous component.
    
    Attributes
    ----------
    Filepath : str
        The absolute filepath to the dynamic linked library (Windows) or the shared object (Linux).
    
    ParametersAsString : str
        A string that will be passed to the external module.
    
    ParametersAsJson : Dict[str, Any]
        A JSON object that will be serialised as a string and passed to the external module.
    
    Notes
    -----
    
    """
    Filepath: str = Field(alias="Filepath", default=None)
    ParametersAsString: str = Field(alias="ParametersAsString", default=None)
    ParametersAsJson: Dict[str, Any] = Field(alias="ParametersAsJson", default=None)

    _relative_schema_path = 'common/ExternalModule.json'
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


ExternalModule.update_forward_refs()
