# pattern printing
# basic star patterns
# *
# **
# ***
# ****

# for i in range(1,5):
#     for j in range(i):
#         print('*',end=' ')
#     print()



#########################
# ****
# ***
# **
# *

# for i in range(1,5):
#     for j in range(5-i):
#         print('*',end=' ')
#     print()


# for i in range(1,5):
#     for j in range(5,i,-1):
#         print('*',end=' ')
#     print()










############################
#     *
#    **
#   ***
#  ****


# for i in range(1,5):
#     for j in range(5-i-1):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     print()








############################

#  ****
#   ***
#    **
#     *

# for i in range(1,5):
#     for j in range(i):
#         print(' ',end=' ')
#     for j in range(5-i):
#         print('*',end=' ')
#     print()

##########################
# *
# **
# ***
# ****
# ***
# **
# *
# def pattern():
#     for i in range(1,5):
#         for j in range(i):
#             print('*',end=' ')
#         print()
#     for i in range(1,4):
#         for j in range(4-i):
#             print('*',end=' ')
#         print()

# for i in range(5):
#     pattern()

################################
#     *
#    ***
#   *****
#  *******
# *********



# for i in range(1,6):
#     for j in range(6-i):
#         print(' ',end=' ')
#     for j in range(i):
#         print('*',end=' ')
#     for j in range(i-1):
#         print('*',end=' ')
#
#     print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4


for i in range(1,5):
    for j in range(i):
        print(j+1,end=' ')
    print()







