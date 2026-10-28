#Bank Account Classification 
#A dictionary contains customer names and account balances. 
#Conditions: 
#- Balance >= ₹10,000 -> Premium Account 
#- Balance > 0 but < ₹10,000 -> Regular Account 
#- Balance == 0 -> No Balance 
#- Balance < 0 -> Overdraft 
 
accounts = { 
        "Rahul": 25000, 
        "Amit": 5000, 
        "Priya": 0, 
        "Neha": -2000 
}
for name, balance in accounts.items():
    if balance >= 10000:
        category = "Premium Account"
    elif balance > 0:
        category = "Regular Account"
    elif balance == 0:
        category = "No Balance"
    else:
        category = "Overdraft"

    print(name, balance, category)