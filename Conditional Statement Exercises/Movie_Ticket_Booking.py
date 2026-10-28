# Movie Ticket Booking
#Create a ticket booking system. 
#Conditions: 
#- Check whether seats are available. 
#- If seats are available, check customer age: 
#- Age < 5 -> Free - Age 5-12 -> 50% discount 
#- Age > 60 -> 30% discount 
#- Otherwise -> Full price 
#- If no seats are available, print "House Full".
seats = int(input("Enter available seats: "))
age = int(input("Enter customer age: "))
price = float(input("Enter ticket price: ₹"))
if seats > 0:
    if age < 5:
        discount = 100
    elif age <= 12:
        discount = 50
    elif age > 60:
        discount = 30
    else:
        discount = 0

    discount_amount = price * discount / 100
    final_price = price - discount_amount

    print("Discount:", discount, "%")
    print("Final Ticket Price: ₹", final_price)
else:
    print("House Full")