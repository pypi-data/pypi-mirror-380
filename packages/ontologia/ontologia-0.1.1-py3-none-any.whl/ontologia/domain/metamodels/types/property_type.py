"""
property_type.py
---------------
This module defines the PropertyType model which represents metadata about
properties in the ontology. It integrates with the data type system and
provides validation and persistence capabilities.

Key Features:
- Property metadata (name, description, etc.)
- Integration with data type system
- Validation rules (required, primary key)
- Relationship with ObjectType
- JSON serialization support
"""

from typing import Optional, Dict, Any, ClassVar
from sqlmodel import Field, Relationship, Column, JSON, Session, select
from pydantic import field_validator, model_validator

from registro import ResourceTypeBaseModel
from registro.config import settings
from ontologia.domain.models.property_data_type import (
    PropertyDataType,
    create_data_type,
    get_type_name,
    TYPE_REGISTRY
)

class PropertyType(ResourceTypeBaseModel, table=True):
    """
    Represents a property definition in the ontology.
    Properties belong to ObjectTypes and define their data structure.
    """
    __resource_type__ = "property-type"

    # Data type and validation
    data_type: str = Field(...)  # Store as string
    data_type_config: Dict[str, Any] = Field(default_factory=dict, sa_column=Column("data_type_config", JSON))
    description: Optional[str] = None
    
    is_primary_key: bool = False
    required: bool = False
    
    # Relationship with ObjectType
    object_type_rid: str = Field(foreign_key="objecttype.rid", index=True)
    object_type_api_name: str = Field(index=True)  # Added field for direct API name reference
    object_type: Optional["ObjectType"] = Relationship(
        back_populates="property_types",
        sa_relationship_kwargs={
            "cascade": "all, delete",
            "lazy": "selectin"
        }
    )

    # Class variable to store session for validation

    @model_validator(mode="before")
    def ensure_initial_values(cls, values: Dict[str, Any]):
        """
        Prepare/check input data, but do not perform any database lookups or mutations.
        Only ensure that if object_type_api_name is provided, it is non-empty.
        """
        if "object_type_api_name" in values and not values["object_type_api_name"]:
            raise ValueError("object_type_api_name must not be empty if provided.")
        # Do not attempt to resolve or mutate DB state here
        return values

    def _get_object_type_by_rid(self, session: Session) -> "ObjectType":
        """Internal method to get the object type by RID."""
        stmt = select(ObjectType).where(ObjectType.rid == self.object_type_rid)
        obj_type = session.exec(stmt).first()
        if not obj_type:
            raise ValueError(f"Object type with RID '{self.object_type_rid}' not found")
        return obj_type

    def _get_object_type_by_api_name(self, session: Session) -> "ObjectType":
        """Internal method to get the object type by api_name."""
        stmt = select(ObjectType).where(ObjectType.api_name == self.object_type_api_name)
        obj_type = session.exec(stmt).first()
        if not obj_type:
            raise ValueError(f"Object type with api_name '{self.object_type_api_name}' not found")
        return obj_type

    def link_object_type(self, session: Session) -> None:
        """
        Link this property to its object type.
        This should be called after the instance is created and before committing to the database.
        """
        # If object_type is already set, use it
        if self.object_type:
            # Ensure object_type_rid matches
            self.object_type_rid = self.object_type.rid
            # Ensure object_type_api_name matches
            self.object_type_api_name = self.object_type.api_name
            return

        # Try to get object type by RID first
        try:
            obj_type = self._get_object_type_by_rid(session)
            self.object_type = obj_type
            self.object_type_api_name = obj_type.api_name
            return
        except ValueError:
            # If that fails, try by api_name
            if self.object_type_api_name:
                obj_type = self._get_object_type_by_api_name(session)
                self.object_type = obj_type
                self.object_type_rid = obj_type.rid
                return
            
        # If we get here, we couldn't find the object type
        raise ValueError(f"Could not find object type for property '{self.api_name}'. Please provide either object_type_rid or object_type_api_name.")

    @field_validator("data_type")
    def validate_data_type(cls, v):
        """Validate data type name and ensure it exists in registry."""
        if v not in TYPE_REGISTRY:
            raise ValueError(f"Invalid data type: {v}. Must be one of: {', '.join(TYPE_REGISTRY.keys())}")
        return v

    @field_validator("data_type_config")
    def validate_data_type_config(cls, v, values):
        """Validate data type configuration."""
        if "data_type" in values:
            try:
                # Try to create the data type with the config to validate it
                create_data_type(values["data_type"], **v)
            except Exception as e:
                raise ValueError(f"Invalid data type configuration: {e}") from e
        return v

    @field_validator("object_type_api_name")
    def validate_object_type_api_name(cls, v):
        """Ensure object_type_api_name is a valid identifier."""
        if not v.isidentifier():
            raise ValueError("object_type_api_name must be a valid Python identifier")
        return v

    @field_validator("object_type", check_fields=False)
    def validate_object_type(cls, v, values):
        """Validate that if object_type is provided, it matches the api_name and rid."""
        if v is not None:
            # Check api_name if provided
            if "object_type_api_name" in values and values["object_type_api_name"]:
                if v.api_name != values["object_type_api_name"]:
                    raise ValueError(f"Provided object_type.api_name '{v.api_name}' does not match object_type_api_name '{values['object_type_api_name']}'")
            
            # Check rid if provided
            if "object_type_rid" in values and values["object_type_rid"]:
                if v.rid != values["object_type_rid"]:
                    raise ValueError(f"Provided object_type.rid '{v.rid}' does not match object_type_rid '{values['object_type_rid']}'")
        return v

    def get_data_type_instance(self) -> PropertyDataType:
        """Get the property data type instance."""
        return create_data_type(self.data_type, **self.data_type_config)

    def set_data_type_instance(self, value: PropertyDataType) -> None:
        """Set the data type from a PropertyDataType instance."""
        self.data_type = get_type_name(value)
        self.data_type_config = value.to_dict()
        # Remove type from config as it's stored separately
        self.data_type_config.pop("type", None)

    def to_dict(self) -> Dict[str, Any]:
        """Convert property type to a dictionary representation."""
        return {
            "api_name": self.api_name,
            "display_name": self.display_name,
            "description": self.description,
            "data_type": self.data_type,
            "data_type_config": self.data_type_config,
            "is_primary_key": self.is_primary_key,
            "required": self.required,
            "object_type_api_name": self.object_type_api_name,
            "object_type_rid": self.object_type_rid
        }

    def __repr__(self) -> str:
        return f"PropertyType(api_name='{self.api_name}', data_type={self.data_type}, object_type='{self.object_type_api_name}')"

# Import at end to avoid circular imports
from ontologia.domain.metamodels.types.object_type import ObjectType
PropertyType.model_rebuild()