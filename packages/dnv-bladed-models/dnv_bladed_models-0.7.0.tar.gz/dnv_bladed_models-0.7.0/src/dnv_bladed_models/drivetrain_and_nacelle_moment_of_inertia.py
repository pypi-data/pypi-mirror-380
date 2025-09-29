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


class DrivetrainAndNacelleMomentOfInertia(BladedModel):
    r"""
    The total moment of inertias of the nacelle and all of its contents, such as the generator or drivetrain.
    
    Attributes
    ----------
    Yawing : float
        The total moment of inertia about the nacelle component's z-axis (yawing) of the nacelle and all of its contents, such as the generator or drivetrain.
    
    Nodding : float
        The total moment of inertia about the nacelle component's y-axis (nodding) of the nacelle and all of its contents, such as the generator or drivetrain.
    
    Rolling : float
        The total moment of inertia about the nacelle component's x-axis (rolling) of the nacelle and all of its contents, such as the generator or drivetrain.
    
    Notes
    -----
    
    """
    Yawing: float = Field(alias="Yawing", default=None)
    Nodding: float = Field(alias="Nodding", default=None)
    Rolling: float = Field(alias="Rolling", default=None)

    _relative_schema_path = 'Components/DrivetrainAndNacelle/DrivetrainAndNacelleMassProperties/DrivetrainAndNacelleMomentOfInertia/DrivetrainAndNacelleMomentOfInertia.json'
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


DrivetrainAndNacelleMomentOfInertia.update_forward_refs()
