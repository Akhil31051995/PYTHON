#
# a = lambda x,y:x*y
#
# print(a(5,4))



# try:
#     a = int(input('enter the value'))
#     b = 100
#     print(a+b)
# except ValueError:
#     print('check your input')





# class Cars:
#     def __init__(self,name):
#         self.name = name
#         self.welcome()
#
#     def display_name(self):
#         print(self.name)
#     def welcome(self):
#         print('Hello sir, welcome to our showroom')
#
#
# car1 = Cars('bmw')
# car2 = Cars('benz')



# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
# Suppose the following input is supplied to the program:
# 9
# Then, the output should be:
# 11106

# a+aa+aaa+aaaa


# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
# input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be
# printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.


# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3




# Example 1:
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.





###################################################
# a = ['hello','world','today',45,85]

# for i in range(len(a)):
#     print(i,a[i])

# for i,v in enumerate(a):
#     print(i,v)


# a = [1,2,3,4,500,40]
# b = ['a','b']
#
# for i,v in zip(a,b):
#     print(i,v)


##########################










# map={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
# s = "MCMXCIV"
# num=0
# last=0
# for i in  s[::-1]:
#     if map[i]>=last:
#         num+=map[i]
#     else:
#         num-=map[i]
#     last=map[i]
#
# print(num)








