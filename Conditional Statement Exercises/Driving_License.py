# Driving License
#Conditions: 
#- Age >= 18. 
#- Check whether a learner license is available.
#- Driving test score >= 60. 

age = int(input("Enter your age: "))
if age >= 18:
    learner_license = input("Do you have a learner license? (yes/no): ").lower()
    if learner_license == "yes":
        score = int(input("Enter driving test score: "))
        if score >= 60:
            print("Driving License Approved")
        else:
            print("Driving Test Failed")
    else:
        print("Learner License Required")
else:
    print("Not Eligible: Age must be 18 or above")