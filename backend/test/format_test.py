import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app.controllers.api_controller import process_request

# prepare .json file
json_reader = open("test_cases_format.json", "r")
test_cases = json.loads(json_reader.read())

# open another file for writing
fout = open("output.py", "w")

success_count = 0
total_tests = len(test_cases)

# helper functions
def isString(value1):
    return type(value1) == type("")
def validChoices(letters, choices):
    if type(choices) != type({"slug": "practice"}):
        return False
    for letter in letters:
        if letter not in choices.keys() or not isString(choices[letter]):
            return False
    return True
def keysInDict(keyList, question):
    return sum([1 for key in keyList if key in question.keys()]) == len(keyList)
def questionTest(statement):
    return isString(statement) and \
        len(statement) >= 1

fout.write("STARTING TEST\n")
for i, test in enumerate(test_cases):
    print(f"Running Test Case {i + 1}:")
    res = process_request(test)
    success = len(res) == 2 and \
        keysInDict(["questions", "status"], res) and \
        type(res["questions"]) == type([])
    if success:
        for question in res["questions"]:
            #print(question)
            if test["format"] == "mc":
                # check the json
                choiceVar = "choice" if "choice" in question.keys() else "choices"
                success = len(question) == 3 and keysInDict(["question", choiceVar, "answer"], question)  # check if every key is in the dict
                # check the question
                success = success and questionTest(question["question"])
                # check the choices, this part fails if question[choiceVar] is a list
                success = success and validChoices("ABC", question[choiceVar])
                # check the answer
                success = success and isString(question["answer"]) and len(question["answer"]) == 1 and question["answer"] in "ABC"
                # check the test result
                if success == False:
                    break
            else:
                success = len(question) == 2 and keysInDict(["question", "answer"], question)  # check if every key is in the dict
                # check the question
                success = success and questionTest(question["question"])
                # check the answer:
                if test["format"] == "tf":
                    success = success and isString(question["answer"]) and question["answer"] in ["True", "False"] 
                elif test["format"] == "simple":
                    success = success and isString(question["answer"]) 
                else:
                    success = False
                # check the test result
                if success == False:
                    break
        if success:
            success_count += 1
        fout.write(f"Test Case {i+1}: {'Success' if success else 'Fail'}\n")
    else:
        fout.write(f"Test Case {i+1}: .json file returned wrong number of items\n")
    print(f"{i + 1} / {total_tests} Tests Done\n==================================================================")

accuracy = (success_count / total_tests) * 100
fout.write(f"\nAccuracy: {accuracy:.2f}% ({success_count}/{total_tests} tests passed)\n")
fout.close()
print("Find the test output in output.py")


# debug tips


# debug output I had earlier
"""
    print(f'len(res): {len(res)}')
    print(f'keys: {res.keys()}\t\t{keysInDict(["questions", "status"], res)}')
    print(f'{type(res["questions"]) == type([])}')
"""