unit = int(input("enter electricity unit:"))
if unit <= 100:
    bill = unit * 5
elif unit <= 200:
    bill = unit * 7
elif unit <= 300:
    bill = unit * 10
else:
     bill = unit * 15
     print("bill : ",bill)
if bill > 3000:
    surcharge = bill * 10/100
    print("surcharge bill: ", surcharge)
    bill = bill + surcharge;
print("after include surcharge bill :",bill)
print("final electricity bill = ", bill)     