# Exercise 1: Check Student Result
# Marks >= 40 -> Pass
# Marks < 40 -> Fail

students = {
    "Rahul": 75,
    "Amit": 32,
    "Priya": 88,
    "Neha": 39,
    "Rohit": 55
}

for name, marks in students.items():
    if marks >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print(name, marks, result)
