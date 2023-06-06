
#Remove Element
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3]

# nums = [int(i) for i in input('enter values').split(',')]
# val = int(input('enter the value'))
# new=[]
#
# for i in nums:
#     if i!=val:
#         new.append(i)
# print(new)
# print('output:',len(new))
###########################################################
# c/100=f-32/180
#
# c/5 = f-32/9
#
# f = 9c/5  +32

# def fareheit(c):
#
#     f = 9*c/5 +32
#     print(f)
#
# fareheit(37)


##################################################
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Input: digits = [9]
# Output: [1,0]

# digits = [1,2,9]
# num =''
# for i in digits:
#     num+=str(i)
#
# num = int(num)+1
#
# output=[]
# for i in str(num):
#     output.append(int(i))
#
# print(output)
#############################################################
# check whether the input string is a palindrome or not



# if s==s[::-1]:
#     print('palindrome')
# else:
#     print('not palindrome')

# s = 'malayalam'
#
#
# for i in range(len(s)):
#     if s[i]!=s[-(i+1)]:
#         print('not palindrome')
#         break
# else:
#     print('palindrome')
##############################################################
# #Write a program to print the shape of a matrix.
# matrix=[ [5,6] ,
#          [15,4] ,
#          [9,80]]
#
# print('rows:',len(matrix))
# print('columns:',len(matrix[0]))

##########################################
#####Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
###between 2000 and 3200 (both included).
###The numbers obtained should be printed in a comma-separated sequence on a single line.

# for i in range(2000,3201):
#     if i%7==0 and i%5!=0:
#         print(i,end=',')





