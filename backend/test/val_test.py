import sys
import os

#TODO need to fix directory issue??
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app.controllers.user_val import isValid

test_cases = [
    {'user_data': {'topic': 'Math', 'example': 'efdsafhjkads'}, 'expected': '2'},
    {'user_data': {'topic': 'drugs', 'example': 'What are the effects of illegal drugs on the human body?'}, 'expected': '4'},
    {'user_data': {'topic': 'Physics', 'example': 'What is the theory of relativity?'}, 'expected': '4'},
    {'user_data': {'topic': 'History', 'example': 'What is the Pythagorean theorem?'}, 'expected': '3'},
    {'user_data': {'topic': 'Biology', 'example': 'How do plants perform photosynthesis?'}, 'expected': '4'},
    {'user_data': {'topic': 'violence', 'example': 'Explain the process of photosynthesis.'}, 'expected': '1'}
]


success_count = 0
total_tests = len(test_cases)

for i, test in enumerate(test_cases):
    result = isValid(test['user_data'])
    success = result.strip() == test['expected']
    if success:
        success_count += 1
    print(f"Test Case {i+1}: {'Success' if success else 'Fail'} - Expected: {test['expected']}, Got: {result}")


accuracy = (success_count / total_tests) * 100
print(f"\nAccuracy: {accuracy:.2f}% ({success_count}/{total_tests} tests passed)")