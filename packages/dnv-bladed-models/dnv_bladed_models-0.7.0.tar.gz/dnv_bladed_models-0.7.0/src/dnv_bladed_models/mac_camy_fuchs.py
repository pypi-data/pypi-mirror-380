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


class MacCamyFuchs(WaveDiffractionApproximation):
    r"""
    The MacCamy-Fuchs methodology will be used, with the member diameter automatically determined from the model.
    
    Not supported yet.
    
    Attributes
    ----------
    WaveDiffractionApproximationType : Literal['MacCamyFuchs'], default='MacCamyFuchs', Not supported yet
        Defines the specific type of WaveDiffractionApproximation model in use.  For a `MacCamyFuchs` object, this must always be set to a value of `MacCamyFuchs`.
    
    MemberDiameter : float, Not supported yet
        A representative member diameter used for MacCamy-Fuchs approximation.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    WaveDiffractionApproximationType: Literal['MacCamyFuchs'] = Field(alias="WaveDiffractionApproximationType", default='MacCamyFuchs', allow_mutation=False, const=True) # Not supported yet # type: ignore
    MemberDiameter: float = Field(alias="MemberDiameter", default=None) # Not supported yet

    _relative_schema_path = 'TimeDomainSimulation/Environment/SeaState/Waves/WaveDiffractionApproximation/MacCamyFuchs.json'
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


MacCamyFuchs.update_forward_refs()
