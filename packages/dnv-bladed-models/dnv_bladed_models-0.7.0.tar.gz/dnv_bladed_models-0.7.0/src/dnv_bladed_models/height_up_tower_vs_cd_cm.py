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


class HeightUpTowerVsCdCm(BladedModel):
    r"""
    A look-up table for the hydrodynamic properties of the tower at different heights.
    
    Not supported yet.
    
    Attributes
    ----------
    HeightUpTower : float, Not supported yet
        The height measured from the bottom of the tower, assuming that the tower is mounted vertically.
    
    Cd : float, Not supported yet
        The coefficient of drag at the specified height.
    
    Cm : float, Not supported yet
        The coefficient of added mass for the tower.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    HeightUpTower: float = Field(alias="HeightUpTower", default=None) # Not supported yet
    Cd: float = Field(alias="Cd", default=None) # Not supported yet
    Cm: float = Field(alias="Cm", default=None) # Not supported yet

    _relative_schema_path = 'Components/Tower/TowerHydrodynamicProperties/HeightUpTowerVsCdCm/HeightUpTowerVsCdCm.json'
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


HeightUpTowerVsCdCm.update_forward_refs()
