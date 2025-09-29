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
from plane.models.cycle_lite import CycleLite
from plane.models.module_lite import ModuleLite
from plane.models.priority_enum import PriorityEnum
from plane.models.state_lite import StateLite
from typing import Set
from typing_extensions import Self

class IssueExpand(BaseModel):
    """
    Extended work item serializer with full relationship expansion.  Provides work items with expanded related data including cycles, modules, labels, assignees, and states for comprehensive data representation.
    """ # noqa: E501
    id: Optional[StrictStr] = None
    cycle: Optional[CycleLite] = None
    module: Optional[ModuleLite] = None
    labels: Optional[StrictStr] = None
    assignees: Optional[StrictStr] = None
    state: Optional[StateLite] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    deleted_at: Optional[datetime] = None
    point: Optional[Annotated[int, Field(le=12, strict=True, ge=0)]] = None
    name: Annotated[str, Field(strict=True, max_length=255)]
    description: Optional[Any] = None
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
    estimate_point: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["id", "cycle", "module", "labels", "assignees", "state", "created_at", "updated_at", "deleted_at", "point", "name", "description", "description_html", "description_stripped", "description_binary", "priority", "start_date", "target_date", "sequence_id", "sort_order", "completed_at", "archived_at", "is_draft", "external_source", "external_id", "created_by", "updated_by", "project", "workspace", "parent", "estimate_point", "type"]

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
        """Create an instance of IssueExpand from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "cycle",
            "module",
            "labels",
            "assignees",
            "state",
            "created_at",
            "updated_at",
            "description_binary",
            "created_by",
            "updated_by",
            "project",
            "workspace",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cycle
        if self.cycle:
            _dict['cycle'] = self.cycle.to_dict()
        # override the default output from pydantic by calling `to_dict()` of module
        if self.module:
            _dict['module'] = self.module.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deleted_at'] = None

        # set to None if point (nullable) is None
        # and model_fields_set contains the field
        if self.point is None and "point" in self.model_fields_set:
            _dict['point'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

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
        """Create an instance of IssueExpand from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "cycle": CycleLite.from_dict(obj["cycle"]) if obj.get("cycle") is not None else None,
            "module": ModuleLite.from_dict(obj["module"]) if obj.get("module") is not None else None,
            "labels": obj.get("labels"),
            "assignees": obj.get("assignees"),
            "state": StateLite.from_dict(obj["state"]) if obj.get("state") is not None else None,
            "created_at": obj.get("created_at"),
            "updated_at": obj.get("updated_at"),
            "deleted_at": obj.get("deleted_at"),
            "point": obj.get("point"),
            "name": obj.get("name"),
            "description": obj.get("description"),
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
            "estimate_point": obj.get("estimate_point"),
            "type": obj.get("type")
        })
        return _obj


