from typing import Optional, Any, ClassVar, Dict
import enum
from sqlmodel import Field, Relationship, Session, select
from pydantic import field_validator, model_validator

from registro import ResourceTypeBaseModel
from registro.config import settings

class Cardinality(str, enum.Enum):
    ONE = "ONE"
    MANY = "MANY"

class LinkTypeSide(ResourceTypeBaseModel, table=True):
    """
    LinkTypeSide model representing one side of a link type in the ontology.
    
    Attributes:
        cardinality (Cardinality): The cardinality of this side of the link (ONE or MANY)
        object_type_api_name (str): The API name of the object type this side connects to
        target_object_type_api_name (str): The API name of the target object type
        foreign_key_property_api_name (Optional[str]): If provided, the API name of a property to use as foreign key
    """
    __resource_type__ = "link-type"
    
    cardinality: Cardinality = Field(...)
    object_type_api_name: str = Field(..., index=True)
    target_object_type_api_name: str = Field(..., index=True)
    foreign_key_property_api_name: Optional[str] = None
    object_type_rid: str = Field(foreign_key="objecttype.rid")
    object_type: Optional["ObjectType"] = Relationship(
        back_populates="outgoing_link_types",
        sa_relationship_kwargs={
            "primaryjoin": "foreign(LinkTypeSide.object_type_rid)==ObjectType.rid",
            "lazy": "joined"
        }
    )

    # Class variable to store session for validation

    @model_validator(mode="before")
    def ensure_initial_link_values(cls, values):
        """
        Prepare/check input data for LinkTypeSide, but do not perform any database lookups or mutations.
        Only ensure that if object_type_api_name or foreign_key_property_api_name are provided, they are non-empty.
        """
        if "object_type_api_name" in values and not values["object_type_api_name"]:
            raise ValueError("object_type_api_name must not be empty if provided.")
        if "foreign_key_property_api_name" in values and values["foreign_key_property_api_name"]:
            if not isinstance(values["foreign_key_property_api_name"], str) or not values["foreign_key_property_api_name"]:
                raise ValueError("foreign_key_property_api_name must not be empty if provided.")
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

    def _get_target_object_type(self, session: Session) -> "ObjectType":
        """Internal method to get the target object type by api_name."""
        stmt = select(ObjectType).where(ObjectType.api_name == self.target_object_type_api_name)
        obj_type = session.exec(stmt).first()
        if not obj_type:
            raise ValueError(f"Target object type with api_name '{self.target_object_type_api_name}' not found")
        return obj_type

    def _get_foreign_key_property(self, session: Session) -> Optional["PropertyType"]:
        """Internal method to get the foreign key property if specified."""
        if not self.foreign_key_property_api_name:
            return None
            
        from ontologia.domain.metamodels.types.property_type import PropertyType
        stmt = select(PropertyType).where(
            (PropertyType.object_type_rid == self.object_type_rid) &
            (PropertyType.api_name == self.foreign_key_property_api_name)
        )
        return session.exec(stmt).first()

    def _validate_object_type(self, obj_type: "ObjectType") -> None:
        """Internal method to validate an object type's primary key configuration."""
        if not obj_type.primary_key_field:
            raise ValueError(f"Object type '{obj_type.api_name}' must have a primary_key_field defined")

        primary_key_props = [p for p in obj_type.property_types if p.is_primary_key]
        if not primary_key_props:
            raise ValueError(f"Object type '{obj_type.api_name}' must have a property marked as primary key")
        if len(primary_key_props) > 1:
            raise ValueError(f"Object type '{obj_type.api_name}' has multiple properties marked as primary key")
        
        primary_key_prop = primary_key_props[0]
        if primary_key_prop.api_name != obj_type.primary_key_field:
            raise ValueError(f"Object type '{obj_type.api_name}' primary_key_field '{obj_type.primary_key_field}' does not match primary key property '{primary_key_prop.api_name}'")

    @field_validator("object_type_api_name")
    def validate_object_type_api_name(cls, v: str) -> str:
        """Validate object_type_api_name format."""
        if not v.isidentifier():
            raise ValueError("object_type_api_name must be a valid Python identifier")
        return v

    @field_validator("target_object_type_api_name")
    def validate_target_object_type_api_name(cls, v: str) -> str:
        """Validate target_object_type_api_name format."""
        if not v.isidentifier():
            raise ValueError("target_object_type_api_name must be a valid Python identifier")
        return v

    @field_validator("foreign_key_property_api_name")
    def validate_foreign_key_property_api_name(cls, v: Optional[str]) -> Optional[str]:
        """Validate foreign_key_property_api_name format if provided."""
        if v is not None and not v.isidentifier():
            raise ValueError("foreign_key_property_api_name must be a valid Python identifier")
        return v

    @field_validator("object_type", check_fields=False)
    def validate_object_type_instance(cls, v: Optional["ObjectType"], values: Dict[str, Any]) -> Optional["ObjectType"]:
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

    def validate_object_types(self, session: Session) -> None:
        """
        Validate both source and target object types.
        This should be called after the instance is created and before committing to the database.
        """
        # Set the session for validation

        # If object_type is already set, use it
        if self.object_type:
            # Ensure object_type_rid matches
            self.object_type_rid = self.object_type.rid
            # Ensure object_type_api_name matches
            self.object_type_api_name = self.object_type.api_name
        else:
            # Try to get object type by RID first
            try:
                source_type = self._get_object_type_by_rid(session)
                self.object_type = source_type
                self.object_type_api_name = source_type.api_name
            except ValueError:
                # If that fails, try by api_name
                if self.object_type_api_name:
                    source_type = self._get_object_type_by_api_name(session)
                    self.object_type = source_type
                    self.object_type_rid = source_type.rid
                else:
                    # If we get here, we couldn't find the object type
                    raise ValueError(f"Could not find source object type for link '{self.api_name}'. Please provide either object_type_rid or object_type_api_name.")

        # Validate source object type
        self._validate_object_type(self.object_type)

        # If foreign_key_property_api_name is provided but target_object_type_api_name is not set yet,
        # try to resolve it from the property
        if self.foreign_key_property_api_name and not self.target_object_type_api_name:
            property_type = self._get_foreign_key_property(session)
            if not property_type:
                raise ValueError(
                    f"Foreign key property '{self.foreign_key_property_api_name}' not found in "
                    f"object type '{self.object_type_api_name}'"
                )
            # Determine target object type from property
            # This is a simplified approach - in a real system, you might have more complex logic
            self.target_object_type_api_name = property_type.api_name.replace("_id", "").replace("_rid", "")

        # Validate target object type
        target_type = self._get_target_object_type(session)
        self._validate_object_type(target_type)

    # Update model_config to exclude database fields from serialization
    model_config = {
        "extra": "forbid",
        "json_schema_extra": {"exclude": {"object_type_rid", "object_type"}}
    }

    def model_dump(self, **kwargs):
        """Override model_dump to ensure database fields are excluded by default"""
        exclude = kwargs.get("exclude", set())
        if isinstance(exclude, set):
            exclude.update({"object_type_rid", "object_type"})
        elif isinstance(exclude, dict):
            exclude["object_type_rid"] = True
            exclude["object_type"] = True
        else:
            exclude = {"object_type_rid", "object_type"}
        kwargs["exclude"] = exclude
        return super().model_dump(**kwargs)

# Import at the end to avoid circular imports
from .object_type import ObjectType

# Model rebuilding
LinkTypeSide.model_rebuild()