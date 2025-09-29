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


class LowSpeedShaft(BladedModel):
    r"""
    The low speed shaft bending definition.
    
    Attributes
    ----------
    EffectiveShaftLength : float
        The length of the low speed shaft to be considered for the bending model, beginning at the outside face of the main bearing.
    
    HingePosition : float
        The fraction of the low speed shaft length (from the hub centre) where the hinge between the two massless rigid shafts are connected.
    
    TorsionalStiffness : float
        The shaft stiffness about the axis of rotation.
    
    TorsionalDamping : float
        The shaft damping about the axis of rotation.
    
    BendingStiffness : float
        The shaft's bending stiffness about any axis perpendicular to the axis of rotation.
    
    BendingDamping : float
        The shaft's bending damping about any axis perpendicular to the axis of rotation.
    
    Notes
    -----
    
    """
    EffectiveShaftLength: float = Field(alias="EffectiveShaftLength", default=None)
    HingePosition: float = Field(alias="HingePosition", default=None)
    TorsionalStiffness: float = Field(alias="TorsionalStiffness", default=None)
    TorsionalDamping: float = Field(alias="TorsionalDamping", default=None)
    BendingStiffness: float = Field(alias="BendingStiffness", default=None)
    BendingDamping: float = Field(alias="BendingDamping", default=None)

    _relative_schema_path = 'Components/DrivetrainAndNacelle/LowSpeedShaft/LowSpeedShaft.json'
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


LowSpeedShaft.update_forward_refs()
