#ATM Difficult Challenge 
#Conditions: 
#- PIN must be correct. 
#- Account must be active. 
#- Amount must be positive. 
#- Amount must be a multiple of ₹100. 
#- Balance must be sufficient. 
#- After withdrawal, a minimum balance of ₹500 must remain. 
#- Amount > ₹20,000 -> Extra verification. 

correct_pin = 1234
account_active = True
balance = 25000
pin = int(input("Enter your ATM PIN: "))
if pin == correct_pin:
    if account_active:
        amount = int(input("Enter withdrawal amount: ₹"))
        if amount > 0:
            if amount % 100 == 0:
                if balance >= amount + 500:
                    if amount > 20000:
                        verify = input("Extra verification required (yes/no): ").lower()
                        if verify == "yes":
                            balance = balance - amount
                            print("Withdrawal Successful")
                            print("Remaining Balance: ₹", balance)
                        else:
                            print("Extra Verification Failed")
                    else:
                        balance = balance - amount
                        print("Withdrawal Successful")
                        print("Remaining Balance: ₹", balance)
                else:
                    print("Insufficient Balance or Minimum Balance Required")
            else:
                print("Amount must be a multiple of ₹100")
        else:
            print("Amount must be positive")
    else:
        print("Account is Inactive")
else:
    print("Incorrect PIN")
