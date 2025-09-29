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


class MassProperties(BladedModel):
    r"""
    The mass properties of the cross-section, expressed per unit length where appropriate.  These are defined in the PrincipalInertiaCoordinateSystem.
    
    Attributes
    ----------
    MassPerUnitLength : float
        The mass per unit length.
    
    PolarMassMomentOfInertia : float
        The polar mass moment of inertia per unit length at the mass centre, as defined by the PrincipalInertiaCoordinateSystem.
    
    RadiusOfGyrationRatio : float
        The ratio of the radius of gyration along the principal inertia Y-axis divided by the radius of gyration in the principal inertia X-axis, as defined by the PrincipalInertiaCoordinateSystem.
    
    Notes
    -----
    
    """
    MassPerUnitLength: float = Field(alias="MassPerUnitLength", default=None)
    PolarMassMomentOfInertia: float = Field(alias="PolarMassMomentOfInertia", default=None)
    RadiusOfGyrationRatio: float = Field(alias="RadiusOfGyrationRatio", default=None)

    _relative_schema_path = 'Components/Blade/CrossSection/MassProperties/MassProperties.json'
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


MassProperties.update_forward_refs()
