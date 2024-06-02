import sys
import os
import json

#TODO need to fix directory issue??
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app.controllers.user_val import isValid

json_reader = open("test_cases.json", "r")
test_cases = json.loads(json_reader.read())

success_count = 0
total_tests = len(test_cases)

for i, test in enumerate(test_cases):
    result = isValid(test['user_data'])
    success = result.strip(' .') == test['expected']
    print(f"Test Case {i+1}: {'Success' if success else 'Fail'} - Expected: {test['expected']}, Got: {result}")
    if success:
        success_count += 1

accuracy = (success_count / total_tests) * 100
print(f"\nAccuracy: {accuracy:.2f}% ({success_count}/{total_tests} tests passed)")