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
from dnv_bladed_models.connectable_node import ConnectableNode

from .schema_helper import SchemaHelper
from .models_impl import *


class TowerConnectableNode(ConnectableNode):
    r"""
    The definition of a connectable node on a tower component.
    
    Not supported yet.
    
    Attributes
    ----------
    HeightUpTower : float, Not supported yet
        The height measured from the bottom of the tower, assuming that the tower is mounted vertically.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    HeightUpTower: float = Field(alias="HeightUpTower", default=None) # Not supported yet

    _relative_schema_path = 'Components/Tower/TowerConnectableNodes/TowerConnectableNode/TowerConnectableNode.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(ConnectableNode._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


TowerConnectableNode.update_forward_refs()
