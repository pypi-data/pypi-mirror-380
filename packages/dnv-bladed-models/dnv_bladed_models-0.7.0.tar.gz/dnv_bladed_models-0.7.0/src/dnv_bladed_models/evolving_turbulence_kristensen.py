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
from dnv_bladed_models.evolving_turbulence import EvolvingTurbulence

from .schema_helper import SchemaHelper
from .models_impl import *


class EvolvingTurbulenceKristensen(EvolvingTurbulence):
    r"""
    The settings for Kristensen evolving turbulence.  In the case of a normal turbulent wind field, the turbulence is \"frozen\" and approaches the turbine at a constant block.  Although this doesn't match physical reality, it is a particular problem for Lidar - as it gives them a \"perfect\" insight into the oncoming wind field.  In order to represent the nature of real turbulence, a second turbulence file is superimposed on the windfield so that it \"evolves\" as it moves forward.  This is computationally expensive, and is usually applied only to the Lidar readings - although it can be applied to all the wind values in a simulation.
    
    Attributes
    ----------
    EvolvingTurbulenceType : Literal['EvolvingTurbulenceKristensen'], default='EvolvingTurbulenceKristensen'
        Defines the specific type of EvolvingTurbulence model in use.  For a `EvolvingTurbulenceKristensen` object, this must always be set to a value of `EvolvingTurbulenceKristensen`.
    
    Notes
    -----
    
    """
    EvolvingTurbulenceType: Literal['EvolvingTurbulenceKristensen'] = Field(alias="EvolvingTurbulenceType", default='EvolvingTurbulenceKristensen', allow_mutation=False, const=True) # type: ignore

    _relative_schema_path = 'TimeDomainSimulation/Environment/Wind/EvolvingTurbulence/EvolvingTurbulenceKristensen.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'EvolvingTurbulenceType').merge(EvolvingTurbulence._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


EvolvingTurbulenceKristensen.update_forward_refs()
