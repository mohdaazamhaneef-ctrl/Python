#Ending         range(10)
#Start, End     range(1,10)
#Start,End,Step range(1,10,1)

for i in range(1,10,1):
    print(i)


data=[43,54,65,23,76,87]
for i in data:
    print(i)
print(data)


data="PYTHON"
for i in data:
    print(i)

for i in range(1,21,1):
    if (i%2==0):
        print(i)

for i in range(2,21,2):
    print(i)

for i in range(1,21,1):
    if (i%2!=0):
        print(i)

for i in range(5,51,1):
    if (i%5==0):
        print(i)

sum=0
for i in range(1,11,1):
    sum+=i
print(sum)

sum=0
for i in range(1,21,1):
    if (i%2==0):
        sum+=i
print(sum)