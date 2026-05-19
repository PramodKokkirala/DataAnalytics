'''
Type conversions
1)int-->

an=78
us=str(an)
om=float(an)
print(om)
print(us)
print(type(om))
print(type(us))


an="pyhton"
ear=int(an)
print(type(ear))


an="90"
ear=int(an)
print(type(ear))

2)float-->

an="90"
ear=float(an)
print(type(ear))

3)List-->

an="90"
ear=list(an)
print(type(ear))
print(ear)

4)tuple-->

an="90"
ear=tuple(an)
print(type(ear))
print(ear)

'''
car=90.78
print(int(car))
print(str(car))
for j in str(car):
    print(j)

Any=[6,7]
print(str(Any))
print(tuple(Any))

how=(4,5)
print(list(how))
print(str(how))

num=int(input("Enter a number: "))
print(89+num)

'''
int as a user-input
num=int(input("Enter a number: "))
print(89+num)

string as a user-input
some=input("Write a Text: ")
print(some)


'''
some=input("Write a Text: ")
print(some)

any=input("Enter number: ").split()
print(any)

'''
List as a user-input
any=list(map(int,input("Enter numbers: ").split()))
print(any)
'''

any=list(map(int,input("Enter numbers: ").split()))
print(any)

any=tuple(map(int,input("Enter numbers: ").split()))
print(any)

num=eval(input("Enter :"))
print(type(num))
