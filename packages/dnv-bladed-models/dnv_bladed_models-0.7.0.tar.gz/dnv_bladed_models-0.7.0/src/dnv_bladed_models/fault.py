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
from dnv_bladed_models.timed_event import TimedEvent

from .schema_helper import SchemaHelper
from .models_impl import *


class Fault(TimedEvent, ABC):
    r"""
    A fault which may occur during the simulation.  These can either be timed events, or based on a set of conditions which may or may not occur.
    
    Attributes
    ----------
    OnComponentInAssembly : str, regex=^Assembly.(.+)$
        A qualified, dot-separated path to a component in the assembly tree to which this applies.  i.e. `Assembly.<name1>.<name2>`
    
    Notes
    -----
    
    """
    OnComponentInAssembly: str = Field(alias="@OnComponentInAssembly", default=None, regex='^Assembly.(.+)$')

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(TimedEvent._type_info)


Fault.update_forward_refs()
