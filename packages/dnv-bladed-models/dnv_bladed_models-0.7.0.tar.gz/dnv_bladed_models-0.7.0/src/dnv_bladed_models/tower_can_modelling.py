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


class TowerCanModelling(BladedModel):
    r"""
    Parameters controlling the way the can will be modelled by Bladed.
    
    Attributes
    ----------
    MaximumNodeSpacing : float
        If any two nodes are further spaced apart than this, an additional node or nodes will be added equally spaced between them.  The default is infinity, meaning that no extra nodes will ever be added unless NumberOfIntermediateNodes has been specified.
    
    NumberOfIntermediateNodes : int, default=0
        The number of structural nodes to be added, equally spaced between the top and bottom of the can.  The default is 0, meaning that (unless the MaximumNodeSpacing requires additional nodes to be added) the can will be represented by a single beam.
    
    Notes
    -----
    
    """
    MaximumNodeSpacing: float = Field(alias="MaximumNodeSpacing", default=None)
    NumberOfIntermediateNodes: int = Field(alias="NumberOfIntermediateNodes", default=None)

    _relative_schema_path = 'Components/Tower/TowerCan/TowerCanModelling/TowerCanModelling.json'
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


TowerCanModelling.update_forward_refs()
