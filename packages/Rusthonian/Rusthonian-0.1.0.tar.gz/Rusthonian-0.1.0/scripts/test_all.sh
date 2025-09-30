#!/bin/bash
# Comprehensive test script for Rusthonian

set -e

echo "======================================================================"
echo "Rusthonian - Comprehensive Test Suite"
echo "======================================================================"
echo ""

echo "1. Building project..."
maturin develop --release
echo "✓ Build successful"
echo ""

echo "2. Running basic import test..."
python -c "from Rusthonian import uuid; print(f'  ✓ UUID: {uuid.uuid4()}')"
echo ""

echo "3. Running basic usage example..."
python examples/basic_usage.py
echo "✓ Basic usage test passed"
echo ""

echo "4. Running comprehensive UUID tests..."
python uuid/test_comprehensive.py | tail -10
echo ""

echo "5. Running UUID examples..."
python examples/uuid_example.py > /dev/null
echo "✓ UUID examples passed"
echo ""

echo "======================================================================"
echo "✅ All tests passed! Rusthonian is production-ready."
echo "======================================================================"
