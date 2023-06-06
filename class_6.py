## dictionary
#
# a = {'name':'Raju','age':20,'height':178,'subject_score':{'phy':80,'chemi':50,'maths':90}}
#
# a['subject_score']['chemi'] = 100
#
# # dictionary using constructor
# b = dict([('name','Akhil'),('age',20),('height',175)])
# print(b)
#
# b['weight'] = 70
# print(b)
#
# data = {'name': 'Akhil', 'age': 20, 'height': 175, 'weight': 70}
# new_data = {'place':'Kozhikode','company':'Futura labs'}
# dict methods
# update
#data.update(new_data)
#print(data)

# print(data.keys())
# print(data.values())
# print(data.items())

## remove
#
# data.pop('name')
# print(data)
#
# data.popitem()
# print(data)
#
# data.popitem()
# print(data)

#new_data = {'age': 20, 'height': 175, 'weight': 70,'name':'Rahul','company':'Infosys'}

# del new_data['weight']
# print(new_data)
#
# new_data.clear()
# print(new_data)
# del new_data
# print(new_data)

## functions
# print(len(new_data))
# print(sorted(new_data))
# print(new_data.values())
# print(175 in new_data.values())


######### if - else conditions
# user_age = int(input('enter your age'))
# age = 50
#
# if user_age<age:
#     print('age is less than 50')
# elif user_age==age:
#     print('age is 50')
# else:
#     print('age is greater than 50')

## write a program to check if a number inputed by user is odd or even
## write a program to check if number given by user is positive or negative

# num  = int(input('enter no'))
#
# if num>0:
#     print('positive no')
# elif num==0:
#     print('zero neither pos or neg')
# else:
#     print('negative no')

# # 90 -- A
# 80 -- B
# 70 -- C
# 60 -- below  fail

# marks = int(input('enter marks'))
#
# if marks>=90:
#     print('grade A')
# elif marks>=80:
#     print('grade B')
# elif marks>=70:
#     print('grade C')
# elif marks>=60:
#     print('grade D')
# else:
#     print('failed')

#list --- sum --- odd


new = [4,5,55,5554,5,978]

# s = sum(new)
# if s%2==0:
#     print('sum is even')
# else:
#     print('sum is odd')

# nested if
# age = 25
# height = 175
#
# if age>20:
#     print('eligible for recruitement')
#     if height>183:
#         print('above 6 ft')
#     else:
#         print('below 6 ft')
#
# else:
#     print('not eligible')

################################################################

# while loops --- condition

# a = 7
# while a>=0:
#     print('hello world')
#     a-=2

# print all odd numbers less than 20 using while loop

# a = 1
# while a<=20:
#     if a%2!=0:
#         print(a)
#     a+=1


# a = list(map(int,input('enter the values').split(",")))
# print(a)

# a=0
# num=int(input('enter the no of values'))
# new_list = []
# while a<num:
#     value = int(input('enter values'))
#     new_list.append(value)
#     a+=1
# print(new_list)




################

# a = 0
# num = int(input('enter the no of values'))
# list1 = []
# while a<num:
#     val = int(input('enter your value'))
#     list1.append(val)
#     a+=1
#
# print(list1)

# list of values user input - even / odd lists --seperate lists
# program to find the sum of first n numbers using while loop
# program to find the factorial of a given number -- while

# user input ---string ----> capitalize case without using methods.
# 'hello world' -----> 'Hello world'












