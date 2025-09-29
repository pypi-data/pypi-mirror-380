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
from dnv_bladed_models.nodes_at_heights import NodesAtHeights
from dnv_bladed_models.tower_node_loads import TowerNodeLoads
from dnv_bladed_models.tower_node_outputs import TowerNodeOutputs
class TowerOutputGroup_AxisSystemEnum(str, Enum):
    GLOBAL = "GLOBAL"

from .schema_helper import SchemaHelper
from .models_impl import *


class TowerOutputGroup(BladedModel):
    r"""
    A named tower output group.
    
    Not supported yet.
    
    Attributes
    ----------
    SelectedNodeLoads : TowerNodeLoads, Not supported yet
    
    AxisSystem : TowerOutputGroup_AxisSystemEnum, default='GLOBAL', Not supported yet
        The axis sytstem to be used for the outputs.
    
    AllConnectableNodes : TowerNodeOutputs, Not supported yet
    
    AllNodes : TowerNodeOutputs, Not supported yet
    
    NodesAtHeights : NodesAtHeights, Not supported yet
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    SelectedNodeLoads: TowerNodeLoads = Field(alias="SelectedNodeLoads", default=None) # Not supported yet
    AxisSystem: TowerOutputGroup_AxisSystemEnum = Field(alias="AxisSystem", default=None) # Not supported yet
    AllConnectableNodes: TowerNodeOutputs = Field(alias="AllConnectableNodes", default=None) # Not supported yet
    AllNodes: TowerNodeOutputs = Field(alias="AllNodes", default=None) # Not supported yet
    NodesAtHeights: NodesAtHeights = Field(alias="NodesAtHeights", default=NodesAtHeights()) # Not supported yet

    _relative_schema_path = 'Components/Tower/TowerOutputGroupLibrary/TowerOutputGroup/TowerOutputGroup.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['NodesAtHeights',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


TowerOutputGroup.update_forward_refs()
