#Question 5: Check Even/Odd Values 
#Given a dictionary, check whether each value is even or odd. 
#Conditions: 
#- Even and greater than 20 -> Large Even 
#- Even and <= 20 -> Even 
#- Odd -> Odd 
data = { 
        "a": 10, 
        "b": 15, 
        "c": 25, 
        "d": 30, 
        "e": 40 
}
for key, value in data.items():
    if value % 2 == 0:
        if value > 20:
            result = "Large Even"
            print("Key:",key,"Value:",value,"Result:",result)
        else:
            result = "Even"
            print("Key:",key,"Value:",value,"Result:",result)
    else:
        result = "Odd"
        print("Key:",key,"Value:",value,"Result:",result)