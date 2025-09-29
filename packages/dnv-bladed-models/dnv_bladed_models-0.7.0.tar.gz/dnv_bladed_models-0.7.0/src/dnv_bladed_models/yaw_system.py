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
from dnv_bladed_models.component import Component
from dnv_bladed_models.yaw_actuation import YawActuation
from dnv_bladed_models.yaw_bearing import YawBearing
from dnv_bladed_models.yaw_system_connectable_nodes import YawSystemConnectableNodes
from dnv_bladed_models.yaw_system_output_group_library import YawSystemOutputGroupLibrary

from .schema_helper import SchemaHelper
from .models_impl import *


class YawSystem(Component):
    r"""
    A definition of the yaw bearing and any activation.
    
    Attributes
    ----------
    ComponentType : Literal['YawSystem'], default='YawSystem'
        Defines the specific type of Component model in use.  For a `YawSystem` object, this must always be set to a value of `YawSystem`.
    
    Bearing : YawBearing
    
    Actuation : YawActuation
    
    OutputGroups : YawSystemOutputGroupLibrary, Not supported yet
    
    ConnectableNodes : YawSystemConnectableNodes, Not supported yet
    
    Notes
    -----
    
    """
    ComponentType: Literal['YawSystem'] = Field(alias="ComponentType", default='YawSystem', allow_mutation=False, const=True) # type: ignore
    Bearing: YawBearing = Field(alias="Bearing", default=None)
    Actuation: YawActuation = Field(alias="Actuation", default=None)
    OutputGroups: YawSystemOutputGroupLibrary = Field(alias="OutputGroups", default=YawSystemOutputGroupLibrary()) # Not supported yet
    ConnectableNodes: YawSystemConnectableNodes = Field(alias="ConnectableNodes", default=YawSystemConnectableNodes()) # Not supported yet

    _relative_schema_path = 'Components/YawSystem/YawSystem.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['OutputGroups','ConnectableNodes',]),
        'ComponentType').merge(Component._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


YawSystem.update_forward_refs()
