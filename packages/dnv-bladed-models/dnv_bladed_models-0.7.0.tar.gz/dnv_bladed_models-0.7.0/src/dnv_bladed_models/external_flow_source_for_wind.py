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
from dnv_bladed_models.wind import Wind

from .schema_helper import SchemaHelper
from .models_impl import *


class ExternalFlowSourceForWind(Wind):
    r"""
    The definition of a wind field that is provided by an external library - a dynamic link library (dll) on Windows, or a shared object (so) on Linux.
    
    Attributes
    ----------
    WindType : Literal['ExternalFlowSourceForWind'], default='ExternalFlowSourceForWind'
        Defines the specific type of Wind model in use.  For a `ExternalFlowSourceForWind` object, this must always be set to a value of `ExternalFlowSourceForWind`.
    
    LibraryFilepath : str
        The filepath of the external library object.
    
    ParametersAsString : str
        A string that will be passed to the external wind module.
    
    ParametersAsJson : Dict[str, Any]
        A JSON object that will be serialised as a string and passed to the external wind module.
    
    Notes
    -----
    
    """
    WindType: Literal['ExternalFlowSourceForWind'] = Field(alias="WindType", default='ExternalFlowSourceForWind', allow_mutation=False, const=True) # type: ignore
    LibraryFilepath: str = Field(alias="LibraryFilepath", default=None)
    ParametersAsString: str = Field(alias="ParametersAsString", default=None)
    ParametersAsJson: Dict[str, Any] = Field(alias="ParametersAsJson", default=None)

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/ExternalFlowSourceForWind.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'WindType').merge(Wind._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


ExternalFlowSourceForWind.update_forward_refs()
