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


class IdealisedYawManoeuvre(BladedModel):
    r"""
    If provided, the controller will be ignored for this operation, and the yaw manoever will be performed at a constant rate.
    
    Not supported yet.
    
    Attributes
    ----------
    Rate : float, Not supported yet
        The rate at which the idealised yaw manoever will be preformed.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    Rate: float = Field(alias="Rate", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Event/IdealisedYawManoeuvre/IdealisedYawManoeuvre.json'
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


IdealisedYawManoeuvre.update_forward_refs()
