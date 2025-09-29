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
from dnv_bladed_models.beddoes_leishman_model import BeddoesLeishmanModel

from .schema_helper import SchemaHelper
from .models_impl import *


class IncompressibleBeddoesLeishmanModel(BeddoesLeishmanModel):
    r"""
    The incompressible Beddoes Leishman dynamic stall model.
    
    Attributes
    ----------
    DynamicStallType : Literal['IncompressibleBeddoesLeishmanModel'], default='IncompressibleBeddoesLeishmanModel'
        Defines the specific type of DynamicStall model in use.  For a `IncompressibleBeddoesLeishmanModel` object, this must always be set to a value of `IncompressibleBeddoesLeishmanModel`.
    
    Notes
    -----
    
    """
    DynamicStallType: Literal['IncompressibleBeddoesLeishmanModel'] = Field(alias="DynamicStallType", default='IncompressibleBeddoesLeishmanModel', allow_mutation=False, const=True) # type: ignore

    _relative_schema_path = 'Settings/AerodynamicSettings/DynamicStall/IncompressibleBeddoesLeishmanModel.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'DynamicStallType').merge(BeddoesLeishmanModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


IncompressibleBeddoesLeishmanModel.update_forward_refs()
