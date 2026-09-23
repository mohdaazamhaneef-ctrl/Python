data={}
print(type(data))
print(data)

data=dict()
print(type(data))
print(data)

#Values can be duplicate
data={"name1":"Aazam","age":24,"att":True,"name2":"Afzal"}
print(data)

#Keys can not be duplicate
data={"name":"Aazam","age":24,"att":True,"name":"Afzal"}
print(data)

#Dictionary is mutable
data={"name":"Aazam","age":24,"att":True}
print(data)
data["name"]="Afzal"
print(data)
print(data["name"])
print(data.get("name")) #Using key
print(data.get("Naeem"))  #Output= None

#Len()
data={"name":"Aazam","age":24,"att":True}
print(len(data))
print(data.values())
print(data.items())

#pop()
data={"name":"Aazam","age":24,"att":True}
data.pop("age")
print(data)

#pop()
data={"name":"Aazam","age":24,"att":True}
print(data.pop("age"))

#popitem()
data={"name":"Aazam","age":24,"att":True}
print(data.popitem())                              

#clear()
data={"name":"Aazam","age":24,"att":True}
data.clear()
print(data)

#copy() Ex1
data={"name":"Aazam","age":24,"att":True}
newData=data

data["name"]="Afzal"
print(newData)
print(data)

#copy() Ex2
data={"name":"Aazam","age":24,"att":True}
newData=data.copy()

data["name"]="Afzal"
print(newData)
print(data)

#In
data={"name":"Aazam","age":24,"att":True}
print("name" in data)
print("Aazam" in data.values())

#not in
data={"name":"Aazam","age":24,"att":True}
print("name" not in data)
print("Aazam" not in data.values())