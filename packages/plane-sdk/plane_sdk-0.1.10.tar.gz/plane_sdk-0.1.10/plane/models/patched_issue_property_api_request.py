# coding: utf-8

"""
    The Plane REST API

    The Plane REST API  Visit our quick start guide and full API documentation at [developers.plane.so](https://developers.plane.so/api-reference/introduction).

    The version of the API Spec: 0.0.2
    Contact: support@plane.so
    This class is auto generated.

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from plane.models.issue_property_api_relation_type_enum import IssuePropertyAPIRelationTypeEnum
from plane.models.property_type_enum import PropertyTypeEnum
from typing import Set
from typing_extensions import Self

class PatchedIssuePropertyAPIRequest(BaseModel):
    """
    PatchedIssuePropertyAPIRequest
    """ # noqa: E501
    relation_type: Optional[IssuePropertyAPIRelationTypeEnum] = None
    display_name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=255)]] = None
    description: Optional[StrictStr] = None
    property_type: Optional[PropertyTypeEnum] = None
    is_required: Optional[StrictBool] = None
    default_value: Optional[List[Annotated[str, Field(min_length=1, strict=True)]]] = None
    settings: Optional[Any] = None
    is_active: Optional[StrictBool] = None
    is_multi: Optional[StrictBool] = None
    validation_rules: Optional[Any] = None
    external_source: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    external_id: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    __properties: ClassVar[List[str]] = ["relation_type", "display_name", "description", "property_type", "is_required", "default_value", "settings", "is_active", "is_multi", "validation_rules", "external_source", "external_id"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PatchedIssuePropertyAPIRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if relation_type (nullable) is None
        # and model_fields_set contains the field
        if self.relation_type is None and "relation_type" in self.model_fields_set:
            _dict['relation_type'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if settings (nullable) is None
        # and model_fields_set contains the field
        if self.settings is None and "settings" in self.model_fields_set:
            _dict['settings'] = None

        # set to None if validation_rules (nullable) is None
        # and model_fields_set contains the field
        if self.validation_rules is None and "validation_rules" in self.model_fields_set:
            _dict['validation_rules'] = None

        # set to None if external_source (nullable) is None
        # and model_fields_set contains the field
        if self.external_source is None and "external_source" in self.model_fields_set:
            _dict['external_source'] = None

        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['external_id'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PatchedIssuePropertyAPIRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "relation_type": obj.get("relation_type"),
            "display_name": obj.get("display_name"),
            "description": obj.get("description"),
            "property_type": obj.get("property_type"),
            "is_required": obj.get("is_required"),
            "default_value": obj.get("default_value"),
            "settings": obj.get("settings"),
            "is_active": obj.get("is_active"),
            "is_multi": obj.get("is_multi"),
            "validation_rules": obj.get("validation_rules"),
            "external_source": obj.get("external_source"),
            "external_id": obj.get("external_id")
        })
        return _obj


