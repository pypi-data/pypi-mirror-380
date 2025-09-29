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
from dnv_bladed_models.tower_can_cross_section_with_sensors import TowerCanCrossSectionWithSensors

from .schema_helper import SchemaHelper
from .models_impl import *


class TowerCanCrossSectionProperties(TowerCanCrossSectionWithSensors, ABC):
    r"""
    The definition of a can cross-section where the material properties, the diameter, and the wall thickness will be used to calculate the structural properties.  Any properties which are omitted will be taken from the BaseCrossSection definition.
    
    Attributes
    ----------
    OutsideDiameter : float
        The external diameter of the can cross-section.
    
    Notes
    -----
    
    """
    OutsideDiameter: float = Field(alias="OutsideDiameter", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(TowerCanCrossSectionWithSensors._type_info)


TowerCanCrossSectionProperties.update_forward_refs()
