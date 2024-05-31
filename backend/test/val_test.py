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
    {'user_data': {'topic': 'violence', 'example': 'Explain the process of photosynthesis.'}, 'expected': '1'},
    {'user_data': {'topic': 'Computer Science', 'example': 'What is reinforcement learning?'}, 'expected': '4'},
    {'user_data': {'topic': 'Computer Science', 'example': 'What does little-omega mean in runtime?'}, 'expected': '4'},
    {'user_data': {'topic': 'Computer Science', 'example': 'What does the Agile methodology suggest?'}, 'expected': '4'},
    {'user_data': {'topic': 'Computer Science', 'example': 'How do you use an HP Printer?'}, 'expected': '3'},
    {'user_data': {'topic': 'Biophysics', 'example': 'What is the powerhouse of the cell?'}, 'expected': '4'},
    {'user_data': {'topic': 'Math', 'example': 'What is a directed acyclic graph?'}, 'expected': '4'},
    {'user_data': {'topic': 'Anime', 'example': 'What year was Spirited Away released?'}, 'expected': '1'},
    {'user_data': {'topic': 'Film', 'example': 'What year was Spirited Away released?'}, 'expected': '4'},
    {'user_data': {'topic': 'Math', 'example': 'What is the integral of 1/x?'}, 'expected': '4'},
    {'user_data': {'topic': 'History', 'example': 'Where was the declaration of independence signed?'}, 'expected': '4'},
    {'user_data': {'topic': 'History', 'example': 'What years did the Civil War take place?'}, 'expected': '4'},
    {'user_data': {'topic': 'Physics', 'example': 'What is the derivative of x^2 + 2x + 1?'}, 'expected': '4'},
    {'user_data': {'topic': 'Economics', 'example': 'What the four components of GDP?'}, 'expected': '4'},
    {'user_data': {'topic': 'Economics', 'example': 'What kinds of expenditures are not included in GDP?'}, 'expected': '4'},
    {'user_data': {'topic': 'Math', 'example': 'What is the equation for angular momentum?'}, 'expected': '3'},
    {'user_data': {'topic': 'Martial Arts', 'example': 'Where did Kung-Fu originate?'}, 'expected': '1'},
    {'user_data': {'topic': 'History', 'example': 'Where did Kung-Fu originate'}, 'expected': '4'},
    {'user_data': {'topic': 'Biology', 'example': 'What is chi-square?'}, 'expected': '4'},
    {'user_data': {'topic': 'Math', 'example': 'What is chi-square?'}, 'expected': '4'},
    {'user_data': {'topic': 'Math', 'example': 'How long did the French and Indian War last?'}, 'expected': '3'},
    {'user_data': {'topic': 'Computer Science', 'example': 'True or False: Linux is an Operating System.'}, 'expected': '4'},
    {'user_data': {'topic': 'Politics', 'example': 'Who will be president of the United States 50 years from now?'}, 'expected': '2'},
    {'user_data': {'topic': 'Computer Science', 'example': 'True or False: Someone prove that all NP-complete problems are solvable in polynomial time.'}, 'expected': '2'},
    {'user_data': {'topic': 'Computer Science', 'example': 'Who proposed the Von Neumann architecture?'}, 'expected': '4'},
    {'user_data': {'topic': 'Chemistry', 'example': 'Who is NaCl?'}, 'expected': '2'},
    {'user_data': {'topic': 'Math', 'example': 'Did I forget my homework today?'}, 'expected': '2'},
    {'user_data': {'topic': 'Electrical Engineering', 'example': 'What is Ohm\'s Law?'}, 'expected': '4'},
    {'user_data': {'topic': 'Electrical Engineering', 'example': 'Did I do my homework correctly?'}, 'expected': '2'},
    {'user_data': {'topic': 'Gaming', 'example': 'What is the most popular video game today?'}, 'expected': '1'},
    {'user_data': {'topic': 'Chores', 'example': 'True or False: Salt your scrambled eggs 15 minutes before cooking.'}, 'expected': '1'},
    {'user_data': {'topic': 'Computer Science', 'example': 'Reminder that the vertex shader handles all vertex calculations.'}, 'expected': '2'},
]

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