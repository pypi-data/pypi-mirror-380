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


class WakePropertiesOfUpstreamTurbine(BladedModel):
    r"""
    
    
    Attributes
    ----------
    AerodynamicInformationResultsPath : str
        A file or URI containing aerodynamic information results, used to generate the initial wake profile of the upwind turbine
    
    SteadyOperationalLoadsResultsPath : str
        A file or URI containing aerodynamic information outputs from this 'Steady Operational Loads' run generates the initial wake profile of the upwind turbine. The steady operational loads run should be performed over all wind speeds and have aerodynamic information outputs switched on for blade 1 at all blade stations.
    
    Notes
    -----
    
    """
    AerodynamicInformationResultsPath: str = Field(alias="AerodynamicInformationResultsPath", default=None)
    SteadyOperationalLoadsResultsPath: str = Field(alias="SteadyOperationalLoadsResultsPath", default=None)

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/DynamicUpstreamWake/WakePropertiesOfUpstreamTurbine/WakePropertiesOfUpstreamTurbine.json'
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


WakePropertiesOfUpstreamTurbine.update_forward_refs()
