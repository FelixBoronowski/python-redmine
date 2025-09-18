#!/usr/bin/env python3
"""
Example usage of the EasyRedmine asset plugin integration with python-redmine.

This example demonstrates how to use the CustomTable and CustomEntity resources
to interact with EasyRedmine's asset management functionality.
"""

from redminelib import Redmine

# Initialize Redmine connection
redmine = Redmine('https://your-redmine-instance.com', key='your-api-key')

# Working with Custom Tables (Asset Table Definitions)
def list_custom_tables():
    """List all available custom tables."""
    print("Available Custom Tables:")
    for table in redmine.custom_table.all():
        print(f"  ID: {table.id}, Name: {table.name}")

def create_custom_table():
    """Create a new custom table for asset management."""
    table = redmine.custom_table.new()
    table.name = "IT Equipment"
    table.description = "Table for tracking IT equipment assets"
    table.save()
    print(f"Created custom table: {table.name} (ID: {table.id})")
    return table

def get_custom_table(table_id):
    """Get a specific custom table by ID."""
    table = redmine.custom_table.get(table_id)
    print(f"Table: {table.name}")
    print(f"Description: {getattr(table, 'description', 'N/A')}")
    return table

# Working with Custom Entities (Asset Records)
def list_entities_in_table(table_id):
    """List all entities in a specific custom table."""
    print(f"Entities in table {table_id}:")
    entities = redmine.custom_entity.filter(custom_table_id=table_id)
    for entity in entities:
        print(f"  ID: {entity.id}, Name: {entity.name}")

def create_asset_entity(table_id):
    """Create a new asset entity in a custom table."""
    entity = redmine.custom_entity.new()
    entity.custom_table_id = table_id
    entity.name = "Dell Laptop #12345"
    entity.notes = "Assigned to John Doe"
    # Set custom field values if needed
    # entity.custom_field_values = {'1': 'Dell', '2': 'Latitude 7420'}
    entity.save()
    print(f"Created entity: {entity.name} (ID: {entity.id})")
    return entity

def get_asset_entity(entity_id):
    """Get a specific asset entity by ID."""
    entity = redmine.custom_entity.get(entity_id)
    print(f"Entity: {entity.name}")
    print(f"Custom Table ID: {entity.custom_table_id}")
    print(f"Notes: {getattr(entity, 'notes', 'N/A')}")
    return entity

def update_asset_entity(entity_id, new_notes):
    """Update an asset entity."""
    entity = redmine.custom_entity.get(entity_id)
    entity.notes = new_notes
    entity.save()
    print(f"Updated entity {entity.id} with new notes")

def delete_asset_entity(entity_id):
    """Delete an asset entity."""
    entity = redmine.custom_entity.get(entity_id)
    entity.delete()
    print(f"Deleted entity {entity_id}")

# Example workflow
if __name__ == "__main__":
    try:
        # List existing tables
        list_custom_tables()

        # Create a new table (uncomment to test)
        # table = create_custom_table()

        # Work with entities in table ID 1 (adjust as needed)
        # table_id = 1
        # list_entities_in_table(table_id)

        # Create a new asset (uncomment to test)
        # entity = create_asset_entity(table_id)

        # Get and update an entity (uncomment to test)
        # entity = get_asset_entity(1)
        # update_asset_entity(1, "Updated notes from API")

        print("Asset plugin integration is working!")

    except Exception as e:
        print(f"Error: {e}")
        print("Make sure your Redmine instance has the custom tables plugin installed")
        print("and that you have the proper permissions.")