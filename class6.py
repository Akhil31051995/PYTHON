## list methods

values = [4,66,6,46234,4,646]

# append
# values.append('hello')
# print(values)
#
# values.append([1,2,3])
# print(values)

# extend

new = [1,5,True]
#print(values+new)
# values.extend(new)
#
# new.extend(values)
# print(new)

# insert

# li = [1,2,5,6,9]
# li.insert(2,'hello')
# print(li)

li = [1,2,5,6,'hello','happy day',9]
li.remove('hello')
# print(li)

# pop
# li.pop()
# print(li)
#
# li.pop(3)
# print(li)
#
# li.clear()
# print(li)

# new = [1,2,3,5,6,8,9]
#
# new.sort(reverse=True)
# print(new)

### Tuples

a=(1,1,2,3,4,5,7,8)
b=(24,6,8,6,5,4)
# print(a)
# print(b)
# del a[-2]



a=('good mornig',)
#print(type(a))
# b=[1]
# #print(b)
#
#
# a=(1,4,5,5,7,-5,-3)
#
# #print(sorted(a,reverse=2))
#
#
# print(a.count(5))

## SETS
a = {1,5,6}
b = {5,8,9}

a.update(b)
print(a)
