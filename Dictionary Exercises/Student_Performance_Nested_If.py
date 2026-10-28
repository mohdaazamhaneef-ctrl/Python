# Exercise 2: Student Performance Using Nested If
# Marks >= 80 -> Excellent
# Marks >= 60 -> Good
# Marks >= 40 -> Average
# Marks < 40 -> Fail

students = {
    "Rahul": 85,
    "Amit": 35,
    "Priya": 72,
    "Neha": 48
}

for name, marks in students.items():
    if marks >= 80:
        category = "Excellent"
    elif marks >= 60:
        category = "Good"
    elif marks >= 40:
        category = "Average"
    else:
        category = "Fail"

    print(name, marks, category)
