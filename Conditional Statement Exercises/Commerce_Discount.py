#E-Commerce Discount
#An online shopping website provides discounts based on the following conditions: 
#- If cart amount >= ₹5,000: 
#- If the customer is a premium member, discount = 20%. 
#- Otherwise, discount = 10%. 
#- If cart amount < ₹5,000: 
#- If the customer is a premium member, discount = 5%. 
#- Otherwise, no discount. 
#- Print the final amount. 

amount=int(input("Enter Amount: "))
Premium_Member=True
if (amount>=5000):
    if(Premium_Member):
        discount=amount*20/100
        print("Discount amount is: ",discount)
    else:
        discount=amount*10/100
        print("Discount amount is: ",discount)
elif(Premium_Member):
    discount=amount*5/100
    print("Discount amount is: ",discount)
else:
    discount=0
    print("Discount amount is: ",discount)

final_amount=amount-discount
print("Your final amount is: ",final_amount)
