#!/usr/bin/env python3
"""
Example: Using Rusthonian's UUID module

This example demonstrates the various UUID generation and manipulation
features available through Rusthonian's uuid bindings.
"""

from Rusthonian import uuid

def main():
    print("=" * 60)
    print("Rusthonian UUID Examples")
    print("=" * 60)
    print()

    # Example 1: Generate different UUID versions
    print("1. Generating different UUID versions:")
    print("-" * 40)
    
    v4 = uuid.uuid4()
    print(f"   UUID v4 (random):     {v4}")
    
    v7 = uuid.uuid7()
    print(f"   UUID v7 (timestamp):  {v7}")
    
    v3 = uuid.uuid3(uuid.NAMESPACE_DNS, "example.com")
    print(f"   UUID v3 (MD5):        {v3}")
    
    v5 = uuid.uuid5(uuid.NAMESPACE_URL, "https://example.com")
    print(f"   UUID v5 (SHA-1):      {v5}")
    print()

    # Example 2: UUID from different formats
    print("2. Creating UUIDs from various formats:")
    print("-" * 40)
    
    # From hex string
    u1 = uuid.UUID(hex="550e8400-e29b-41d4-a716-446655440000")
    print(f"   From hex:   {u1}")
    
    # From int
    u2 = uuid.UUID(int=113059749145936325402354257176981405696)
    print(f"   From int:   {u2}")
    
    # From bytes
    u3 = uuid.UUID.from_bytes(u1.bytes)
    print(f"   From bytes: {u3}")
    print()

    # Example 3: Different string formats
    print("3. Different string representations:")
    print("-" * 40)
    u = uuid.uuid4()
    print(f"   Hyphenated: {u.as_hyphenated()}")
    print(f"   Simple:     {u.as_simple()}")
    print(f"   Braced:     {u.as_braced()}")
    print(f"   URN:        {u.as_urn()}")
    print(f"   Uppercase:  {u.encode_simple_upper()}")
    print()

    # Example 4: UUID properties
    print("4. UUID properties and fields:")
    print("-" * 40)
    u = uuid.uuid4()
    print(f"   UUID:       {u}")
    print(f"   Version:    {u.version}")
    print(f"   Variant:    {u.variant}")
    print(f"   As int:     {u.int}")
    print(f"   Time low:   {u.time_low()}")
    print(f"   Node:       {u.node()}")
    print()

    # Example 5: Timestamp extraction
    print("5. Working with timestamps:")
    print("-" * 40)
    u7 = uuid.uuid7()
    print(f"   UUID v7:       {u7}")
    print(f"   Has timestamp: {u7.has_timestamp()}")
    ts = u7.get_timestamp()
    if ts:
        seconds, nanos = ts
        print(f"   Timestamp:     (seconds={seconds}, nanos={nanos})")
        print(f"   Seconds:       {seconds}")
        print(f"   Nanos:         {nanos}")
    print()

    # Example 6: Namespace constants
    print("6. Using namespace constants:")
    print("-" * 40)
    dns_uuid = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")
    url_uuid = uuid.uuid5(uuid.NAMESPACE_URL, "https://example.com")
    oid_uuid = uuid.uuid5(uuid.NAMESPACE_OID, "1.2.3.4")
    x500_uuid = uuid.uuid5(uuid.NAMESPACE_X500, "CN=example")
    
    print(f"   DNS namespace:  {dns_uuid}")
    print(f"   URL namespace:  {url_uuid}")
    print(f"   OID namespace:  {oid_uuid}")
    print(f"   X500 namespace: {x500_uuid}")
    print()

    # Example 7: UUID comparison and sorting
    print("7. UUID comparison and sorting:")
    print("-" * 40)
    uuids = [uuid.uuid4() for _ in range(5)]
    sorted_uuids = sorted(uuids, key=lambda x: str(x))
    print("   Sorted UUIDs:")
    for u in sorted_uuids[:3]:  # Show first 3
        print(f"     - {u}")
    print()

    # Example 8: Using Builder for custom UUIDs
    print("8. Building custom UUIDs:")
    print("-" * 40)
    builder = uuid.Builder()
    builder.with_version(4)
    builder.with_variant("RFC4122")
    custom_uuid = builder.build()
    print(f"   Custom UUID: {custom_uuid}")
    print()

    # Example 9: Performance test
    print("9. Performance demonstration:")
    print("-" * 40)
    import time
    
    start = time.time()
    count = 100000
    for _ in range(count):
        uuid.uuid4()
    elapsed = time.time() - start
    
    print(f"   Generated {count:,} UUIDs in {elapsed:.3f}s")
    print(f"   Rate: {count/elapsed:,.0f} UUIDs/second")
    print()

    print("=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)

if __name__ == "__main__":
    main()
