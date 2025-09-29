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
from dnv_bladed_models.hub import Hub
from dnv_bladed_models.rotor_imbalances import RotorImbalances

from .schema_helper import SchemaHelper
from .models_impl import *


class StandardHub(Hub, ABC):
    r"""
    The common properties of hubs with rotational symmetry and more than two blades.
    
    Attributes
    ----------
    NumberOfBlades : int
        The number of blades on the hub.
    
    Imbalances : RotorImbalances
    
    Notes
    -----
    
    """
    NumberOfBlades: int = Field(alias="NumberOfBlades", default=None)
    Imbalances: RotorImbalances = Field(alias="Imbalances", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(Hub._type_info)


StandardHub.update_forward_refs()
