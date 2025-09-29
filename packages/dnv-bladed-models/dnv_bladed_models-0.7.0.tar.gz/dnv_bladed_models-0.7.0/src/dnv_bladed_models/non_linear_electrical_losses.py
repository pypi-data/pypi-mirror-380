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
from dnv_bladed_models.electrical_losses import ElectricalLosses
from dnv_bladed_models.input_power_vs_loss import InputPowerVsLoss

from .schema_helper import SchemaHelper
from .models_impl import *


class NonLinearElectricalLosses(ElectricalLosses):
    r"""
    An electrical loss model where the losses are related to the power being generated, but is not linearly proportional to it.
    
    Attributes
    ----------
    ElectricalLossesType : Literal['NonLinearElectricalLosses'], default='NonLinearElectricalLosses'
        Defines the specific type of ElectricalLosses model in use.  For a `NonLinearElectricalLosses` object, this must always be set to a value of `NonLinearElectricalLosses`.
    
    InputPowerVsLoss : List[InputPowerVsLoss]
        A list of points in a look-up table specifying the relationship between the power and the corresponding losses.
    
    Notes
    -----
    
    """
    ElectricalLossesType: Literal['NonLinearElectricalLosses'] = Field(alias="ElectricalLossesType", default='NonLinearElectricalLosses', allow_mutation=False, const=True) # type: ignore
    InputPowerVsLoss: List[InputPowerVsLoss] = Field(alias="InputPowerVsLoss", default=list())

    _relative_schema_path = 'Components/Generator/ElectricalLosses/NonLinearElectricalLosses.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['InputPowerVsLoss',]),
        'ElectricalLossesType').merge(ElectricalLosses._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


NonLinearElectricalLosses.update_forward_refs()
