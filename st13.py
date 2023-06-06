
# all factors of a number
# num = int(input('enter the number'))
# for i in range(1,num+1):
#     if num%i==0:
#         print(i,end=",")

# check armstrong numbers

# '153'

# num = input('enter the number')
# sum=0
# for i in num:
#     sum+=int(i)**len(num)
#
# if sum==int(num):
#     print('armstrong')
# else:
#     print('not armstrong')
#
# # 8208, 9474, 54748










## Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106
# a+aa+aaa+aaaa
# num = '9'
# sum=0
# for i in range(1,5):
#     sum+=int(num*i)
#
#
# print(sum)











#########################################################
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
#
# s ='Hello world!'
# upper =0
# lower = 0
# for i in s:
#     if i.isupper():
#         upper+=1
#     if i.islower():
#         lower+=1
#
# print("upper:",upper)
# print("lower:",lower)


# ### special characters
# s='@#hell#o@123% wo#r@ld@'
# count1 =0
# count2=0
# for i in s:
#     if i=='@':
#         count1+=1
#     if i=='#':
#         count2+=1
#
# print(count1,count2)

#########################################
# string = input('enter the string')
# count1=0
# count2=0
# for i in string:
#     if i.isalpha():
#         count1+=1
#     if i.isdigit():
#         count2+=1
# print(count1,count2)












################################################################3
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

# pattern printing
########################################
# 2
# 2 4
# 2 4 16
# 2 4 16 256

#1,2,4,8 --- var *2

# for i in range(1,6):
#     var = 2
#     for j in range(1,i):
#         print(var, end = ' ')
#         var**=2
#     print()


##################################

# s='python'
#
# for i in range(1,len(s)+1):
#     for j in range(i):
#         print(s[j],end=' ')
#     print()

################################

