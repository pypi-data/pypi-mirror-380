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
from dnv_bladed_models.damper import Damper
from dnv_bladed_models.vector3_d import Vector3D

from .schema_helper import SchemaHelper
from .models_impl import *


class LinearPassiveDamper(Damper):
    r"""
    A linear vibration damper to add to the support structure.
    
    Not supported yet.
    
    Attributes
    ----------
    ComponentType : Literal['LinearPassiveDamper'], default='LinearPassiveDamper', Not supported yet
        Defines the specific type of Component model in use.  For a `LinearPassiveDamper` object, this must always be set to a value of `LinearPassiveDamper`.
    
    Mass : float, Not supported yet
        The active mass of the vibration damper.
    
    Frequency : float, Not supported yet
        The peak frequency which the vibration damper responds to.
    
    Damping : float, Not supported yet
        The fraction of critical damping that the vibration damper will achive.
    
    IgnoreInModalAnalysis : bool, Not supported yet
        If true, the damper will be ignored in modal analyses.
    
    Direction : Vector3D
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    ComponentType: Literal['LinearPassiveDamper'] = Field(alias="ComponentType", default='LinearPassiveDamper', allow_mutation=False, const=True) # Not supported yet # type: ignore
    Mass: float = Field(alias="Mass", default=None) # Not supported yet
    Frequency: float = Field(alias="Frequency", default=None) # Not supported yet
    Damping: float = Field(alias="Damping", default=None) # Not supported yet
    IgnoreInModalAnalysis: bool = Field(alias="IgnoreInModalAnalysis", default=None) # Not supported yet
    Direction: Vector3D = Field(alias="Direction", default=None)

    _relative_schema_path = 'Components/Damper/LinearPassiveDamper.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'ComponentType').merge(Damper._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


LinearPassiveDamper.update_forward_refs()
