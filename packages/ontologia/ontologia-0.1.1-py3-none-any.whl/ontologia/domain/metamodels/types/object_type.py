"""
object_type.py
-------------
This module defines the ObjectType model which represents object types
in the ontology. It manages property definitions and relationships
with other object types through link types.

Key Features:
- Object type metadata
- Property type management
- Link type relationships
- Validation and persistence
"""

from typing import List, Optional, Dict, Any, Union
from sqlmodel import Field, Relationship, Column, JSON
from pydantic import field_validator
from sqlalchemy.orm import Session

from registro import ResourceTypeBaseModel
from ontologia.domain.models.property_data_type import PropertyDataType

class ObjectType(ResourceTypeBaseModel, table=True):
    """
    Represents an object type in the ontology.
    Object types define the structure and relationships of objects.
    """
    __resource_type__ = "object-type"
    
    # Identity and metadata
    api_name: str = Field(index=True)
    display_name: str
    description: Optional[str] = None
    primary_key_field: str = Field(...)

    # Relationships
    property_types: List["PropertyType"] = Relationship(
        back_populates="object_type",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "lazy": "selectin"
        }
    )

    outgoing_link_types: List["LinkTypeSide"] = Relationship(
        back_populates="object_type",
        sa_relationship_kwargs={
            "cascade": "all, delete-orphan",
            "lazy": "selectin"
        }
    )

    @field_validator("property_types", check_fields=False)
    def validate_property_types(cls, v: List["PropertyType"], info: Any) -> List["PropertyType"]:
        """Validate property types and set their object_type_api_name."""
        if v is None:
            return []
        
        # Get the object type's api_name from the data
        api_name = info.data.get("api_name")
        if not api_name:
            raise ValueError("ObjectType must have an api_name")

        # Set object_type_api_name for each property
        for prop in v:
            prop.object_type_api_name = api_name
            # Ensure service and instance match parent
            prop.service = info.data.get("service")
            prop.instance = info.data.get("instance")
            # Set primary key flag if this property is the primary key
            if prop.api_name == info.data.get("primary_key_field"):
                prop.is_primary_key = True
                prop.required = True

        return v

    def get_property(self, api_name: str) -> Optional["PropertyType"]:
        """Get a property type by its API name."""
        return next(
            (prop for prop in self.property_types if prop.api_name == api_name),
            None
        )

    def set_properties(self, properties: List[Union[Dict[str, Any], "PropertyType"]], session: Session) -> None:
        """
        Set property types from a list of property definitions.
        Each property definition can be either:
        
        1. A dictionary containing:
           - api_name: str
           - display_name: str
           - data_type: PropertyDataType
           - is_primary_key: bool (optional)
           - required: bool (optional)
           - description: str (optional)
           
        2. A PropertyType instance with object_type_api_name set
        """
        from ontologia.domain.metamodels.types.property_type import PropertyType

        self.property_types = []
        for prop in properties:
            if isinstance(prop, dict):
                property_type = PropertyType(
                    service=self.service,
                    instance=self.instance,
                    api_name=prop["api_name"],
                    display_name=prop.get("display_name", prop["api_name"]),
                    description=prop.get("description"),
                    data_type=prop["data_type"],
                    is_primary_key=prop.get("is_primary_key", False) or prop["api_name"] == self.primary_key_field,
                    required=prop.get("required", False) or prop["api_name"] == self.primary_key_field,
                    object_type_api_name=self.api_name,
                    object_type_rid=self.rid if self.rid else None
                )
            else:
                property_type = prop
                if property_type.object_type_api_name != self.api_name:
                    raise ValueError(f"Property type '{property_type.api_name}' has incorrect object_type_api_name. Expected '{self.api_name}', got '{property_type.object_type_api_name}'")
                if property_type.api_name == self.primary_key_field:
                    property_type.is_primary_key = True
                    property_type.required = True
            property_type.link_object_type(session)
            if property_type not in session:
                session.add(property_type)
            self.property_types.append(property_type)

    @property
    def properties(self) -> List[Dict[str, Any]]:
        """
        Get properties as a list of dictionaries for backward compatibility.
        """
        return [prop.to_dict() for prop in self.property_types]

    def __repr__(self) -> str:
        return f"ObjectType(api_name='{self.api_name}', properties={len(self.property_types)})"

# Import at end to avoid circular imports
from ontologia.domain.metamodels.types.property_type import PropertyType
from ontologia.domain.metamodels.types.link_type import LinkTypeSide

ObjectType.model_rebuild()