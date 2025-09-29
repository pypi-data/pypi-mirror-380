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


class SelectedComponentOutputGroup(BladedModel):
    r"""
    A reference to the OutputGroup on a specific component within the assembly.
    
    Not supported yet.
    
    Attributes
    ----------
    ComponentWithinAssembly : str, regex=^Assembly.(.+)$, Not supported yet
        A qualified, dot-separated path to a component in the assembly tree.  e.g. `Assembly.Hub.PitchSystem1.Blade`
    
    SelectedOutputGroup : str, Not supported yet
        This is the name of the OutputGroup that should be used for the selected component, as defined in the OutputGroups library of the component's definition.
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    ComponentWithinAssembly: str = Field(alias="@ComponentWithinAssembly", default=None, regex='^Assembly.(.+)$') # Not supported yet
    SelectedOutputGroup: str = Field(alias="@SelectedOutputGroup", default=None) # Not supported yet

    _relative_schema_path = 'common/SelectedComponentOutputGroup.json'
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


SelectedComponentOutputGroup.update_forward_refs()
