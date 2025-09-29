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
from dnv_bladed_models.wave_diffraction_approximation import WaveDiffractionApproximation

from .schema_helper import SchemaHelper
from .models_impl import *


class SimpleCutoffFrequency(WaveDiffractionApproximation):
    r"""
    The MacCamy-Fuchs methodology will be used, with the member diameter automatically determined from the model.
    
    Not supported yet.
    
    Attributes
    ----------
    WaveDiffractionApproximationType : Literal['SimpleCutoffFrequency'], default='SimpleCutoffFrequency', Not supported yet
        Defines the specific type of WaveDiffractionApproximation model in use.  For a `SimpleCutoffFrequency` object, this must always be set to a value of `SimpleCutoffFrequency`.
    
    CutoffFrequency : float, Not supported yet
        A threshold to cut off high frequency wave particle kinematics for calculating applied forces.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    WaveDiffractionApproximationType: Literal['SimpleCutoffFrequency'] = Field(alias="WaveDiffractionApproximationType", default='SimpleCutoffFrequency', allow_mutation=False, const=True) # Not supported yet # type: ignore
    CutoffFrequency: float = Field(alias="CutoffFrequency", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Waves/WaveDiffractionApproximation/SimpleCutoffFrequency.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'WaveDiffractionApproximationType').merge(WaveDiffractionApproximation._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


SimpleCutoffFrequency.update_forward_refs()
