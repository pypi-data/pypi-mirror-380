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


class TowerShadowPowles(BladedModel):
    r"""
    Parameters for the empirical Powles tower shadow model. This implementation scales the wake width in proportion to the square root of the distance downstream.
    
    Attributes
    ----------
    ShadowWidthProportion : float, default=0
        The wake width as a proportion of the local obstruction's diameter.  The wake width is constant in the case of there being no downstream variation, but in the case of an inverse square variation, the wake width is applied at the reference length, \"Powles L Reference\" (the width at other points scaling in proporton to the square root of the distance downstream).
    
    MaximumDeficit : float, default=0
        The maximum deficit for use in the empirical Powles equation, expressed as a fraction of the unperturbed flow.
    
    LengthReference : float, default=0
        The distance downstream of the obstruction that the maximum deficit is applicable for, expressed as a multiple of the obstruction's diameter.
    
    Notes
    -----
    
    """
    ShadowWidthProportion: float = Field(alias="ShadowWidthProportion", default=None)
    MaximumDeficit: float = Field(alias="MaximumDeficit", default=None)
    LengthReference: float = Field(alias="LengthReference", default=None)

    _relative_schema_path = 'Components/Tower/TowerAerodynamicProperties/FlowObstruction/TowerShadowPowles/TowerShadowPowles.json'
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


TowerShadowPowles.update_forward_refs()
