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


class TowerNodeOutputs(BladedModel):
    r"""
    The outputs to produce for a specified node or node type.
    
    Not supported yet.
    
    Attributes
    ----------
    Displacements : bool, default=False, Not supported yet
        If true, the displacements of the nodes from their undeformed position will be output.
    
    Loads : bool, default=False, Not supported yet
        If true, the loads on the tower at the node's location will be output.
    
    WaterKinematics : bool, default=False, Not supported yet
        If true, the water velocities and accelerations at the node's location will be output.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    Displacements: bool = Field(alias="Displacements", default=None) # Not supported yet
    Loads: bool = Field(alias="Loads", default=None) # Not supported yet
    WaterKinematics: bool = Field(alias="WaterKinematics", default=None) # Not supported yet

    _relative_schema_path = 'Components/Tower/TowerOutputGroupLibrary/TowerOutputGroup/TowerNodeOutputs/TowerNodeOutputs.json'
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


TowerNodeOutputs.update_forward_refs()
