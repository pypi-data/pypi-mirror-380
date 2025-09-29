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
from dnv_bladed_models.bending_torsion_coupling_terms_about_elastic_xy import BendingTorsionCouplingTermsAboutElasticXY
from dnv_bladed_models.bladed_model import BladedModel
from dnv_bladed_models.shear_stiffnesses_along_elastic_xy import ShearStiffnessesAlongElasticXY

from .schema_helper import SchemaHelper
from .models_impl import *


class StiffnessProperties(BladedModel):
    r"""
    The stiffness properties of the blade cross-section. All properties, except for torsional stiffness, are defined in the PrincipalElasticCoordinateSystem. Torsional stiffness is defined in the PrincipalShearCoordinateSystem.
    
    Attributes
    ----------
    BendingStiffnessAboutElasticX : float
        The bending stiffness about the principal elastic X-axis, as defined by the PrincipalElasticCoordinateSystem.
    
    BendingStiffnessAboutElasticY : float
        The bending stiffness about the principal elastic Y-axis, as defined by the PrincipalElasticCoordinateSystem.
    
    TorsionalStiffnessAboutShearZ : float
        The torsional stiffness about the principal shear Z-axis (shear centre), as defined by the PrincipalShearCoordinateSystem.
    
    AxialStiffness : float
        The axial stiffness, perpendicular to the principal elastic Z-axis (elastic centre), as defined by the PrincipalElasticCoordinateSystem.
    
    ShearStiffnessesAlongElasticXY : ShearStiffnessesAlongElasticXY
    
    BendingTorsionCouplingTermsAboutElasticXY : BendingTorsionCouplingTermsAboutElasticXY
    
    Notes
    -----
    
    """
    BendingStiffnessAboutElasticX: float = Field(alias="BendingStiffnessAboutElasticX", default=None)
    BendingStiffnessAboutElasticY: float = Field(alias="BendingStiffnessAboutElasticY", default=None)
    TorsionalStiffnessAboutShearZ: float = Field(alias="TorsionalStiffnessAboutShearZ", default=None)
    AxialStiffness: float = Field(alias="AxialStiffness", default=None)
    ShearStiffnessesAlongElasticXY: ShearStiffnessesAlongElasticXY = Field(alias="ShearStiffnessesAlongElasticXY", default=None)
    BendingTorsionCouplingTermsAboutElasticXY: BendingTorsionCouplingTermsAboutElasticXY = Field(alias="BendingTorsionCouplingTermsAboutElasticXY", default=None)

    _relative_schema_path = 'Components/Blade/CrossSection/StiffnessProperties/StiffnessProperties.json'
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


StiffnessProperties.update_forward_refs()
