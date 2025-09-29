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


class AppliedMomentVsFrictionTorque(BladedModel):
    r"""
    A line or row in a look-up table, specifying a value of FrictionTorque for a specified AppliedMoment.
    
    Attributes
    ----------
    AppliedMoment : float
        The bending moment over the pitch system's main bearing.
    
    FrictionTorque : float
        The corresponding friction for the specified moment.
    
    Notes
    -----
    
    """
    AppliedMoment: float = Field(alias="AppliedMoment", default=None)
    FrictionTorque: float = Field(alias="FrictionTorque", default=None)

    _relative_schema_path = 'Components/PitchSystem/Friction/PitchBearingKineticFriction/PitchBearingFrictionXYMomentRelationship/AppliedMomentVsFrictionTorque/AppliedMomentVsFrictionTorque.json'
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


AppliedMomentVsFrictionTorque.update_forward_refs()
