"""Al programes."""

# ***********multiplication matrix *************

# a = [[1, 2, 3], [4, 5, 6],[1,2,3]]
# b = [[7, 8], [9, 10],[11, 12]]
# print(c)

# a = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
# b = [[1, 0, 0], [0, 1, 0], [0 ,0, 1]]

# if(len(a[0])==len(b)):
#   m = [[0 for x in range(len(b[0]))] for y in range(len(a))]
#   print(m)
#   for i in range(len(a)):
#       for j in range(len(b[0])):
#           for k in range(len(b)):
#               m[i][j]+=a[i][k]*b[k][j]
#   for matrix in m:
#       print(matrix)
# else:
#   print("rows 1 and column 2 is not matching")

# ------------------------------------------


# ************ palidrome************

# user_input = input().lower().strip()
# if user_input[::-1] == user_input:
#   print("\n Its Palidrome")
# else:
#   print("\n Its not Palidrome")


# -----------------------------------------

# ************sub palidrome************

# user_input=input("enter string ").lower().strip()

# for i in range(len(user_input)):
#   result=''
#   for j in range(i,len(user_input)):
#       result+=user_input[j]
#       if len(result) >= 2 and result==result[::-1]:
#           print(result,"this is palidrome")


# -------------------------------------------------


# ********* determinate of matrix 2*2 *************

# def det(a):
#   result = (a[0][0] * a[1][1]) - (a[0][1]*a[1][0])
#   print(result)
#   return result
# det([[2,3],[2,4]])

# --------------------------------------------------

# ********* determinant of matrix 3*3 *************
# def det(l):
#     """Function to calculate a determinant."""
#     n = len(l)
#     if (n > 2):
#         flag = 1
#         t = 0
#         total = 0
#         while t <= n - 1:
#             d = {}
#             t1 = 1
#             while t1 <= n - 1:
#                 m = 0
#                 d[t1] = []
#                 while m <= n - 1:
#                     if (m == t):
#                         pass
#                     else:
#                         d[t1].append(l[t1][m])  # d = {1 : [4, 5 ,6]}
#                     m += 1
#                 t1 += 1
#             l1 = [d[x] for x in d]
#             total = total + flag * (l[0][t] * det(l1))
#             flag = flag * (-1)
#             t += 1
#         return total
#     else:
#         return (l[0][0] * l[1][1]) - (l[0][1] * l[1][0])

# l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# l1 = [[6, 1, 1], [1, 1, 1], [1, 1, 1]]

# l2 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]

# print(det(l2))


# ------------------------------------------------------

# **print number if number is greater or equal to 25****.

# l=[x for x in range(1,101)]
# print(l)
# user_input=int(input("enter a number: "))
# if user_input >= 25:
#   print(l[24:])
# else:
#   print("do nothing")


# ----------------------------------------------------------

# ********* see that the multiples is in list 2 or not ********************

# l1=[x*y for x in range(1,11) for y in range(1,11)]
# l = [x for x in range(1,11)]
# l1 = [i for i in range(11,101)]
# l = [l[x]*l[y] for x in range(len(l)) for y in range(len(l)) if l[x]*l[y] in l1]
# print(l)


# ------------------------------------------------------------


# ************ to check when a person turns what will be the year when he turns 100
# import datetime
# age =float (input("enter age: "))
# age=int(age)
# name = input("enter name: ")
# if age < 0:
#   print("wrong value ")

# else:
#   diff = 100 - (age)
#   current_format = datetime.datetime.now()
#   current_year = current_format.year
#   when_100 = diff+current_year
#   print(when_100," is the year when user turns 100")
# ----------------------------------------------------------------


# ************** divisor **************
# user_input=int(input("enter number="))
# list=[]
# for r in range (1,user_input+1):
#   if user_input % r  == 0:
#       list.append(r)
# for m in list :
# #     print(m)


# -----------------------------------------------


# ************fibonacci of user's no**************
# def fibo(user_input):
#     """Fibonaci series."""
#     if user_input < 2:
#         return user_input
#     else:
#         return(fibo(user_input - 1) + fibo(user_input - 2))
# user_input = int(input("enter no:"))
# print("fibonacci series")
# for i in range(user_input):
#     print(fibo(i))


#  -----------------------------------------------

"""Cowbull program.""" 
# import pdb
# import random
# def cowbull(): 
#   """Cow Bull game."""
#   user_lenght = int(input("enter lenght:\t")) 
#   cow = 0 
#   bull = 0 
#   random_no = [random.randrange(0, 9) for x in range(user_lenght)] 
#   print("enter no. of digits") 
#   guesses = [int(x) for x in input("enter user_lenght digit no. \t").strip()]
#   print(guesses) 
 
#   for i in range(user_lenght): 
#     if guesses[i] == random_no[i]: 
#       cow += 1 
#     else: 
#       bull += 1

# # comparing cow and bulls
#   if cow > bull:
#     print("you won")
#   else:
#     print("you lose")
#     print(random_no)
# cowbull()


#  -----------------------------------------------


'''employess information'''
# def employee(num):
#     """Function of Employee class."""
#     employees = []
#     for i in range(num):
#       emp = {'name': input("enter the name:\t "),'tenure': int(input("enter tenure:\t")),'designation': input("enter designation:\t"),'salary': int(input("enter salary:\t"))}
#       employees.append(emp)
#       print("\n")
#     user_designation=input("enter to check avg salary of particular designation:")
#     total = [i['salary']  for i in employees if i['designation'] == user_designation]
    
#     print("Avg salary of {} is {}".format(user_designation, sum(total) / len (total)))
    
#     print("Minimum salary of:", min(employees, key = lambda x : x['salary']))
    
#     print("maximum salary of employee", max(employees, key=lambda x : x['salary']))

# employee(int(input("Enter the number of employees \t")))
 

# -------------------------------------------


'''Insertion sort'''
# def insertion_sort(l):
#   count = 0
#   for index in range(1,len(l)):
# #     print('index {}'.format(index))
#     temp = l[index]
#     position = index - 1
# #     print('position {}'.format(position))
#     while position >=0 and temp < l[position]:
#       l[position+1] = l[position]
#       position = position - 1
# #       print('position inside while {}'.format(position))
#     l[position+1] = temp
#   return l, count

# print(insertion_sort([9,8,7, 6, 5, 4, 3, 2, 1]))


# ---------------------------------------

'''insertion sort'''
# def insertion_sort(l):
#   count = 0
#   for index in range(1,len(l)):
# #     print('index {}'.format(index))
#     temp = l[index]
#     position = index - 1
# #     print('position {}'.format(position))
#     while position >=0 and temp < l[position]:
#       l[position+1] = l[position]
#       position = position - 1
# #       print('position inside while {}'.format(position))
#     l[position+1] = temp
#   return l, count

# print(insertion_sort([9,8,7, 6, 5, 4, 3, 2, 1]))


# -------------------------------------------

'''gnome sort '''
# def gnome(alist):
# 	for i in range(1,len(alist)):
# 		while i!=0 and alist[i] <= alist[i-1]:
# 			alist[i],alist[i-1] = alist[i-1], alist[i]
#     print(alist[i],alist[i-1])
# 			i -=1
# alist = [34,2,10,-9,27,97]
# gnome(alist)
# print("Sorted list: ",alist)


# --------------------------------------


'''Regular expression'''
# import re
# import datetime
# from datetime import date
# s = 'my birthday is on 01/01/1990'
# s2 ='my graduation day is on 01-07-12'  
# s3 = 'my wedding anniversary is on 01.01.2016'
# s4 = ' 01-jan-19'
# match = re.findall(r'[\d]{1,2}/[\d]{1,2}/[\d]{4}',s)
# match1 = re.findall(r'[\d]{1,2}-[\d]{1,2}-[\d]{2}',s2)
# match2 = re.findall(r'[\d]{1,2}.[\d]{1,2}.[\d]{4}',s3)
# match3 = re.findall(r"([0-9]{1,2}\-[a-z]{3}\-[0-9]{1,2})", s4)
# print(match)
# print(match1)
# print(match2)
# print(match3)



# --------------------------------------------------


'''company data'''
# def company():
#     alist = []
#     comp_dets ={
#     'google': {
#         'emp1': {'designation': 'coder', 'salary': 50000},
#         'emp2': {'designation': 'developer', 'salary': 20000},
#         'emp3': {'designation': 'tester', 'salary': 30000}
#         }, 
#     'adobe': {
#         'emp1': {'designation': 'hr', 'salary': 23000},
#         'emp2': {'designation': 'clerk', 'salary': 5000},
#         'emp3': {'designation': 'accountant', 'salary': 15000}
#           },
#     'microsoft': {
#         'emp1': {'designation': 'manager', 'salary': 60000},
#         'emp2': {'designation': 'project manager', 'salary': 55000},
#         'emp3': {'designation': 'director', 'salary': 45000}
#           }
#     }

#     alist = [(c ,emp, comp_dets[c][emp]) for c in comp_dets for emp in comp_dets[c]]
#     print(alist)
#     print("\n")
   
#     print("Name wised  company: ",sorted(comp_dets))
#     '''Maximum salary'''
#     max_sal = max([comp_dets[c][emp]['salary'] for c in comp_dets for emp in comp_dets[c]])
#     max_cmp = [(c , comp_dets[c][emp]) for c in comp_dets for emp in comp_dets[c] if comp_dets[c][emp]['salary'] == max_sal]
#     print("\nmaximum salary :",max_cmp)
#     print("\n")

#     '''Minimum salary'''
#     min_sal = min([comp_dets[cd][em]['salary'] for cd in comp_dets for em in comp_dets[cd]]) 
#     min_cmp = [(cd , comp_dets[cd][em]) for cd in comp_dets for em in comp_dets[cd] if comp_dets[cd][em]['salary'] == min_sal]
#     print("Minimum salary",min_cmp)
#     print("\n")
#     '''sorting'''
    
#     sort_sal = sorted([comp_dets[c][emp]['salary'] for c in comp_dets for emp in comp_dets[c]],reverse=True)

    
#     for i in sort_sal:
#         sort_cmp = ([(c,emp,comp_dets[c][emp]['salary']) for c in comp_dets for emp in comp_dets[c] if  comp_dets[c][emp]['salary'] == i ] )
#         print(sort_cmp)
# company()