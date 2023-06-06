# Tuples
#immutable,ordered,duplicates

a = (6,5,7.8,5,5,5,5,'hello',True)



# tuple ---- > list
# a = list(a)
# a[-2] = "hello world"
# a = tuple(a)
# print(a)

# b = ('happy day',)
# print(a+b)

# del a
# print(a)

# tuple unpacking

# a,*b,c = ('hello','world',True,1235,'india')
#
# print(a)
# print(b)
# print(c)

# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (fruit1,fruit2,*fruit3) = fruits
#
# print(fruit1)
# print(fruit2)
# print(fruit3)

# a,*b,c = ['hello','world',True,1235,'india']
#
# print(a,b,c)

# # zipping
# a = (1,2,3)
# b = (4,5,6)
#
# c = tuple(zip(a,b))
# print(c)

# tuple functions
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# print(sorted(fruits,reverse=True))

#print(sum(a))
# len,max,min,sorted,sum

#a = (1,2,2,5,'hello','roses',56,2,56,True,0)

# tuple methods
#print(a.count(False))

#print(a.index('roses'))

## SETS

#unordered,mutable,set does not allow dulicate values,set only allows immutable data types.

a = set()

b = {1,2,3,45,89,-1,20}

# methods
# add
# b.add('world')
# print(b)
# # update method
#
# b.update(['hello',1000,True])
# b.update(('new','day',(1,2,3,4)))
# print(b)

# remove
#b.pop()
#b.remove(89)

# b.discard(20)
# print(b)

# b.clear()
# print(b)

# operations
s1 = {1,5,8,10,-1,-10,-30,99}
s2 = {3,4,5,6,7,8,9}
# print(s1|s2)
# print(s1&s2)
# print(s1-s2)
# print(s2-s1)
# print(s1^s2)

#print(sum(s1))

### methods
# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))

x = {1,2,3,7,8,9}
y = {1,2}

# print(x.issuperset((y)))
# print(y.issubset((x)))
z = y.copy()
# print(z)

##################################################
#DICTIONARY

# collection of key value pairs -- mapping
# mutable,unordered,duplicate keys are not allowed, key should be immutable datatype

a = {'name':'Raju','age':26,'height':160,'marital status':'yes'}
b = {'name':'Raju','age':26,'height':160,'marital status':'yes',(1,2,3):5000}

c = {'name':['raju','ramu','sakshi','kavya'],'age':[20,21,15,9],
     'subjects':{'physics':50,'chemistry':30,'maths':50,'english':65}}


##
details ={"class1":{'studentno':35,'pass_percent':85,'class teacher':'smitha'},
          "class2":{'studentno':25,"pass_percent":75,'class teacher':'Ajitha'}}


print(details)

### elements access & modify

### search --
#user input two values --- and perform basic mathematical operations on them.
## user input list -- check








