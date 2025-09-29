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
from dnv_bladed_models.tower_can_cross_section_properties import TowerCanCrossSectionProperties

from .schema_helper import SchemaHelper
from .models_impl import *


class TowerCanPropertiesByMaterial(TowerCanCrossSectionProperties):
    r"""
    The definition of a can cross-section where the material properties, the diameter, and the wall thickness will be used to calculate the structural properties.  Any properties which are omitted will be taken from the BaseCrossSection definition.
    
    Attributes
    ----------
    WallThickness : float
        The wall thickness of the can.
    
    Notes
    -----
    
    """
    WallThickness: float = Field(alias="WallThickness", default=None)

    _relative_schema_path = 'Components/Tower/TowerCan/TowerCanPropertiesByMaterial/TowerCanPropertiesByMaterial.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(TowerCanCrossSectionProperties._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


TowerCanPropertiesByMaterial.update_forward_refs()
