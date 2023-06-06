## functions

# def welcome():
#     print('hello , welcome to our class')
#
#
# welcome()

# single argument

# def welcome(name):
#
#     print(f"Hello,welcome {name}")
#
# welcome('Rahul')

# positional arguments

# def div(num1,num2):
#     div = num1/num2
#
#     print('div:',div)
#
# div(10,30)
# div(30,10)

# keyword arguments

# def three_sum(a=10,b=10,c=5):
#     sum = a+b+c
#     return sum,a+5,b**2,c**3
#
# a,b,c,d = three_sum(a=20,c=5)
# print(a)
# print(b)
# print(c)
# print(d)

## 2 nos -- basic ---return ---store variable



# def basic_operations(a,b):
#     sum = a+b
#     diff = a-b
#     prod = a*b
#     div = a/b
#     # local
#     return sum,diff,prod,div
#
#
# newsum,difference,product,division = basic_operations(50,20)


# write a function to find the factorial of a number
# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact*=i
#     return fact
#
# print(factorial(5))


# Lambda functions --- anonymous functions.

# a = lambda x:x**5
#
# print(a(5))
#
#
# b = lambda x,y : x*y
# print(b(56,12))

###################################################################

#find length of a string without using len() fn
# str = 'welcome'
# length = 0
# for i in str:
#     length+=1
# print(length)


#User will input (2numbers).Write a program to swap the numbers

# a = 100
# b = 50
# # temp = b
# # b=a
# # a=temp
# # print(a,b)
#
# a,b = b,a
# print(a,b)

#Print the first 20 numbers of a Fibonacci series
# a=0
# b=1
# print(a)
# print(b)
# for i in range(18):
#     sum = a+b
#     a,b = b,sum
#     print(sum)


#print all factors of a given no by user
#
# num = int(input('enter no'))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i)

# ## join the strings to a single string
# li= ['my','name','is','farhan']
# str = ''
# for i in li:
#     str+=i
#     str+=' '
# print(str)



# Write a program that accepts a sentence and calculate the number of letters and digits.
#hello world! 123
# LETTERS 10
# DIGITS 3

# str ='hello world! 123'
# c = 0
# d = 0
# for i in str:
#     if i.isalpha():
#         c+=1
#     elif i.isdigit():
#         d+=1
# print('letter:',c,'digits:',d)


# *
# **
# ***
# ****
# *****

# for i in range(1,5): # 1,2,3,4
#     for j in range(i):# 0,01,012,
#         print('*',end='')
#     print()
#

##################
#Count the number of vowels in a string provided by the user.

# vow='aeiou'
# str='HELLOworld'
# count = 0
# for i in str.lower():
#     if i in vow:
#         count+=1
#
# print(count)

######################################

# num = int(input('enter the number'))
#
# for i in range(2,num//2):
#     if num%i==0:
#         break
# else:
#     print('prime number')

###################################
#count the no of vowels in the string -- user ---{'a':5,'e':8,'i':8.....}
## count of chars
# string1 = "I am in kozhikode, and today is a wonderful day" -- dict format

# ##################################
# st = input('enter the string')
# d={}
# vow = 'aeiou'
# for i in vow:
#     count = 0
#     for j in st.lower():
#         if j==i:
#             count+=1
#     d[i]=count
#
# print(d)
########################################
# count of chars
# string1 = "I am in kozhikode, and today is a wonderful day"
# se = set(string1)
# chars={}
# for i in se:
#     if i!=' ' and  i!=',':
#         count =0
#
#         for j in string1:
#             if i==j:
#                 count+=1
#         chars[i]=count
# print(chars)
#####################################
# prime range
# lower,upper = tuple(map(int,input('enter upper and lower limit').split(',')))
#
# for i in range(lower,upper+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

##########################################

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# n = int(input('no of terms '))
# num = input('enter the number')
# sum = 0
# for i in range(1,n+1):
#     sum+=int(num*i)
# print(sum)
####################################################
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
# input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be
# printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

# a = list(input('enter binary').split(','))
#
# for i in a:
#     index = 0
#     sum=0
#     for j in i[::-1]:
#         sum+=int(j)*(2**index)
#         index+=1
#
#     if sum%5==0:
#         print(i)
###############################################################

#Write a python program to find the max item from a list without using the max function
#Write a python program to reverse a list
####  Write a program that can convert a 2D list to 1D list
### Write a program that can print
#list_2d=[ [5,6,7,7] , [5,4,6,7] , [9,8,9,10] ]
###  Write a program that can perform union and intersection on 2 given list.
# l1=[1,2,5,4,6,89,7]
# l2=[4,5,6,6,8,4,7]
### Write a program to print the shape of a matrix.

#matrix=[ [5,6,10,7] , [15,4,16,7] , [9,80,19,10],[1,5,8,99] ]













