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
from dnv_bladed_models.damper import Damper

from .schema_helper import SchemaHelper
from .models_impl import *


class ActiveDamper(Damper, ABC):
    r"""
    An active damper, applying a force which is specified by the controller.
    
    Not supported yet.
    
    Attributes
    ----------
    ForceLag : float, Not supported yet
        The force lag for the force signal's transfer function.
    
    AccelerationLag : float, Not supported yet
        The time lag for the acceleration signal's transfer function.
    
    ForceTransferFunction : float, Not supported yet
        Transfer function for active damper
    
    PerturbationForLinearisationCalculation : float, Not supported yet
        The perturbation step to use during linearisation calculation.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    ForceLag: float = Field(alias="ForceLag", default=None) # Not supported yet
    AccelerationLag: float = Field(alias="AccelerationLag", default=None) # Not supported yet
    ForceTransferFunction: float = Field(alias="ForceTransferFunction", default=None) # Not supported yet
    PerturbationForLinearisationCalculation: float = Field(alias="PerturbationForLinearisationCalculation", default=None) # Not supported yet

    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        None).merge(Damper._type_info)


ActiveDamper.update_forward_refs()
