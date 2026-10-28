# Login + Role-Based Access
#Create a login system. 
#Conditions: 
#- Check username. 
#- If username is correct, check password. 
#- If password is correct, check role: 
#- "admin" -> Full Access 
#- "teacher" -> Teacher Dashboard 
#- "student" -> Student Dashboard 
#- Anything else -> Invalid Role 
#- Wrong password -> "Wrong Password" 
#- Wrong username -> "Invalid Username" 
username = input("Enter username: ")
password = input("Enter password: ")
if username == "admin123":
    if password == "admin@123":
        role = input("Enter role (admin/teacher/student): ").lower()
        if role == "admin":
            print("Full Access")
        elif role == "teacher":
            print("Teacher Dashboard")
        elif role == "student":
            print("Student Dashboard")
        else:
            print("Invalid Role")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")