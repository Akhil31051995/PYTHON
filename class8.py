# for loops

# nested for loop

# for i in range(4):
#     print('*******')
#     for j in range(5):
#         print('nested loop')

new = [[1,5,6],[56,74],[84,95,22],[2,0,134]]

# maximum = []
# for i in new:
#     maximum.append(max(i))
# print(maximum)
even =[]
# even numbers --- extract --- list
for i in new:
    for j in i:
        if j%2==0:
            even.append(j)

#print(even)







# str = ['mMasa','mnON','dsDgAy','sYs'] #-----> create a string with only capital char in the list
#
# new = ''
# for i in str:
#     for j in i:
#         if j.isupper()==True:
#             new+=j
# print(new)

li = [454,5,454,45,45,8487,787,9]
# sum

# sum =0
# for i in li:
#     sum+=i
# print(sum)

# while loop --
# index = 0
# sum=0
# while index<len(li):
#     sum+=li[index]
#     index+=1
# print(sum)

## user input list of numbers creation
# new=[]
# n = int(input('enter the number of values to add'))
# for i in range(n):
#     num = int(input('enter the value'))
#     new.append(num)
#
# print(new)

# a = list(map(int,input('enter the numbers').split(',')))
# print(a)

# list of first 10 numbers
# list comprehension

# list if even --

# a = [ i for i in range(100,200) if i%2==0]
# print(a)

# b = [ i**2 if i%2==0   else i**3 for i in range(10,20)]
# print(b)


st = [1,2,3]
alpha=['a','b','c','d','e','f']
# for i in range(len(st)):
#     print(i,st[i])

# for i,v in enumerate(st):
#     print(i,v)

# for i,v in zip(st,alpha):
#     print(i,v)

##############################################################
# reverse a string without using any known methods--general--   'hello'---->'olleh'
# st = 'hello'
# x = ''
# for i in range(len(st)-1,-1,-1) :
#     x+=st[i]
#
# print(x)

###############
#    'hoLLyWoOd' --- 'HOllYwOoD'  swapcase without using method
# st ='hoLLyWoOd'
# new = ''
# for i in st:
#     if i.isupper()==True:
#         new+=i.lower()
#     else:
#         new+=i.upper()
#
# print(new)

##############################
# num = input('enter the number')
# index = 0
# sum = 0
# while index<len(num):
#     sum+=(int(num[index]))**len(num)
#
#     index+=1
# if sum==int(num):
#     print('armstrong')
# else:
#     print('not armstrong')
########################################

#Count the number of vowels in a string provided by the user.
#Print the first 20 numbers of a Fibonacci series -- for & while

##########################################################
# join a string using while loop
# find the sum of a list using while
## zip and enumerate

##############################################################
#User will input (2numbers).Write a program to swap the numbers


# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3


##############################################################
#find length of a string without using len() fn
## count of chars
# string1 = "I am in kozhikode, and today is a wonderful day"

###################
#count the no of vowels in the string -- user
#print first 20 nos of a fibonocci series
#print all factors of a given no by user
###################################################
# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# a+aa+aaa+aaaa
##################################################


