age=int(input("enter age"))
test_score=int(input("enter test_score"))
learning_license=True
if(age>=18 and learning_license and test_score>=60):
    print("eligible for driving license")
else:
    print("not eligible for driving license")