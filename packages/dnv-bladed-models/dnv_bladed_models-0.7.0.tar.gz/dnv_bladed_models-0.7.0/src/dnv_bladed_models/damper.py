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
from dnv_bladed_models.component import Component

from .schema_helper import SchemaHelper
from .models_impl import *


class Damper(Component, ABC):
    r"""
    The common properties of all support structure dampers.
    
    Not supported yet.
    
    Attributes
    ----------
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(Component._type_info)


Damper.update_forward_refs()
