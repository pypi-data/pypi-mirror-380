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
from dnv_bladed_models.aerodynamic_model import AerodynamicModel
from dnv_bladed_models.blade_element_theory_corrections import BladeElementTheoryCorrections
from dnv_bladed_models.momentum_theory_corrections import MomentumTheoryCorrections

from .schema_helper import SchemaHelper
from .models_impl import *


class BladeElementMomentum(AerodynamicModel):
    r"""
    The Blade Element Momentum (BEM) theory model.
    
    Attributes
    ----------
    AerodynamicModelType : Literal['BladeElementMomentum'], default='BladeElementMomentum'
        Defines the specific type of AerodynamicModel model in use.  For a `BladeElementMomentum` object, this must always be set to a value of `BladeElementMomentum`.
    
    MomentumTheoryCorrections : MomentumTheoryCorrections
    
    BladeElementTheoryCorrections : BladeElementTheoryCorrections
    
    Notes
    -----
    
    """
    AerodynamicModelType: Literal['BladeElementMomentum'] = Field(alias="AerodynamicModelType", default='BladeElementMomentum', allow_mutation=False, const=True) # type: ignore
    MomentumTheoryCorrections: MomentumTheoryCorrections = Field(alias="MomentumTheoryCorrections", default=None)
    BladeElementTheoryCorrections: BladeElementTheoryCorrections = Field(alias="BladeElementTheoryCorrections", default=None)

    _relative_schema_path = 'Settings/AerodynamicSettings/AerodynamicModel/BladeElementMomentum.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set([]),
        'AerodynamicModelType').merge(AerodynamicModel._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


BladeElementMomentum.update_forward_refs()
