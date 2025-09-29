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
from dnv_bladed_models.friction_torque_vs_stiction_torque import FrictionTorqueVsStictionTorque

from .schema_helper import SchemaHelper
from .models_impl import *


class PitchBearingStiction(BladedModel):
    r"""
    The additional torque resisting the initial movement of the bearing.
    
    Attributes
    ----------
    ConstantStiction : float, default=0
        The stiction is the additional friction when the bearing is stationary (static friction = kinetic friction + stiction).
    
    StictionTorquePerUnitFrictionTorque : float
        A fixed ratio between the kinetic friction of the bearing and the stiction opposing the initial motion.
    
    FrictionTorqueVsStictionTorque : List[FrictionTorqueVsStictionTorque]
        A look-up table describing a non-linear relationship between the friction of the bearing and the corresponding stiction.
    
    Notes
    -----
    
    """
    ConstantStiction: float = Field(alias="ConstantStiction", default=None)
    StictionTorquePerUnitFrictionTorque: float = Field(alias="StictionTorquePerUnitFrictionTorque", default=None)
    FrictionTorqueVsStictionTorque: List[FrictionTorqueVsStictionTorque] = Field(alias="FrictionTorqueVsStictionTorque", default=list())

    _relative_schema_path = 'Components/PitchSystem/Friction/PitchBearingStiction/PitchBearingStiction.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['FrictionTorqueVsStictionTorque',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


PitchBearingStiction.update_forward_refs()
