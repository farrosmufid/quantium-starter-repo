#!/bin/bash

# 1. Activate virtual environment
source env/bin/activate

if [ $? -ne 0 ]; then
    echo "Failed to activate the virtual environment."
    exit 1
fi

# 2. Execute the test suite
pytest

# 3. Return exit code 0 if all tests passed, or 1 if something went wrong
if [ $? -eq 0 ]; then
    echo "All tests passed successfully."
    exit 0
else 
    echo "Tests failed."
    exit 1
fi
