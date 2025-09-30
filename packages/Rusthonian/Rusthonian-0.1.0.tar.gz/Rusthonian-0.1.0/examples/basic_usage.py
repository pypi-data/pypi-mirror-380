#!/usr/bin/env python3
"""
Basic Usage Example for Rusthonian

This example shows basic usage of the Rusthonian package.
"""

# Import the Rusthonian package
from Rusthonian import uuid

# Generate a random UUID (v4)
random_uuid = uuid.uuid4()
print(f"Random UUID: {random_uuid}")

# Generate a timestamp-based UUID (v7)
timestamp_uuid = uuid.uuid7()
print(f"Timestamp UUID: {timestamp_uuid}")

# Create UUID from string
parsed_uuid = uuid.UUID(hex="550e8400-e29b-41d4-a716-446655440000")
print(f"Parsed UUID: {parsed_uuid}")

# Get UUID properties
print(f"Version: {parsed_uuid.version}")
print(f"Variant: {parsed_uuid.variant}")
print(f"Is nil: {parsed_uuid.is_nil()}")

# Different string formats
print(f"Simple format: {random_uuid.as_simple()}")
print(f"URN format: {random_uuid.as_urn()}")
