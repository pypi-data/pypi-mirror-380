# *********************************************************************#
# Bladed Python Models API                                             #
# Copyright (c) DNV Services UK Limited (c) 2025. All rights reserved. #
# MIT License (see license file)                                       #
# *********************************************************************#


# coding: utf-8

from __future__ import annotations

from abc import ABC

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
from dnv_bladed_models.modal_structural_modelling import ModalStructuralModelling
from dnv_bladed_models.rigid_structural_modelling import RigidStructuralModelling
from dnv_bladed_models.structural_modelling import StructuralModelling
from dnv_bladed_models.structural_modelling_insert import StructuralModellingInsert

from .schema_helper import SchemaHelper
from .models_impl import *

TStructuralModellingOptions = TypeVar('TStructuralModellingOptions', StructuralModellingInsert, ModalStructuralModelling, RigidStructuralModelling, StructuralModelling, )

class FlexBody(Component, ABC):
    r"""
    The common properties of components modelled using multibody flex bodies.
    
    Attributes
    ----------
    Modelling : Union[StructuralModellingInsert, ModalStructuralModelling, RigidStructuralModelling]
    
    Notes
    -----
    
    """
    Modelling: Union[StructuralModellingInsert, ModalStructuralModelling, RigidStructuralModelling] = Field(alias="Modelling", default=None, discriminator='StructuralModellingType')

    _type_info = TypeInfo(
        set([('Modelling', 'StructuralModellingType'),]),
        set([]),
        set([]),
        None).merge(Component._type_info)


    @property
    def Modelling_as_ModalStructuralModelling(self) -> ModalStructuralModelling:
        """
        Retrieves the value of Modelling guaranteeing it is a ModalStructuralModelling; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        ModalStructuralModelling
            A model object, guaranteed to be a ModalStructuralModelling.

        Raises
        ------
        TypeError
            If the value is not a ModalStructuralModelling.
        """
        return self.Modelling_as(ModalStructuralModelling)


    @property
    def Modelling_as_RigidStructuralModelling(self) -> RigidStructuralModelling:
        """
        Retrieves the value of Modelling guaranteeing it is a RigidStructuralModelling; if it is not, an error is raised.

        Useful when using type-checking development tools, as it provides a concise way to retrieve a value and assign a variable with the correct type.

        Returns
        -------
        RigidStructuralModelling
            A model object, guaranteed to be a RigidStructuralModelling.

        Raises
        ------
        TypeError
            If the value is not a RigidStructuralModelling.
        """
        return self.Modelling_as(RigidStructuralModelling)


    @property
    def Modelling_as_inline(self) -> Union[ModalStructuralModelling, RigidStructuralModelling]:
        """
        Retrieves the value of Modelling as a model object; if the value is specified with a '$insert', an error is raised.

        Returns
        -------
        Union[ModalStructuralModelling, RigidStructuralModelling]
            A model object at the specified index, guaranteed to not be a '$insert'.

        Raises
        ------
        TypeError
            If the value is not one of the concrete types of StructuralModelling; i.e. it is specified with a '$insert'.
        """
        if isinstance(self.Modelling, StructuralModellingInsert) or self.Modelling.is_insert:
            raise TypeError(f"Expected Modelling value to be an in-line object, but it is currently in the '$insert' state.")
        return self.Modelling


    def Modelling_as(self, cls: Type[TStructuralModellingOptions])-> TStructuralModellingOptions:
        """
        Retrieves the value of Modelling, ensuring it is of the specified type.
        The specified type must be one of the valid concrete types of StructuralModelling, or the '$insert' type
        (in the case the model is defined to be inserted from an external resource).

        Useful when using type-checking development tools, as it provides a concise way to access a value with the correct type.

        Parameters
        ----------
        cls: Type[Union[StructuralModellingInsert, ModalStructuralModelling, RigidStructuralModelling]]
            One of the valid concrete types of StructuralModelling, or the '$insert' type
            (in the case the model is defined to be inserted from an external resource).

        Returns
        -------
        TStructuralModellingOptions
            A model object of the specified type.

        Raises
        ------
        TypeError
            If the value is not of the specified type.

        Examples
        --------
        Get a reference to the value when it is one of the types of StructuralModelling:
        >>> val_obj = model_obj.Modelling_as(models.ModalStructuralModelling)
        >>> val_obj = model_obj.Modelling_as(models.RigidStructuralModelling)

        Get a reference to the value, when it was specified with a '$insert' and read in from a file:
        >>> insert_obj = model_obj.Modelling_as(models.StructuralModellingInsert)
        """
        if not isinstance(self.Modelling, cls):
            raise TypeError(f"Expected Modelling of type '{cls.__name__}' but was type '{type(self.Modelling).__name__}'")
        return self.Modelling


FlexBody.update_forward_refs()
