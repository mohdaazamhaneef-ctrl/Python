# lenth method()
studentinfo=["Aazam","Pyhton","MCA",23,80000.00,False]
print(len(studentinfo))

# append method()
marks=[66,76,56,99,87,98,78]
marks.append(44)
marks.append([33,22])
print(marks)
print(marks[7])     #index

#inset method()
marks=[66,76,56,99,87,98,78]
marks.insert(1,33)
print(marks)

#entend method()
marks=[66,76,56,99,87,98,78]
marks.extend([77,88,55])
print(marks)

#remove method()
marks=[66,76,56,99,87,98,76,78]
marks.remove(76)
print(marks)        #ValueError: if list.remove(x): x not in list

#pop method()
marks=[66,76,56,99,87,98,76,78]
marks.pop()
print(marks)


#Exercises

#Ex1 Create a list of 5 numbers and append 10 to it
numbers=[60,50,40,30,20]
numbers.append(10)
print(numbers)

#Ex2 Add multiple numbers [20, 30, 40) to the same list.
numbers=[60,50,80,99]
numbers.extend([20,30,40])
print(numbers)

#Ex3 Insert the number 5 at index 0 Of the list
numbers=[6,7,8,9,10]
numbers.insert(0,5)
print(numbers)

#Ex4 Insert the number 25 at index 3 of the list
numbers=[10,15,20,30,35]
numbers.insert(3,25)
print(numbers)

#Ex5 Remove the number 30 from the list
numbers=[10,15,20,30,35]
numbers.remove(30)
print(numbers)

#Ex6 Remove the last item from the list and print it
numbers=[10,15,20,30,35]
numbers.pop()
print(numbers)

#EX7 Remove the item at index 2 and print it.
numbers=[10,15,20,30,35]
numbers.pop(2)
print(numbers)

#Ex8 Find the index of 20 in the list
numbers=[10,15,20,30,35]
print(numbers.index(20))

#Ex9 Count how many times IO appears in the list.
numbers=[10,15,20,10,30,35,10]
print(numbers.count(10))

#Ex10 Sort the list in ascending order.
numbers=[10,90,50,30,70,60,20,100,40]
numbers.sort()
print(numbers)

#Ex11 Sort the list in descending order
numbers=[10,90,50,30,70,60,20,100,40]
numbers.sort(reverse=True)
print(numbers)

#Ex12 Reverse the list.
numbers=[10,90,50,30,70,60,20,100,40]
numbers.reverse()
print(numbers)

#Ex13 Clear all items from the list.
numbers=[10,90,50,30,70,60,20,100,40]
numbers.clear()
print(numbers)

#Ex14 Create a list of fruit names and add "mango" at the end.
fruits=["Apple","Guava","Orange","Banana"]
fruits.append("Mango")
print(fruits)

#Ex15 Insert "guava" at index 1 in the fruit list.
fruits=["Apple","Orange","Banana"]
fruits.insert(1,"Guava")
print(fruits)

#Ex16 Remove "banana" from the fruit list.
fruits=["Apple","Guava","Orange","Banana"]
fruits.remove("Banana")
print(fruits)

#Ex17 Add another list ("grapes", "orange") to the fruit list.
fruits=["Apple","Guava","Banana"]
fruits.extend(["Grapes","Orange"])
print(fruits)

#Ex18 Sort the fruit list alphabetically.
fruits=["Apple","Guava","Orange","Banana"]
fruits.sort()
print(fruits)

#Ex19 Reverse the fruit list.
fruits=["Apple","Guava","Orange","Banana"]
fruits.reverse()
print(fruits)

#Ex20 Count how many times "apple" appears in the fruit list.
fruits=["Apple","Guava","Orange","Apple","Banana"]
print(fruits.count("Apple"))

#Ex21 Create an empty list and add 1, 2, 3 using append().
numbers=[]
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)

#Ex22 Remove all items from the fruit list at the end.
fruits=["Apple","Guava","Orange","Apple","Banana"]
fruits.clear()
print(fruits)

#Ex23 Create a list Of 5 marks and find the highest mark.
marks=[10,90,50,30,70]
highest=max(marks)
print("highest marks", highest)

#Ex24 Find the lowest mark from the same list.
marks=[10,90,50,30,70]
lowest=min(marks)
print("Lowest Marks", lowest)

#Ex25 Remove the first occurrence of a specific number (e.g„ 50).
numbers=[10,15,20,10,30,35,10]
print(numbers.count(10))        #Occurrence = Number of times something appears

#Ex26 Check if a number (e.g„ 100) exists in the list.
numbers=[10,15,20,10,30,35,10]
if 100 in numbers:
    print("100 is exists in the list")
else:
    print("100 does not exists in the list")

#Ex27 Find the length of the list.
numbers=[10,15,20,10,30,35,10]
print(len(numbers))

#Ex28 Copy a list to another list and modify the new list.
numbers=[10,15,20,10,30,35,10]
new_num=numbers.copy()         #New List
new_num.append(9)
print(new_num)
print(numbers)

#Ex29 Find the sum Of all numbers in a list.
numbers=[10,15,20,10,30,35,10]
print(sum(numbers))

#Ex30 find the average of numbers in a list.
numbers=[2,8,10,9,12]
print(sum(numbers)/len(numbers))

#Ex31 Find the maximum and minimum values in a list.
numbers=[2,8,10,9,12]
print(max(numbers))
print(min(numbers))

#Ex32 Remove all even numbers from a list.
numbers=[2,8,10,9,12,11,5]
for i  in numbers[:]:
    if i%2==1:
        numbers.remove(i)
print(numbers)

#Ex33 Remove all odd numbers from a list.
numbers=[2,8,10,9,12,11,5]
for i in numbers[:]:
    if i%2==0:
        numbers.remove(i)
print(numbers)