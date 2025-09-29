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


class DamperForceOrTorqueVsRate(BladedModel):
    r"""
    A line or row in a look-up table, specifying a value of Rate for a specified DamperForceOrTorque.
    
    Attributes
    ----------
    DamperForceOrTorque : float
        The torque or linear force applied by the damper for the corresponding rate.
    
    Rate : float
        The rate of the pitch bearing for which the torque or linear force will apply.
    
    Notes
    -----
    
    """
    DamperForceOrTorque: float = Field(alias="DamperForceOrTorque", default=None)
    Rate: float = Field(alias="Rate", default=None)

    _relative_schema_path = 'Components/PitchSystem/PitchController/PitchSafetySystem/DamperForceOrTorqueVsRate/DamperForceOrTorqueVsRate.json'
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


DamperForceOrTorqueVsRate.update_forward_refs()
