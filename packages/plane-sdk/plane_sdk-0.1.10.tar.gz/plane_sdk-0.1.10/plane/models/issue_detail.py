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

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from plane.models.label import Label
from plane.models.priority_enum import PriorityEnum
from plane.models.user_lite import UserLite
from typing import Set
from typing_extensions import Self

class IssueDetail(BaseModel):
    """
    Comprehensive work item serializer with full relationship management.  Handles complete work item lifecycle including assignees, labels, validation, and related model updates. Supports dynamic field expansion and HTML content processing.
    """ # noqa: E501
    id: Optional[StrictStr] = None
    assignees: List[UserLite]
    labels: List[Label]
    type_id: Optional[StrictStr] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    point: Optional[Annotated[int, Field(le=12, strict=True, ge=0)]] = None
    name: Annotated[str, Field(strict=True, max_length=255)]
    description_html: Optional[StrictStr] = None
    description_stripped: Optional[StrictStr] = None
    description_binary: Optional[Union[StrictBytes, StrictStr]] = None
    priority: Optional[PriorityEnum] = None
    start_date: Optional[date] = None
    target_date: Optional[date] = None
    sequence_id: Optional[Annotated[int, Field(le=2147483647, strict=True, ge=-2147483648)]] = None
    sort_order: Optional[Union[StrictFloat, StrictInt]] = None
    completed_at: Optional[datetime] = None
    archived_at: Optional[date] = None
    is_draft: Optional[StrictBool] = None
    external_source: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    external_id: Optional[Annotated[str, Field(strict=True, max_length=255)]] = None
    created_by: Optional[StrictStr] = None
    updated_by: Optional[StrictStr] = None
    project: Optional[StrictStr] = None
    workspace: Optional[StrictStr] = None
    parent: Optional[StrictStr] = None
    state: Optional[StrictStr] = None
    estimate_point: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "assignees", "labels", "type_id", "created_at", "updated_at", "deleted_at", "point", "name", "description_html", "description_stripped", "description_binary", "priority", "start_date", "target_date", "sequence_id", "sort_order", "completed_at", "archived_at", "is_draft", "external_source", "external_id", "created_by", "updated_by", "project", "workspace", "parent", "state", "estimate_point", "type"]

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
        """Create an instance of IssueDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "created_at",
            "updated_at",
            "description_binary",
            "updated_by",
            "project",
            "workspace",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in assignees (list)
        _items = []
        if self.assignees:
            for _item_assignees in self.assignees:
                if _item_assignees:
                    _items.append(_item_assignees.to_dict())
            _dict['assignees'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item_labels in self.labels:
                if _item_labels:
                    _items.append(_item_labels.to_dict())
            _dict['labels'] = _items
        # set to None if type_id (nullable) is None
        # and model_fields_set contains the field
        if self.type_id is None and "type_id" in self.model_fields_set:
            _dict['type_id'] = None

        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deleted_at'] = None

        # set to None if point (nullable) is None
        # and model_fields_set contains the field
        if self.point is None and "point" in self.model_fields_set:
            _dict['point'] = None

        # set to None if description_stripped (nullable) is None
        # and model_fields_set contains the field
        if self.description_stripped is None and "description_stripped" in self.model_fields_set:
            _dict['description_stripped'] = None

        # set to None if description_binary (nullable) is None
        # and model_fields_set contains the field
        if self.description_binary is None and "description_binary" in self.model_fields_set:
            _dict['description_binary'] = None

        # set to None if start_date (nullable) is None
        # and model_fields_set contains the field
        if self.start_date is None and "start_date" in self.model_fields_set:
            _dict['start_date'] = None

        # set to None if target_date (nullable) is None
        # and model_fields_set contains the field
        if self.target_date is None and "target_date" in self.model_fields_set:
            _dict['target_date'] = None

        # set to None if completed_at (nullable) is None
        # and model_fields_set contains the field
        if self.completed_at is None and "completed_at" in self.model_fields_set:
            _dict['completed_at'] = None

        # set to None if archived_at (nullable) is None
        # and model_fields_set contains the field
        if self.archived_at is None and "archived_at" in self.model_fields_set:
            _dict['archived_at'] = None

        # set to None if external_source (nullable) is None
        # and model_fields_set contains the field
        if self.external_source is None and "external_source" in self.model_fields_set:
            _dict['external_source'] = None

        # set to None if external_id (nullable) is None
        # and model_fields_set contains the field
        if self.external_id is None and "external_id" in self.model_fields_set:
            _dict['external_id'] = None

        # set to None if created_by (nullable) is None
        # and model_fields_set contains the field
        if self.created_by is None and "created_by" in self.model_fields_set:
            _dict['created_by'] = None

        # set to None if updated_by (nullable) is None
        # and model_fields_set contains the field
        if self.updated_by is None and "updated_by" in self.model_fields_set:
            _dict['updated_by'] = None

        # set to None if parent (nullable) is None
        # and model_fields_set contains the field
        if self.parent is None and "parent" in self.model_fields_set:
            _dict['parent'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if estimate_point (nullable) is None
        # and model_fields_set contains the field
        if self.estimate_point is None and "estimate_point" in self.model_fields_set:
            _dict['estimate_point'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IssueDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "assignees": [UserLite.from_dict(_item) for _item in obj["assignees"]] if obj.get("assignees") is not None else None,
            "labels": [Label.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "type_id": obj.get("type_id"),
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "deleted_at": obj.get("deleted_at"),
            "point": obj.get("point"),
            "name": obj.get("name"),
            "description_html": obj.get("description_html"),
            "description_stripped": obj.get("description_stripped"),
            "description_binary": obj.get("description_binary"),
            "priority": obj.get("priority"),
            "start_date": obj.get("start_date"),
            "target_date": obj.get("target_date"),
            "sequence_id": obj.get("sequence_id"),
            "sort_order": obj.get("sort_order"),
            "completed_at": obj.get("completed_at"),
            "archived_at": obj.get("archived_at"),
            "is_draft": obj.get("is_draft"),
            "external_source": obj.get("external_source"),
            "external_id": obj.get("external_id"),
            "created_by": obj.get("created_by"),
            "updated_by": obj.get("updated_by"),
            "project": obj.get("project"),
            "workspace": obj.get("workspace"),
            "parent": obj.get("parent"),
            "state": obj.get("state"),
            "estimate_point": obj.get("estimate_point"),
            "type": obj.get("type")
        })
        return _obj


