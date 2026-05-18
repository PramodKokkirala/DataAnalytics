'''
sets-
-->A set is a collection of unique and unordered elements
-->Duplicaate values are not allowed
-->Items are not stored in index order
-->represented with {}(curly braces)

Methods-
1)union()-> gives all the values or elements from 2 sets together in one set
Syntax->variable_name.union(another variable_name)
2)intersection()-> gives the common elements from 2 sets
Syntax->variable_name.intersection(another variable_name)
3)difference()->to get uncommon elements or values from the set
Syntax->variable_name.difference(another variable_name)
4)add()->to add new element into set
Syntax->variable_name.add(element)
5)update()->to add new elements into set
Syntax->variable_name.update(list of elements)
6)remove()->used to remove or delete the element from the set,but will throw key error if given element is not present in set
Syntax->variable_name.remove(element)
7)discard()->used to remove or delete the element from the set,but will not throw any error is given element is not present in set
'''
any={1,2,2,3,4}
print(any)

any={1,2,2,3,4}
an={56,34,86,74}
print(any | an)
print(any.union(an))
print(sorted(any | an))

an=[56,34,86,74]
print(set(an))

a={1,2,3,4}
b={5,4,3,2}
print(a & b)
print(a.intersection(b))

a={1,2,3,4}
b={2,5,4,1}
print(a and b)

a = {1,2,3,4}
b = {3,4,5,6}
print(a.difference(b))
print(b.difference(a))

any={1,2,2,3,4}
any.add(41)
print(any)

any={1,2,2,3,4}
any.update([41,42])
print(any)

any={1,2,2,3,4}
print(sum(any))

any={1,2,2,3,4}
print(min(any))

any={1,2,2,3,4}
print(max(any))

any={1,2,2,3,4}
any.remove(2)
print(any)

any={1,2,2,3,4}
any.discard(2)
print(any)
