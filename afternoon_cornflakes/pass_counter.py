"""
Write a python program that accept scores of
15 student from teacher(user) and determine
the number of students that pass or fail.
pass mark is 45
"""

number_passed = 0
for count in range(1, 16):
    score = int(input("Enter score: "))
    if score >= 45:
        number_passed += 1
number_failed = 15 - number_passed
print("passed: ",number_passed)
print("failed: ",number_failed)
