# a = []
# for i in range(1,101):
#     a.append(i)
# #
# print(a)

# list comprehension

# b =[i for i in range(1,101,2)]
# print(b)
# c= [ i for i in range(5,51,5)]
# #print(c)
#
# d=[45,23,56,98,74,121]
# new = [ i if i%2==0 else i**2 for i in d ]
# print(new)

# st = 'MoHAnLaL'
#
# new =[ i if i.isupper()==True else i.upper() for i in st]
# print(new)

# st = list(input('enter the list'))
# print(st)

# n = int(input('etra number venam?'))
# li=[]
# for i in range(n):
#     num = int(input('enter your number'))
#     li.append(num)
#
# print(li)


# new = [int(i) for i in input('enter the numbers').split(',') if int(i)%2==0]
# print(new)

# dictionary comprehension

# d = { i:i**2 for i in range(11) if i%2==0}
# print(d)
#
# di = { i:0 for i in 'abcdefghijklmnopqrstuvwxyz'}
# print(di)


# st = 'have a wonderful day'
# vow ='aeiou'
#
# d={ i:0 for i in vow}
#
# for i in vow:
#     for j in st:
#         if i==j:
#             d[i]+=1
#
# print(d)

# *
# **
# ***
# ****
# *****


