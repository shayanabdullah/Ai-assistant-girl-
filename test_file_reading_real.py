#!/usr/bin/env python3
"""Test file reading with updated DESKTOP_CONTROL_PROMPT"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'riko_project'))

from server.process.llm_funcs.llm_scr import llm_response

# Test file reading
print("=== Testing File Reading ===")
test_message = "read the test_file.txt file and tell me what's in it"
print(f"User: {test_message}")
print()

response = llm_response(test_message)
print(f"Riko: {response}")
print()

print("=== Test Complete ===")
