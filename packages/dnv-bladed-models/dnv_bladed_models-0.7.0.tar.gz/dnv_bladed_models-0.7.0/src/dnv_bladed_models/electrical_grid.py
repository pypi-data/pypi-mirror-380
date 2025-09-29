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
from dnv_bladed_models.grid_loss_energy_sink import GridLossEnergySink

from .schema_helper import SchemaHelper
from .models_impl import *


class ElectricalGrid(BladedModel):
    r"""
    The definition of the electrical grid that the turbine is connected to.
    
    Not supported yet.
    
    Attributes
    ----------
    NetworkVoltage : float, Not supported yet
        The voltage of the local network.
    
    ConnectingLineResistance : float, Not supported yet
        The resistance of the line that connects the turbine to the local network.
    
    ConnectingLineInductance : float, Not supported yet
        The inductance of the line that connects the turbine to the local network.
    
    NetworkResistance : float, Not supported yet
        The resistance of the network that the turbine is connected to.
    
    NetworkInductance : float, Not supported yet
        The inductance of the network that the turbine is connected to.
    
    NumberOfTurbinesOnFarm : int, Not supported yet
        The number of turbines on the farm that share the same grid connection.
    
    GridLossEnergySinks : List[GridLossEnergySink], Not supported yet
        A list of energy sinks available to the turbine.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    NetworkVoltage: float = Field(alias="NetworkVoltage", default=None) # Not supported yet
    ConnectingLineResistance: float = Field(alias="ConnectingLineResistance", default=None) # Not supported yet
    ConnectingLineInductance: float = Field(alias="ConnectingLineInductance", default=None) # Not supported yet
    NetworkResistance: float = Field(alias="NetworkResistance", default=None) # Not supported yet
    NetworkInductance: float = Field(alias="NetworkInductance", default=None) # Not supported yet
    NumberOfTurbinesOnFarm: int = Field(alias="NumberOfTurbinesOnFarm", default=None) # Not supported yet
    GridLossEnergySinks: List[GridLossEnergySink] = Field(alias="GridLossEnergySinks", default=list()) # Not supported yet

    _relative_schema_path = 'Turbine/ElectricalGrid/ElectricalGrid.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['GridLossEnergySinks',]),
        None).merge(BladedModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


ElectricalGrid.update_forward_refs()
