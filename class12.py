# *
# **
# ***
# ****
# ***
# **
# *
#
# for i in range(1,5):
#     for j in range(i):
#         print('*',end=' ')
#     print()
# for i in range(1,4):
#     for j in range(4-i):
#         print('*',end=' ')
#     print()


#     *
#    ***
#   *****
#  *******
# *********

# for i in range(1,5):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i-1):
#         print('*',end=' ')
#
#     print()


#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

# for i in range(1,4):
#     for j in range(5-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i-1):
#         print('*',end=' ')
#     print()
#
# for i in range(1,5):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(5-i):
#         print('*',end=' ')
#     for j in range(5-i-1):
#         print('*',end=' ')
#     print()

###################################################

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



# map = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
#
# s = "MCMXCIV"
# sum=0
#
# for i in range(len(s)):
#     if i<len(s)-1:
#         if map[s[i]]>=map[s[i+1]]:
#             sum+=map[s[i]]
#         else:
#             sum-=map[s[i]]
#     else:
#         sum+=map[s[i]]
#
#
# print(sum)

#############################################################

#Remove Element
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]

#
# nums = [0,1,2,2,2,2,3,0,4,2]
# val = 2
# new = []
# for i in nums:
#     if i!=val:
#         new.append(i)
#
# print(new)

#
# s='PAYPALISHIRING'
# numRows=3
# def zigzag(s,numRows):
#
#     if(numRows  < 2):
#         return s
#
#     arr = ['' for i in range(numRows)]
#     direction = 'down'
#     row = 0
#     for i in s:
#         arr[row] += i
#         if row == numRows-1:
#             direction = 'up'
#         elif row == 0:
#             direction = 'down'
#         if(direction == 'down'):
#             row += 1
#         else:
#             row -= 1
#     return (''.join(arr))
#
# print(zigzag(s,numRows))
#


