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
from dnv_bladed_models.tower_can_cross_section_properties_where_different import TowerCanCrossSectionPropertiesWhereDifferent
from dnv_bladed_models.tower_can_torsional_properties import TowerCanTorsionalProperties

from .schema_helper import SchemaHelper
from .models_impl import *


class TowerCanPropertiesExplicitWhereDifferent(TowerCanCrossSectionPropertiesWhereDifferent):
    r"""
    The definition of a single tower can cross-section where any structural properties can be explicitly specified if they are different to those specified in the BaseCrossSection.
    
    Attributes
    ----------
    MassPerUnitLength : float
        The mass per unit length. If omitted, the value from the BaseCrossSection will be used.
    
    BendingStiffness : float
        The bending stiffness of the cross-section. If omitted, the value from the BaseCrossSection will be used.
    
    ShearStiffness : float
        The shear stiffness or shear modulus of the cross-section. If omitted, the value from the BaseCrossSection will be used.
    
    TorsionalProperties : TowerCanTorsionalProperties
    
    Notes
    -----
    
    """
    MassPerUnitLength: float = Field(alias="MassPerUnitLength", default=None)
    BendingStiffness: float = Field(alias="BendingStiffness", default=None)
    ShearStiffness: float = Field(alias="ShearStiffness", default=None)
    TorsionalProperties: TowerCanTorsionalProperties = Field(alias="TorsionalProperties", default=None)

    _relative_schema_path = 'Components/Tower/TowerCan/TowerCanPropertiesExplicitWhereDifferent/TowerCanPropertiesExplicitWhereDifferent.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(TowerCanCrossSectionPropertiesWhereDifferent._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


TowerCanPropertiesExplicitWhereDifferent.update_forward_refs()
