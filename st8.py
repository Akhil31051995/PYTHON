#while

# print all even numbers less than 20 using while loop

# find sum of first 20 numbers
# a=1
# sum = 0
# while a<=20:
#     sum=sum+a
#     a+=1
#
# print(sum)

# find factorial of a given number(user input)
# num =int(input('enter the number'))
# s=1
# fact = 1
# while s<=num:
#     fact=fact*s
#     s+=1
# print(fact)


# new = (45,56,23,89)
# sum =0
# index = 0
# while index<len(new):
#     sum+=new[index]
#     index+=1
#
# print(sum)

#new = [1,2,85,96,74,56,45,23,47]

# odd = []
# even=[]
#
# index = 0
# while index<len(new):
#     if new[index]%2==0:
#         even.append(new[index])
#     else:
#         odd.append(new[index])
#
#     index+=1
#
# print(odd)
# print(even)

# l = [45,52,62,1]
#
# index = 0
# product = 1
# while index<len(l):
#     product*=l[index]


#     index+=1
# print(product)


# new_list = ['my','name','is','raju']
#
# # while -- single string
# st =" "
#
# index = 0
# while index<len(new_list):
#     st+=new_list[index]
#     st+=" "
#
#     index+=1
#
# print(st)

# find the sum of digits of a given number ---145263--while

num = input('enter the number')
index = 0
sum = 0
while index<len(num):
    sum =sum+int(num[index])

    index+=1

print(sum)