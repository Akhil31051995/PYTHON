# sets
# s1 = {1,2,3,4,5}
# s2 = {89,50,12,123,3,5}
# # operations
# s2.remove(123)
# print(s2)
# s2.discard(50)
# print(s2)
#
# s2.pop()
# print(s2)
# print(s1|s2)
# print(s1&s2)
# print(s1-s2)
# print(s2-s1)

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.difference(s2))
# s1.update(s2)
# print(s1)


# DICTIONARY


# mutable,unordered,values are accessed using keys,does not allow duplicate keys,
# keys -- immutable data type


# data = {'class1':{'names':['anu','anil'],'marks':[85,80],'subjects':['phy','chemi']},
#         'class2':{'names':['sooraj','anirudh','adith'],'marks':[100,95,80],'subjects':'cs'}}

# data['class2']['names'][-1] = None
# data['class1']['subjects'][-1] = 'maths'
#
# del data['class2']
#
# del b['age']
# b['class teacher'] = 'raju'
# print(b)

# a = {'name':'sooraj','age':19,'height':172,'weight':60}
# b = {'names':['sooraj','adith','anirudh'],'age':(19,20,19),'av_height':172,'av_weight':60}

# # methods
# a.pop('age')
# print(a)
# a.popitem()
# print(a)
# a.popitem()
# # print(a)
#
# print(sorted(a))
#
# d1 ={1:1,2:4,3:9}
# d2 = {4:16,5:25,6:36}
# d1.update(d2)
# print(d1)










### conditions  if -else


# if num>0:
#     print('num is positive')
# elif num==0:
#     print('zero neither pos or neg')
# else:
#     print('num is negative')


# num = int(input('enter  no'))
# if num%2!=0:
#     print('odd')
# else:
#     print('even')


# # 90 -- A
# 80 -- B
# 70 -- C
#60-70 --D
# 60 -- below  fail
marks = int(input('enter marks'))
grace = 3
# if marks>=90:
#     print('A')
#     marks+=grace
#     print(marks)
# elif marks>=80:
#     print('B')
#     print(marks)
# elif marks>=70:
#     print('C')
#     print(marks)
# elif marks>=60:
#     print('D')
#     print(marks)
#
# else:
#     print('failed')
#     print(marks)
