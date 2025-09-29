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
from dnv_bladed_models.component import Component
from dnv_bladed_models.interface_load_file import InterfaceLoadFile
from dnv_bladed_models.superelement_connectable_nodes import SuperelementConnectableNodes
class Superelement_WaveLoadingUnitsInFileEnum(str, Enum):
    N = "N"
    K_N = "kN"

from .schema_helper import SchemaHelper
from .models_impl import *


class Superelement(Component):
    r"""
    A structural superelement, mathematically representing a structural component.
    
    Not supported yet.
    
    Attributes
    ----------
    ComponentType : Literal['Superelement'], default='Superelement', Not supported yet
        Defines the specific type of Component model in use.  For a `Superelement` object, this must always be set to a value of `Superelement`.
    
    DefinitionFilepath : str, Not supported yet
        The filepath of URI to the superelement data.
    
    WaveLoadingFilepath : str, Not supported yet
        The filepath of URI to the accompanying wave data.
    
    WaveLoadingUnitsInFile : Superelement_WaveLoadingUnitsInFileEnum, default='kN', Not supported yet
        The units that were used when generating the wave load files.  The industry standard is to provide wave loads in kN and kNm.
    
    CoordinateTransformationMatrix : List[List[float]]
        A 6x6 matrix to transform one set of coordinates into another.
    
    InterfaceLoadFile : InterfaceLoadFile, Not supported yet
    
    ConnectableNodes : SuperelementConnectableNodes, Not supported yet
    
    Notes
    -----
    This model is not supported yet by the Bladed calculation engine.
    """
    ComponentType: Literal['Superelement'] = Field(alias="ComponentType", default='Superelement', allow_mutation=False, const=True) # Not supported yet # type: ignore
    DefinitionFilepath: str = Field(alias="DefinitionFilepath", default=None) # Not supported yet
    WaveLoadingFilepath: str = Field(alias="WaveLoadingFilepath", default=None) # Not supported yet
    WaveLoadingUnitsInFile: Superelement_WaveLoadingUnitsInFileEnum = Field(alias="WaveLoadingUnitsInFile", default=None) # Not supported yet
    CoordinateTransformationMatrix: List[List[float]] = Field(alias="CoordinateTransformationMatrix", default=list())
    InterfaceLoadFile: InterfaceLoadFile = Field(alias="InterfaceLoadFile", default=None) # Not supported yet
    ConnectableNodes: SuperelementConnectableNodes = Field(alias="ConnectableNodes", default=SuperelementConnectableNodes()) # Not supported yet

    _relative_schema_path = 'Components/Superelement/Superelement.json'
    _type_info = TypeInfo(
        set([]),
        set([]),
        set(['CoordinateTransformationMatrix','ConnectableNodes',]),
        'ComponentType').merge(Component._type_info)


    class Config:
        extra = Extra.forbid
        validate_assignment = True
        allow_population_by_field_name = True
        pass

    def _entity(self) -> bool:
        return True


Superelement.update_forward_refs()
