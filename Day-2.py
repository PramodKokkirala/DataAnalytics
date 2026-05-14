'''
Operators:
1.Arithmetic-  +,-,*,/,%,//,**
Example:print(2*3)
        print(4%5==0)
        print(10**2)
        print(10/2)
        print(35.20//5)
        
2.Assignment-  =,+=,-=,%=,*=
Example:count=0
        for j in range(1,10):
            count +=1 or count=count+1
        print(count)
        
3.Comparision-  ==,!=,>=,<=,<,>
== looks for both are equal or not
Ex:a=7
   b=9
   print(a==b)


4.Logical- and,or,not
1)and operator is used to check if both should be true
2)or operator is used to check if any one of both should be true
Ex:a=15
   if(a%3==0 and a%5==0):
      print("True")
   a=5
   if(a%3==0 or a%5==0):
      print("True")

5.Membership- in,not in
Ex:
a=7
b=[1,2]
print(a not in b)

a=7
b=[1,2,7,8]
print(a in b)

6.Identity-  is,is not
is operator looks for the object is same or not
Ex:a=[1,2]          
   b=[1,2]
   c=a
   print(a==b)
   print(id(a))
   print(id(b))
   print(id(c))
   print(a is c)
   print(a is not b)
   
7.Bitwise- &,|,<<,>>
Ex:print(5&3)
   print(5|3)
   print(5>>3)
   print(5<<3)
'''
print(2*3)
print(4%5==0)
print(10**2)
print(10/2)
print(35.20//5)

count=0
for j in range(1,10):
    count +=1 
print(count)

a=7
b=9
print(a==b)

a=[1,2]
b=[1,2]
c=a
print(a==b)
print(id(a))
print(id(b))
print(id(c))
print(a is c)
print(a is not b)
'''
Note:1)== looks for both are equal or not
     2)is operator looks for the object is same or not
'''

a=15
if(a%3==0 and a%5==0):
    print("True")
a=5
if(a%3==0 or a%5==0):
    print("True")


a=7
b=[1,2]
print(a not in b)

a=7
b=[1,2,7,8]
print(a in b)


print(5&3)
print(5|3)
print(5>>3)
print(5<<3)

'''
a=9 # immutable
b=7.0
print(a+b)
'''

'''
1)String-  '',"",''''''
Note:
 String is sequence of characters that are enclosed in '',"",''''''
 String is immutable data

2)Methods-
1)replace()-Used to replace new subString
Syntax--> variable_name.replace("oldstring","newstring")

2)Split()-Used to separate into parts,and it will split based on the substring where before substring is one index and after is another index
Syntax--> variable_name.split("substring")

3)len()-Used to get number of values , substring
Syntax--> len(variable_name)

4)slicing()-can give the access to get particular part/Index from the string
Syntax--> variable_name[starting index : ending index]

5)Indexing()-used to get substring present in that index position
Syntax--> variable_name[index position]
join()-->"substring".join(variable_name)
'''

any="Pyhton78,&"
for j in any:
    print(j)

any="Python is a language"
print(any.replace("Python","Java"))
print(any)

any="Python is a language"
print(any.split("is"))

any="Python is a language"
print(any.split("$"))

any="Python is a language"
print(len(any))

any="Python is a language"
print(any[3:11])

any="Python is a language"
print(any[3])

print(any.index("ang"))

