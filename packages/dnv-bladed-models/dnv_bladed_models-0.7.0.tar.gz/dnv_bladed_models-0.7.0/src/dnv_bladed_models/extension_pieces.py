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


class ExtensionPieces(BladedModel):
    r"""
    The (typically cylindrical) extension connecting the pitch drive to the blade root.  These can be provided if the drag on this part of the hub needs to be modelled.
    
    Attributes
    ----------
    ExtensionPieceDiameter : float
        The diameter of the (typically cylindrical) extension piece.
    
    CoefficientOfDrag : float
        The coefficient of drag for the extension piece.
    
    Notes
    -----
    
    """
    ExtensionPieceDiameter: float = Field(alias="ExtensionPieceDiameter", default=None)
    CoefficientOfDrag: float = Field(alias="CoefficientOfDrag", default=None)

    _relative_schema_path = 'Components/Hub/ExtensionPieces/ExtensionPieces.json'
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


ExtensionPieces.update_forward_refs()
