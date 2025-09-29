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


class GridLossEnergySink(BladedModel):
    r"""
    An energy sink used to absorb the power from the generator in the case of a grid loss where generator braking is used.
    
    Not supported yet.
    
    Attributes
    ----------
    MaximumGeneratorTorque : float, default=0, Not supported yet
        The maximum generator torque while the energy sink is active after grid loss has occurred.  This limit is applied to generator torque demand in addition to the maximum torque demand specified in the generator model parameters.
    
    EnergyCapacityOfSink : float, default=0, Not supported yet
        The total generator mechanical input energy which can be absorbed before generator torque falls to zero following grid loss.  In a multi-rotor turbine, this is the energy capacity per rotor.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    MaximumGeneratorTorque: float = Field(alias="MaximumGeneratorTorque", default=None) # Not supported yet
    EnergyCapacityOfSink: float = Field(alias="EnergyCapacityOfSink", default=None) # Not supported yet

    _relative_schema_path = 'Turbine/ElectricalGrid/GridLossEnergySink/GridLossEnergySink.json'
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


GridLossEnergySink.update_forward_refs()
