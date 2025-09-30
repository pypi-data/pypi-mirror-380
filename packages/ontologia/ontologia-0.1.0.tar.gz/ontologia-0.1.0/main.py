# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "sqlmodel>=0.0.24",
#     "registro>=0.1.5",
#     "pydantic>=2.0.0",
#     "ulid-py>=1.1.0",
# ]
# ///

# --- main.py ---

import logging
# ---- ADD THIS SECTION ----
# Configure the external 'registro' library FIRST
try:
    import sys
    import site
    from pathlib import Path
    
    # Add the site-packages to sys.path if not already there
    python_path = Path('.pythonlibs/lib/python3.11/site-packages')
    if python_path.exists() and str(python_path) not in sys.path:
        sys.path.append(str(python_path))
    
    from registro.config import settings
    # Set defaults to match previous ontologia/registry behavior
    settings.DEFAULT_SERVICE = "ontology"
    settings.DEFAULT_INSTANCE = "main"
    # Set the specific TYPE pattern required by ontologia's resource types
    settings.set_pattern("TYPE", r"^(object-type|property-type|link-type)$") # Adjust if 'ontology' or 'object' are also valid resource types

    # Define RESERVED_WORDS specific to ontologia, excluding allowed type names
    ontologia_base_reserved = {
        "registro", "resource", # From registro itself
        "property", "link", "relation",
        "rid", "primaryKey", "typeId", "resourceObject",
        "create", "read", "update", "delete", "list", "all",
        "null", "true", "false", "none", "id",
        # Add any other specific reserved words needed by ontologia
    }
    # Let registro handle its own internal reserved words plus yours
    current_reserved = settings.RESERVED_WORDS
    current_reserved.update(ontologia_base_reserved)
    settings.RESERVED_WORDS = current_reserved

    logging.info("Registro library configured for Ontologia.")
except ImportError as e:
    logging.error(f"Failed to import and configure the 'registro' library: {e}")
    exit(1)
# ---- END ADDED SECTION ----


"""
Example usage of the Ontologia registry system with ObjectType and LinkTypeSide.
This script demonstrates creating and managing object types and their relationships.
"""

import logging
from sqlmodel import SQLModel, Session, create_engine, select
from sqlalchemy import inspect
from ontologia.domain.metamodels.types.object_type import ObjectType
from ontologia.domain.metamodels.types.link_type import LinkTypeSide, Cardinality
from ontologia.domain.metamodels.types.property_type import PropertyType

# Configure logging - set to DEBUG level
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Database configuration
DATABASE_URL = "sqlite:///ontologia.db"
engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    """Initialize the database by creating all tables."""
    logger.info("Creating database tables...")
    SQLModel.metadata.drop_all(engine)  # Start fresh
    SQLModel.metadata.create_all(engine)
    
    # List all tables using SQLAlchemy inspect
    inspector = inspect(engine)
    table_names = inspector.get_table_names()
    logger.info("Database tables created:")
    logger.info(f"Tables: {table_names}")

def create_person_object_type(session: Session):
    """Create a sample Person object type with properties."""
    # Create the object type first
    person_type = ObjectType(
        service="ontology",
        instance="main",
        api_name="person",
        display_name="Person",
        primary_key_field="first_name"
    )
    
    # Save the object type first to get its RID
    session.add(person_type)
    session.commit()

    # Define properties using dictionaries (approach 1)
    properties = [
        {
            "api_name": "first_name",
            "display_name": "First Name",
            "data_type": "string",
            "required": True
        },
        {
            "api_name": "last_name",
            "display_name": "Last Name",
            "data_type": "string",
            "required": True
        },
        {
            "api_name": "age",
            "display_name": "Age",
            "data_type": "integer",
            "required": False
        },
        {
            "api_name": "address_id",
            "display_name": "Address ID",
            "data_type": "string",
            "required": False
        }
    ]

    # Set properties using the session
    person_type.set_properties(properties, session)
    session.commit()
    return person_type

def create_address_object_type(session: Session):
    """Create a sample Address object type with properties."""
    # Create the object type first
    address_type = ObjectType(
        service="ontology",
        instance="main",
        api_name="address",
        display_name="Address",
        primary_key_field="street"
    )
    
    # Save the object type first to get its RID
    session.add(address_type)
    session.commit()

    # Define properties using PropertyType instances (approach 2)
    properties = [
        PropertyType(
            service="ontology",
            instance="main",
            api_name="street",
            display_name="Street",
            data_type="string",
            required=True,
            object_type_api_name=address_type.api_name  # Only need to provide api_name
        ),
        PropertyType(
            service="ontology",
            instance="main",
            api_name="city",
            display_name="City",
            data_type="string",
            required=True,
            object_type_api_name=address_type.api_name  # Only need to provide api_name
        ),
        PropertyType(
            service="ontology",
            instance="main",
            api_name="postal_code",
            display_name="Postal Code",
            data_type="string",
            required=True,
            object_type_api_name=address_type.api_name  # Only need to provide api_name
        )
    ]

    # Set properties using the session
    address_type.set_properties(properties, session)
    session.commit()
    return address_type

def create_person_address_link(person_type: ObjectType, address_type: ObjectType):
    """Create a link type between Person and Address using explicit target object type."""
    # Create link using only api_names
    link = LinkTypeSide(
        service="ontology",
        instance="main",
        api_name="lives_at",
        display_name="Lives At",
        cardinality=Cardinality.ONE,
        object_type_api_name=person_type.api_name,
        target_object_type_api_name=address_type.api_name
    )
    return link

def create_person_address_link_by_property(person_type: ObjectType):
    """Create a link type between Person and Address using a foreign key property."""
    # Create link using foreign_key_property_api_name instead of target_object_type_api_name
    link = LinkTypeSide(
        service="ontology",
        instance="main",
        api_name="has_address",
        display_name="Has Address",
        cardinality=Cardinality.ONE,
        object_type_api_name=person_type.api_name,
        foreign_key_property_api_name="address_id"
    )
    return link

def main():
    """Main function demonstrating the usage of the registry system."""
    # Initialize database
    init_db()

    # Create a session
    with Session(engine) as session:
        try:
            # Create person and address object types
            logger.info("Creating object types...")
            person_type = create_person_object_type(session)
            address_type = create_address_object_type(session)
            
            # Create link between person and address (approach 1: explicit target)
            logger.info("Creating link type with explicit target...")
            person_address_link = create_person_address_link(person_type, address_type)
            
            # Validate and link object types
            person_address_link.validate_object_types(session)
            
            session.add(person_address_link)
            session.commit()
            
            # Create link between person and address (approach 2: using foreign key property)
            logger.info("Creating link type using foreign key property...")
            person_address_link_by_property = create_person_address_link_by_property(person_type)
            
            # Validate and link object types
            person_address_link_by_property.validate_object_types(session)
            
            session.add(person_address_link_by_property)
            session.commit()
            
            # Show object type details
            logger.info("\nCreated Types:")
            logger.info(f"Person Type RID: {person_type.rid}")
            logger.info(f"Address Type RID: {address_type.rid}")
            logger.info(f"Link Type (explicit) RID: {person_address_link.rid}")
            logger.info(f"Link Type (by property) RID: {person_address_link_by_property.rid}")
            
            # Query and show property types
            logger.info("\nProperty Types:")
            property_types = session.exec(select(PropertyType)).all()
            logger.info(f"Total property types in database: {len(property_types)}")
            for prop in property_types:
                logger.info(f"  - {prop.api_name} ({prop.data_type}) -> ObjectType: {prop.object_type_api_name}")
            
            # Demonstrate relationships
            logger.info("\nRelationships:")
            logger.info(f"Person Type properties: {len(person_type.property_types)}")
            for prop in person_type.property_types:
                logger.info(f"  - {prop.api_name} ({prop.data_type})")
            
            logger.info(f"Person Type outgoing links: {len(person_type.outgoing_link_types)}")
            for link in person_type.outgoing_link_types:
                if hasattr(link, 'foreign_key_property_api_name') and link.foreign_key_property_api_name:
                    logger.info(f"  - {link.api_name} ({link.cardinality}) -> {link.target_object_type_api_name} [via property: {link.foreign_key_property_api_name}]")
                else:
                    logger.info(f"  - {link.api_name} ({link.cardinality}) -> {link.target_object_type_api_name}")
            
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            session.rollback()
            raise

        # --- NOVO: Imprimir tabelas e schema ao final ---
        finally:
            # Use SQLAlchemy inspector para obter informações detalhadas
            inspector = inspect(engine)

            logger.info("\n--- DATABASE SCHEMA SUMMARY ---")
            table_names = inspector.get_table_names()
            logger.info(f"Total de tabelas criadas: {len(table_names)}")
            for table_name in table_names:
                logger.info(f"\nTabela: {table_name}")
                columns = inspector.get_columns(table_name)
                logger.info("  Colunas:")
                for col in columns:
                    logger.info(f"    - {col['name']} ({col['type']})")
                # Opcional: Imprimir chaves estrangeiras
                fks = inspector.get_foreign_keys(table_name)
                if fks:
                    logger.info("  Chaves Estrangeiras:")
                    for fk in fks:
                         logger.info(f"    - {fk['constrained_columns']} -> {fk['referred_table']}.{fk['referred_columns']}")

            logger.info("\n--- END DATABASE SCHEMA SUMMARY ---")

if __name__ == "__main__":
    main()
