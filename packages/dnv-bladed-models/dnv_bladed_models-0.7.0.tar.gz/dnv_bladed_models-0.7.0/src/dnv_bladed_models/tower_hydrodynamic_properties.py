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
from dnv_bladed_models.height_up_tower_vs_cd_cm import HeightUpTowerVsCdCm

from .schema_helper import SchemaHelper
from .models_impl import *


class TowerHydrodynamicProperties(BladedModel):
    r"""
    The hydrodynamic properties of the tower, if fully or partly submerged in water.
    
    Not supported yet.
    
    Attributes
    ----------
    CoefficientOfDrag : float, default=1.12, Not supported yet
        The coefficient of drag for the entire tower.
    
    CoefficientOfMass : float, Not supported yet
        The coefficient of added mass for the tower.
    
    HeightUpTowerVsCdCm : List[HeightUpTowerVsCdCm], Not supported yet
        A look-up table for the hydrodynamic properties of the tower at different heights.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    CoefficientOfDrag: float = Field(alias="CoefficientOfDrag", default=None) # Not supported yet
    CoefficientOfMass: float = Field(alias="CoefficientOfMass", default=None) # Not supported yet
    HeightUpTowerVsCdCm: List[HeightUpTowerVsCdCm] = Field(alias="HeightUpTowerVsCdCm", default=list()) # Not supported yet

    _relative_schema_path = 'Components/Tower/TowerHydrodynamicProperties/TowerHydrodynamicProperties.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['HeightUpTowerVsCdCm',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


TowerHydrodynamicProperties.update_forward_refs()
