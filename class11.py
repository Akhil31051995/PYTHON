# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
# input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be
# printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

# a = list(map(str,input('enter the binary numbers').split(',')))
#
# for i in a:
#     index=0
#     sum=0
#     for j in i[::-1]:
#         sum+=int(j)*(2**index)
#         index+=1
#     if sum%5==0:
#         print(i)


###################################################
# check whether the input string is a palindrome or not

# s = 'malayalam'
#
# for i in range(len(s)):
#     if s[i]!=s[-(i+1)]:
#         print('not palindrome')
#         break
# else:
#     print('Palindrome ')

##############################################
# l = [12,23,52,27]
# index=0
# sum = 0
# while index<len(l):
#     sum+=l[index]
#     index+=1
# print(sum)

##############################################
# *
# **
# ***
# ****
# *****

# for i in range(1,6):
#     for j in range(i):
#         print('*',end=' ')
#     print()
##########################################
# *****
# ****
# ***
# **
# *

# for i in range(1,6):
#     for j in range(6-i):
#         print('*',end=' ')
#     print()

##########################################
#     *
#    **
#   ***
#  ****
# *****

# for i in range(1,6):
#     for j in range(6-i-1):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     print()

########################################
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Input: digits = [9]
# Output: [1,0]

# a = list(map(str,input('enter the numbers').split(',')))
# b= str(int("".join(a))+1)
# print(list(map(int,b)))
####################################################

# a = [int(i) for i in input('enter values').split(',')]
# s = ''
# for i in a:
#     s+=str(i)
# num = int(s)+1
# output=[]
# for i in str(num):
#     output.append(int(i))
# print(output)

#######################################################

#####Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
###between 2000 and 3200 (both included).
###The numbers obtained should be printed in a comma-separated sequence on a single line.

# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         print(i,end =',')

#####################################
#Median of Two Sorted Arrays
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
#Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

# nums1 = [2,1]
# nums2 = [4,3]
#
# num = nums1+nums2
# num.sort()
#
# if len(num)%2!=0:
#     index = len(num)//2
#     median = num[index]
#     print(median)
# else:
#     index = (int(len(num)/2))-1
#     median = (num[index]+num[index+1])/2
#     print(median)

###################################################





###############################################################



