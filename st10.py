# loop control statements

# functions

# def welcome(name):
#     print(f'Hello,welcome to our class {name}')
#
#
# welcome('anirudh')

# positional arguments
#
# def div(a,b):
#     div = a/b
#     print(div)
#
#
# div(10,20)
# div(20,10)

# keyword arguments

# def summing(a=0,b=0,c=0):
#     sum = a+b+c
#     print(sum)
#
# summing(5,10,15)
#
# def summing(a=0,b=0,c=0):
#     sum = a+b+c
#     return sum

# def basic(num1,num2):
#     add = num1+num2
#     div  = num1/num2
#     multi = num1*num2
#     sub = num1-num2
#     return add,div,multi,sub
#
# a,d,m,s = basic(50,15)
#
# print(m**2)

# function to find factorial of a number
# def factorial(num):
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     return fact
#
#
# print(factorial(5))

# function to find length of string
# def str_length(str):
#
#     length = 0
#     for i in str:
#         length+=1
#     return length
#
# print(str_length('hello world'))

# lambda function

# a = lambda x,y:x*y
#
# print(a(5,4))

# l=['abc','aBc','OmY']
# string = ''
# for i in l:
#     for j in i:
#         if j.isupper()==True:
#             string+=j
#
# print(string)
# new = [[1,5,6],[56,74],[84,95,22],[2,0,134]]
#
# even = []
# for i in new:
#     for j in i:
#         if j%2==0:
#             even.append(j)
#
# print(even)

l = ['hello','world','today','holiday']
new=[]
for i in l:
    new.append(len(i))

print(new)