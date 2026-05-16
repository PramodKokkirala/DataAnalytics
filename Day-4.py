'''
Concatiation- The (+) is used fro int and can add, but for the other data types it will act as concatinating the data type
Tuple- Collection of different data types separated by commas,represented in ()paranthesis and immutable
Methods-
1)count()-this is used to count the particular item in a tuple
Syntax-variable_name.count(item)
2)index()-this is used to get the index postion of the item , and only gives the first occurence

Dictionary- can only use integers,strings,tuple as a key
Dict is a key :value pair , kay and value is separated by (:) and pair is separated by comma
Represented by {}
Methods-
1)keys()-used to retreive all the keys of the dictionary
Syntax-dict.keys()
2)values()-used to retreive all the values of the dictionary
Syntax-dict.values()
3)items()-used to retreive all the keys and values of the dictionary
Syntax-dict.items()
4)update()-used to add a new key value pair
Syntax-dict.update({})
5)clear()-used to clear all the items in the dictionary
dict.clear()
'''

a=90
b=8
print(a+b)

any_="Python "
so="is a language"
print(any_+so)

an=[1,2]
am=[3,4]
print(an+am)

some=(1,"Python",[1,2],(3,4))
sim=(1,[1,2],[3,4],"Python")
print(some)
print(some[2][1])
print(some.index("Python"))
print(some.count("Python"))
print(sim.index("Python"))

any=(1,"python",(1,2,(34,"this is python 3rd Class",78),"Python is a language",89),34,(3,4))
print(any[2][2][1][7])

pramod_details={"Name":"Pramod",
              1:2,
              (1,2):[3,4]}
print(pramod_details)
print(type(pramod_details))

chaitu_details={"Name":"Chaitanya",
                "age":60,
                "Mobile":8341440910,
                "Pan":"HAJDB3526L"}
print(chaitu_details.keys())
print(chaitu_details.values())
print(chaitu_details.items())
print(chaitu_details["age"])
print(chaitu_details["Name"])
chaitu_details.update({"Aadhaar":123456789012})
print(chaitu_details.items())
chaitu_details["Name"]="Togi"
print(chaitu_details["Name"])
print(chaitu_details.items())
chaitu_details["Address"]="ajhhadhadbcuh"
print(chaitu_details["Address"])
print(chaitu_details.items())
chaitu_details.clear()
print(chaitu_details)


