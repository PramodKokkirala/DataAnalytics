'''
1.Program to convert 24h clock into normal clock

time_=input("Enter 24 hours time: ")
parts_=time_.split(":")
hour_=int(parts_[0])
min_=int(parts_[1])
print(f"{time_} is converted into {hour_ - 12}:{min_} pm")

List-
List is a collection of different data type
Represented in [](square brackets) seperated by ,(commas)
Mutable
'''
any=[1,"python",[1,2,[34,"this is python 3rd Class",78],"Python is a language",89],34,[3,4]]
print(any[2][4])
print(any[2][2][1][8])


'''
methods-
1)append()=this method is used to add new item into list, and it will in the lat index position
Syntax-->variable_name.append(item)

2)extend()=this method is used to add iterable into the list, and it will in the last index position, each value or substring is each is each index in the list
Syntax-->varibale_name.extend(iterable)

3)pop()=This is used to remove the item from the list, but will mention here index position in the pop method
Syntax-->variable_name.pop(index_position)

4)remove()=This is used to remove item from list,but will mention here direct value in the remove method
Syntax-->variable.name.remove(value)
'''
any=[1,2,3]
any.append(6)
print(any)
any.extend([20,19,22])
any.append([20,90])
print(any)

'''
Immutable-->could not able to modify on that particluar variable
Ex:Int,String
Mutable-->could able to modify on that particular variable
Ex:List
'''
so="python is a language"
print(so.replace("python","java"))
print(so)
any=[1,2,3]
any.append(6)
print(any)


any=[1,2,3]
print(any.pop(0))
print(any)

any=[1,2,3]
any.remove(3)
print(any)

so=["Python",90,"Java"]
so.remove("Python")
print(so)
