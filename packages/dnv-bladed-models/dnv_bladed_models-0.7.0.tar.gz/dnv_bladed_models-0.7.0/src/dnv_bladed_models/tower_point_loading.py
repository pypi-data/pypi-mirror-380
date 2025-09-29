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
from dnv_bladed_models.support_structure_point_loading import SupportStructurePointLoading

from .schema_helper import SchemaHelper
from .models_impl import *


class TowerPointLoading(SupportStructurePointLoading):
    r"""
    A time history of point loading applied to an axisymmetric tower.
    
    Attributes
    ----------
    AppliedLoadType : Literal['TowerPointLoading'], default='TowerPointLoading'
        Defines the specific type of AppliedLoad model in use.  For a `TowerPointLoading` object, this must always be set to a value of `TowerPointLoading`.
    
    HeightOfImpact : float, default=0
        The height up the tower that the force is to be applied, measured from the bottom of the tower component.
    
    Notes
    -----
    
    """
    AppliedLoadType: Literal['TowerPointLoading'] = Field(alias="AppliedLoadType", default='TowerPointLoading', allow_mutation=False, const=True) # type: ignore
    HeightOfImpact: float = Field(alias="HeightOfImpact", default=None)

    _relative_schema_path = 'TimeDomainSimulation/AppliedLoad/TowerPointLoading.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'AppliedLoadType').merge(SupportStructurePointLoading._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


TowerPointLoading.update_forward_refs()
