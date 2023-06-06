# dictionary

#person = {'name':'Arjit','age':20,'height':175,'weight':65}

# for i,v in person.items():
#     print(i,v)

# dictionary comprehension

# 10 ---square

# d={ i:i**2 for i in range(1,11) if i%2==0 }
# print(d)

# for i in range(1,11):
#     d[i]=i**2
#
# print(d)

##############################################
#count the no of vowels in the string -- user ---{'a':5,'e':8,'i':8.....}

# string = input('enter the string')
# vow='aeiuo'
# vow={ i:0 for i in vow}
#
# for i in vow:
#
#     for j in string.lower():
#         if i==j:
#             vow[i]+=1
#
#
#
# print(vow)

####################################

## count of chars
# string1 = "I am in kozhikode, and today is a wonderful day"
# char = set(string1)
# d={}
# for i in char:
#     if i!=" " and i!=",":
#         count =0
#         for j in string1:
#             if i==j:
#                 count+=1
#         d[i]=count
#
# print(d)
################################
# string1 = "I am in kozhikode, and today is a wonderful day"
# d= { i:0 for i in string1 if i!=" " and i!=","}
#
# for i in d:
#     for j in string1:
#         if i==j:
#             d[i]+=1
#
# print(d)

#########################################

# # prime in a range
# lower,upper = tuple(map(int,input('enter the ranges').split(',')))
#
# for i in range(lower,upper+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

#############################################

# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# n = int(input('enter the number of terms'))
# num= input('enter the number')
# sum = 0
# for i in range(1,n+1):
#     sum+=int(num*i)
#
# print(sum)
#################################################################
# #### Write a program to print the shape of a matrix.
# matrix=[ [5,6,10] ,[15,4,16] , [9,80,19], [1,5,8] ]
#
# print(len(matrix),len(matrix[0]))

######################################################

# max of a list -- without using max function

# l1=[7,20,5,40,6,89,74]
# max = l1[0]
# for i in l1:
#     if i>max:
#         max=i
#
# print(max)

#####################################################
###  Write a program that can perform union and intersection on 2 given list.
# l1=[1,5,2,5,4,6,6,89,7,7]
# l2=[4,5,6,6,8,4,7]
# ints=[]
# for i in l1:
#     if i in l2 and i not in ints:
#         ints.append(i)
#
# print(ints)

################################
# list_2d=[ [5,6,7,7] , [5,4,6,7] , [9,8,9,10] ]
# # 2d ---1d
# new=[]
# for i in list_2d:
#     new+=i
# print(new)

#########################################
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
# input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be
# printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
################################################################

# ## palindrome
# s ='malayalam'
# for i in range(len(s)):
#     if s[i]!=s[-(i+1)]:
#         print('not palindrome')
#         break
# else:
#     print('palindrome')
#########################################
# pattern printing -- inverted triangle

# for i in range(5,-1,-1):
#     for j in range(i):
#         print('*',end = ' ')
#     print()

###################################
# normal triangle
# for i in range(1,6):
#     for j in range(i):
#         print('*',end = ' ')
#     print()

###############################
# for i in range(1,5):
#
#     for j in range(5-i):
#         print(' ',end = ' ')
#     for l in range(i):
#         print('#', end=' ')
#     print()
#
##################################

# for i in range(1,5):
#
#     for j in range(i):
#         print(' ',end = ' ')
#     for l in range(5-i):
#         print('#', end=' ')
#     print()
###################################
# triangle
# for i in range(1,5):
#
#     for j in range(5-i):
#         print(' ',end = ' ')
#     for l in range(i):
#         print('#', end=' ')
#     for k in range(i-1):
#         print('*',end=' ')
#     print()
###################################
# for i in range(1,5):
#
#     for j in range(5-i):
#         print(' ',end = ' ')
#     for l in range(i):
#         print('#', end=' ')
#     for k in range(i-1):
#         print('*',end=' ')
#     print()
# for i in range(2,5):
#
#     for j in range(i):
#         print(' ',end = ' ')
#     for l in range(5-i):
#         print('#', end=' ')
#     for k in range(5-i-1):
#         print('*',end=' ')
#     print()
#
###########################################

# example 1:
#
# Input: digits = [1,2,3]
#
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
#
# Incrementing by one gives 123 + 1 = 124.
#
# Thus, the result should be [1,2,4].
#
# Example 2:
# Input: digits = [4,3,2,1]
#
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
#
# Incrementing by one gives 4321 + 1 = 4322.
#
# Thus, the result should be [4,3,2,2].
#
# Example 3:
# Input: digits = [9]
#
# Output: [1,0]

################################################
# Median of Two Sorted Arrays
#
# Example 1:
#
# Input: nums1 = [1,3], nums2 = [2]
#
# Output: 2.00000
#
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
#
# Input: nums1 = [1,2], nums2 = [3,4]
#
# Output: 2.50000
#
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

#############################################################################
# Remove Element
#
# Example 1:
#
# Input: nums = [3,2,2,3], val = 3
#
# Output: 2, nums = [2,2,_,_]
#
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Example 2:
#
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
#
# Output: 5, nums = [0,1,4,0,3,_,_,_]

############################################################################

#####Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
###between 2000 and 3200 (both included).
###The numbers obtained should be printed in a comma-separated sequence on a single line.


################################################################
# Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

###############################################################
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V = 5, III = 3.
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

#############################################################



