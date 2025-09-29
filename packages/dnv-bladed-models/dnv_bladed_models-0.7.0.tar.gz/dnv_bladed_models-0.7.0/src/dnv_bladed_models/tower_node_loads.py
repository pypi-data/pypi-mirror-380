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


class TowerNodeLoads(BladedModel):
    r"""
    The moments and forces to output for any node location where the loads are requested.
    
    Not supported yet.
    
    Attributes
    ----------
    Mx : bool, default=False, Not supported yet
        If true, the moment about the x-axis will be output.
    
    My : bool, default=False, Not supported yet
        If true, the moment about the y-axis will be output.
    
    Mz : bool, default=False, Not supported yet
        If true, the moment about the z-axis will be output.
    
    Mxy : bool, Not supported yet
        If true, the maximum moment about any axis that lies in the XY plane will be output.
    
    Fx : bool, default=False, Not supported yet
        If true, the force in the X direction will be output.
    
    Fy : bool, default=False, Not supported yet
        If true, the force in the Y direction will be output.
    
    Fz : bool, default=False, Not supported yet
        If true, the force in the Z direction will be output.
    
    Fxy : bool, Not supported yet
        If true, the maximum force along any axis that lies in the XY plane will be output.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    Mx: bool = Field(alias="Mx", default=None) # Not supported yet
    My: bool = Field(alias="My", default=None) # Not supported yet
    Mz: bool = Field(alias="Mz", default=None) # Not supported yet
    Mxy: bool = Field(alias="Mxy", default=None) # Not supported yet
    Fx: bool = Field(alias="Fx", default=None) # Not supported yet
    Fy: bool = Field(alias="Fy", default=None) # Not supported yet
    Fz: bool = Field(alias="Fz", default=None) # Not supported yet
    Fxy: bool = Field(alias="Fxy", default=None) # Not supported yet

    _relative_schema_path = 'Components/Tower/TowerOutputGroupLibrary/TowerOutputGroup/TowerNodeLoads/TowerNodeLoads.json'
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


TowerNodeLoads.update_forward_refs()
