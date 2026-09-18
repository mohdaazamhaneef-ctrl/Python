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
