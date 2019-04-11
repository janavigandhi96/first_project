'''1.Write a Python program to print the following string in a specific format'''

# print("Twinkle ,twinkle, little star,\n\t How I wonder what you are !\n\t\tUp above the world so high, \n\t\t Like a dimond in the sky.\nTwinkle ,twinkle, little star,\n\t How I wonder what you are ")

'''2. Write a Python program to get the Python version you are using. '''
# import sys
# print(sys.version)

'''3. Write a Python program to display the current date and time.'''
# import datetime
# current_datetime  = datetime.datetime.now()
# print("current date: ",current_datetime )

'''4. Write a Python program which accepts the radius of a circle from the user and compute the area'''
# radius = float(input("enter radius of circle:\t"))
# pi = 3.14
# area = pi * radius * radius
# print("area of the circle: ",area)

'''5.Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.'''
# firstname = input("enter first name: ")
# lastname = input("enter last name:")
# fullname = lastname + " "+firstname
# print(fullname)

'''6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers'''
# num = input("enter sequence of comma-separated numbers: ")

# list_num = num.split(",")
# tuple_num =tuple(num.split(","))
# print("in list form: ",list_num)
# print("in tuple form: ",tuple_num)


'''7. Write a Python program to accept a filename from the user and print the extension of that'''
# filename = input("enter name with extension:")
# print("Name of the file:",filename)
# name,ext = filename.split(".")
# print("extension of file:",ext)

'''8.Write a Python program to display the first and last colors from the following list'''
# color_list = ["Red", "Green", "White","Black"]
# print("First color is {} \nLast color is {}".format(color_list[0],color_list[-1]))

'''9. **Write a Python program to display the examination schedule. (extract the date from exam_st_date).'''
# import datetime
# exam_st_date =(11,12,2014)
# print("the examiation will start from %d/%d/%d"%exam_st_date)


'''10.Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.'''
# n = input("enter a number:")
# value = n
# value1 = n+n
# value2 = n+n+n
# v = int(value)
# v1 = int(value1)
# v2 = int(value2)
# total = v+v1+v2
# print(total)


'''11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).'''
# import datetime
# print(datetime.__doc__)


'''12.Write a Python program to print the calendar of a given month and year.'''
# import calendar
# m = int(input("enter month(1-12):"))
# y = int(input("enter year:"))
# print("calendar of:\n\n",calendar.month(y,m))


'''13. Write a Python program to print the following here document. Go to the editor
Sample string :'''
# print('a string that you "don\'t" have to escape \nThis \nis a ....... multi-line\nheredoc string ----------> example')

'''14. Write a Python program to calculate number of days between two dates.'''
# from datetime import date
# date1 = date(2014, 7, 2)
# date2 = date(2014, 7, 11)
# diff = date2 - date1
# print(diff.days)

'''15. Write a Python program to get the volume of a sphere with radius 6.'''
# from math import pi
# radius = 6
# volume =(4*pi*radius**3)/3
# print("volume of sphere:",volume())

'''16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.'''
# num = int(input("enter no :"))
# v = num - 17
# if num > 17:
# 	value = v*2
# 	print("the no is greater than 17 than double abs value is:", value)
# else:
# 	value = abs(v)
# 	print("the no is smaller so the abs value is:",value)


'''17.Write a Python program to test whether a number is within 100 of 1000 or 2000'''
# no = int(input("enter a no.:"))
# diff = abs(100-no)
# if diff <= 1000 or diff <=2000:
# 	print(True)
# else:
# 	print(False)

'''18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return thrice of their sum.'''
# n1 = int(input("enter no1:"))
# n2 = int(input("enter no2:"))
# n3 = int(input("enter no3:"))
# value = n1+n2+n3
# if n1 == n2 == n3:
# 	print(value)*3
# else:
# 	print((value))

'''19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.'''

# str1 = "this is a sentence."
# if 'Is' in str1:
# 	print("its no changeable")
# else:
# 	str2 ="Is " + str1
# 	print(str2)


'''20. Write a Python program to get a string which is n (non-negative integer) copies of a given string'''
# n = int(input("enter non negative number:"))
# str = "Hello "
# print(str*n,"\n")

'''20. Write a Python program to get a string which is n (non-negative integer) copies of a given string'''
# n = int(input("enter a no. : "))
# if n%2 == 0:
# 	print(n," this is even number")
# else: 
# 	print(n," is odd number")

'''22. Write a Python program to count the number 4 in a given list.'''
# n = [1,4, 3, 5, 9, 8]
# if 4 in n:
# 	print(n.count(4))
# else:
# 	print("there is no 4.")

'''23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2. '''
# n = int(input("enter non negative no:"))
# st = "abcd"
# if len(st) > 2: 
# 	print( (st[0:2]) * n)
# else:
# 	print(st*n)

'''24. Write a Python program to test whether a passed letter is a vowel or not'''
# def vowels(letter):
# 	vow = ['a','e','i','o','u']
# 	if letter not in vow:
# 		print(letter,"is not vowel")
# 	else:
# 		print(letter,"it is vowel")
# vowels('a')
# vowels('b')
# vowels('c')
# vowels('i')

'''25. Write a Python program to check whether a specified value is contained in a group of values. '''
# def test(l,val):
# 	if val in l:
# 		return True
# 	else:
# 		return False
# print(test((10, 15, 5, 2),2))
# print(test((10, 15, 5, 2),20))


'''26. Write a Python program to create a histogram from a given list of integers.'''
# def hist(l):
# 	for i in l:
# 		print(i * ' @ ')
# hist([2,5,8,3,7])


'''27. Write a Python program to concatenate all elements in a list into a string and return it(*)'''
# def con(l):
# 	str_l = ''
# 	for  x in (l):
# 		str_l += str(x)
# 	return str_l
# print(con([10,20,30]))


'''28. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence'''
# number = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]
# for  x in number:
# 	if x % 2 ==0:
# 		print(x)
# 	if x == 237:
# 		break


'''29. Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.'''
# color_list_1 = set(["red", "orange", "blue"])
# color_list_2 = set(["red", "black"])
# inter = color_list_1.difference(color_list_2)
# print(inter)

'''30. Write a Python program that will accept the base and height of a triangle and compute the area'''
# base = int(input("enter base of triangle:"))
# height = int(input("enter height of triangle"))
# area = (height *base)/2
# print("area of triangle is ",area)

'''31. Write a Python program to compute the greatest common divisor (GCD) of two positive integers.'''
# def gcd(a,b):
# 	if b==0:
# 		return a
# 	else:
# 		return gcd (b, a%b)
# print(gcd(24,18))

# '''32. Write a Python program to get the least common multiple (LCM) of two positive integers.'''(**)
# def gcd(a, b):
# 	if a == b:
# 		return a
# 	if a > b:
# 		return gcd(a-b,b)
# 	return gcd(a,b-a)
# def lcm(a,b):
# 	return (a*b)/gcd(a,b)
# print(lcm(15,20))

'''33. Write a Python program to sum of three given integers. However, if two values are equal sum will be zero'''

# def total(n1,n2,n3):
# 	if n1 == n2 or n1 == n3 or n2 == n3:
# 		return  0
# 	else :
# 		t = n1+n2+n3
# 		return t 
# print(total(10,20,30))
# print(total(10,10,30))
# print(total(10,20,20))
# print(total(10,20,10))

'''34. Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20. '''
# def sum_int(a,b):
# 	t = a+b
# 	if t >= 15 and t <= 20:
# 		return 20
# 	else:
# 		return t
# print(sum_int(10,16))
# print(sum_int(10,6))

'''35. Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5'''
# def five(a,b):
# 	total = a+b
# 	diff = a-b
# 	if a == b:
# 		return True
# 	elif total == 5:
# 		return True
# 	elif diff == 5:
# 		return True
# 	else:
# 		return False
# print(five(10,10))
# print(five(4,1))
# print(five(10,5))
# print(five(10,20))

'''36. Write a Python program to add two objects if both objects are an integer type.'''
# def obj_int(a,b):
# 	if a == int(a) and b == int(b):
# 		raise TypeError
# 	return a+b
# print(obj_int(10,20))

'''37. Write a Python program to display your details like name, age, address in three different lines. '''
# def display():
# 	name = 'abc'
# 	age = 19
# 	address = 'Mumbai, Maharashtra,India'
# 	print("{}\n{}\n{}".format(name,age,address))a
# display()


'''38. Write a Python program to solve (x + y) * (x + y)  (***)'''
# def solve(x,y):
# 	result = (x+y) * (x+y)
# 	print(" ({}+{})^2 = {} ".format(x,y,result))
# solve(3,4)

'''39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.'''
# def future(amt, rate, years):
# 	fv =  amt * ( (1 + (rate/100)) **7 )
# 	print(round(fv,2))
# future(10000,3.5,7)

'''40. Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).'''
# def distance(x1,y1,x2,y2):
# 	formula = (((x2 - x1)**2) + ((y2 - y1)**2))**(1/2)
# 	return round(formula,2)
# print(distance(4,0,6,6))

'''41. Write a Python program to check whether a file exists.  (***)'''
# import os.path
# with open("1.file.txt","w") as fe:
# 	print(os.path.isfile('1.file.txt'))

'''42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.  (***)'''
# import struct
# print(struct.calcsize("P") * 8)

'''43. Write a Python program to get OS name, platform and release information.(***)'''
# import os
# import platform
# print(os.name,platform.release(), platform.system())

