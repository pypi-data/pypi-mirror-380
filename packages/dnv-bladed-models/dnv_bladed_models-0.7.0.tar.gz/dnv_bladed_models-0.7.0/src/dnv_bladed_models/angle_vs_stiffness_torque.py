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


class AngleVsStiffnessTorque(BladedModel):
    r"""
    A line or row in a look-up table, specifying a value of StiffnessTorque for a specified Angle.
    
    Not supported yet.
    
    Attributes
    ----------
    Angle : float, Not supported yet
        The angle of deflection of the pendulum from its resting position.
    
    StiffnessTorque : float, Not supported yet
        The opposing stiffness torque applicable at the corresponding angle of deflection.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    Angle: float = Field(alias="Angle", default=None) # Not supported yet
    StiffnessTorque: float = Field(alias="StiffnessTorque", default=None) # Not supported yet

    _relative_schema_path = 'Components/Damper/AngleVsStiffnessTorque/AngleVsStiffnessTorque.json'
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


AngleVsStiffnessTorque.update_forward_refs()
