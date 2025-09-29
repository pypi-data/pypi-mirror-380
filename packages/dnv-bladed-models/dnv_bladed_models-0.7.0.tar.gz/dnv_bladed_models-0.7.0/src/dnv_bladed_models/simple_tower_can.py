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
from dnv_bladed_models.tower_can import TowerCan
from dnv_bladed_models.tower_can_properties_by_material import TowerCanPropertiesByMaterial
from dnv_bladed_models.tower_can_properties_by_material_where_different import TowerCanPropertiesByMaterialWhereDifferent

from .schema_helper import SchemaHelper
from .models_impl import *


class SimpleTowerCan(TowerCan):
    r"""
    A tower can where the structural properties will be calculated from the material properties and geometry of the can.
    
    Attributes
    ----------
    TowerCanType : Literal['SimpleTowerCan'], default='SimpleTowerCan'
        Defines the specific type of TowerCan model in use.  For a `SimpleTowerCan` object, this must always be set to a value of `SimpleTowerCan`.
    
    Material : str, regex=^TowerMaterialsLibrary.(.+)$
        A reference to a material in the tower's material library, using the key of the TowerMaterial in the Tower MaterialsLibrary.  i.e. `MaterialsLibrary.<material-key>`
    
    BaseCrossSection : TowerCanPropertiesByMaterial
    
    TopCrossSection : TowerCanPropertiesByMaterialWhereDifferent
    
    Notes
    -----
    
    """
    TowerCanType: Literal['SimpleTowerCan'] = Field(alias="TowerCanType", default='SimpleTowerCan', allow_mutation=False, const=True) # type: ignore
    Material: str = Field(alias="@Material", default=None, regex='^TowerMaterialsLibrary.(.+)$')
    BaseCrossSection: TowerCanPropertiesByMaterial = Field(alias="BaseCrossSection", default=None)
    TopCrossSection: TowerCanPropertiesByMaterialWhereDifferent = Field(alias="TopCrossSection", default=None)

    _relative_schema_path = 'Components/Tower/TowerCan/SimpleTowerCan.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'TowerCanType').merge(TowerCan._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


SimpleTowerCan.update_forward_refs()
