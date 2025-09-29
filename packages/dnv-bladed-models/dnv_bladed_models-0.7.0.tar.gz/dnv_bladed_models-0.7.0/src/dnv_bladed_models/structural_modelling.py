# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


# coding: utf-8

from __future__ import annotations

from abc import ABC

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
class StructuralModelling_StructuralModellingTypeEnum(str, Enum):
    MODAL_STRUCTURAL_MODELLING = "ModalStructuralModelling"
    RIGID_STRUCTURAL_MODELLING = "RigidStructuralModelling"
    INSERT = "Insert"
class StructuralModelling_GeometricStiffnessModelEnum(str, Enum):
    AXIAL_LOADS_ONLY = "AxialLoadsOnly"
    INTERNAL_LOADS_ONLY = "InternalLoadsOnly"
    DISABLED = "Disabled"

from .schema_helper import SchemaHelper
from .models_impl import *


class StructuralModelling(BladedModel, ABC):
    r"""
    The modelling options for a component with flexibility.  This is primarily the blade and the support structure.
    
    Attributes
    ----------
    StructuralModellingType : StructuralModelling_StructuralModellingTypeEnum
        Defines the specific type of model in use.
    
    MaximumNodeSpacing : float
        The maximum node spacing allowed on the component.  If any two nodes are further spaced apart than this, an additional node or nodes will be added inbetween them.  If omite, no additional nodes will be added.
    
    GeometricStiffnessModel : StructuralModelling_GeometricStiffnessModelEnum, default='AxialLoadsOnly'
        The geometric stiffness model to use for the support structure
    
    Notes
    -----
    
    This class is an abstraction, with the following concrete implementations:
        - StructuralModellingInsert
        - ModalStructuralModelling
        - RigidStructuralModelling
    
    """
    StructuralModellingType: StructuralModelling_StructuralModellingTypeEnum = Field(alias="StructuralModellingType", default=None)
    MaximumNodeSpacing: float = Field(alias="MaximumNodeSpacing", default=None)
    GeometricStiffnessModel: StructuralModelling_GeometricStiffnessModelEnum = Field(alias="GeometricStiffnessModel", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(BladedModel._type_info)


StructuralModelling.update_forward_refs()
