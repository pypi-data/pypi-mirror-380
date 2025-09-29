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
from dnv_bladed_models.event import Event

from .schema_helper import SchemaHelper
from .models_impl import *


class TimedEvent(Event, ABC):
    r"""
    An event that occurs at a specified time in the simulation.
    
    Attributes
    ----------
    TimeOccurs : float
        The time at which the event occurs.  This is measured from the start of the output recording, and ignores any lead-in time.
    
    Notes
    -----
    
    """
    TimeOccurs: float = Field(alias="TimeOccurs", default=None)

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(Event._type_info)


TimedEvent.update_forward_refs()
