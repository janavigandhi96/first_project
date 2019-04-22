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

'''44. Write a Python program to locate Python site-packages.'''
# import site 
# print(site.getsitepackages())


# '''45. Write a python program to call an external command in Python'''(not done)
# filepath = '1.file.txt'
# import os
# os.startfile(filepath)

'''46. Write a python program to get the path and name of the file that is currently executing.'''
# import os
# print("current file name ",os.path.realpath(__file__))


'''47. Write a Python program to find out the number of CPUs using.'''
# import multiprocessing
# print("cpu.no:",multiprocessing.cpu_count())

# 48. Write a Python program to parse a string to Float or Integer.
# n = '54.95'
# print("string to float",float(n))
# print("string to int",int(float(n)))


'''49. Write a Python program to list all files in a directory in Python.'''
# from os import listdir
# from os.path import isfile, join
# files_list = [f for f in listdir('/janvi')if isfile(join('/janvi',f))]
# print(files_list)

'''50. Write a Python program to print without newline or space.'''
# for i in range(1,10):
# 	print(i,end = "")

'''51. Write a Python program to determine profiling of Python programs'''
# import cProfile
# def sum():
# 	print("add",10+20)
# cProfile.run('sum()')


'''52. Write a Python program to print to stderr'''
# import sys
# def eprint(*args, **kwargs):
#     print(*args, file=sys.stderr, **kwargs)
# eprint("abc", "efg", "xyz", sep="--")

'''53. Write a python program to access environment variables.'''
# import os
# print(os.environ)
# print("*****************")
# print(os.environ['HOMEPATH'])
# print("*****************")
# print(os.environ['Path'])

'''54. Write a Python program to get the current username'''
# import getpass
# print(getpass.getuser())

'''55. Write a Python to find local IP addresses using Python's stdlib'''
# import socket
# print(socket.gethostbyname(socket.gethostname()))


'''56. Write a Python program to get height and width of the console window.(not done) '''
# def terminal_size():
#     import fcntl, termios, struct
#     th, tw, hp, wp = struct.unpack('HHHH',
#         fcntl.ioctl(0, termios.TIOCGWINSZ,
#         struct.pack('HHHH', 0, 0, 0, 0)))
#     return tw, th

# print('Number of columns and Rows: ',terminal_size())

'''56. Write a Python program to get height and width of the console window.'''
# import time 
# def sum_of_n_numbers(n):
# 	start_time = time.time()
# 	s = 0
# 	for  i in range(1, n+1):
# 		s = s + i
# 	end_time = time.time()
# 	return s, end_time-start_time
# n = 5
# print(sum_of_n_numbers(n))


'''58. Write a python program to sum of the first n positive integers.'''
# n = int(input("enter positive no. "))
# total = (n*(n+1))/2
# print("sum of first n no:",total)


'''59. Write a Python program to convert height (in feet and inches) to centimeters'''
# feet  = int(input("enter foot: "))
# inches = int(input("enter inches: "))
# cent = (feet*30.48) + (inches * 2.54)
# print("height in centimeters: ",round(cent,2))

'''60. Write a Python program to calculate the hypotenuse of a right angled triangle'''
# a = int(input("enter widht:"))
# b = int(input("enter height:"))
# hypotenuse = ((a**2) +(b**2))**(1/2)
# print("the hypotenuse of a right angle triangle is: ",round(hypotenuse,2))

'''61. Write a Python program to convert the distance (in feet) to inches, yards, and miles'''
# feet = int(input("enter distance:"))
# inches = feet * 12
# yards = feet/3
# miles = feet / 5280
# print("feet to inches: {}\nfeet to yards: {}\nfeet into miles:{}\n".format(inches,round(yards,3),round(miles,3)))

'''62. Write a Python program to convert all units of time into seconds. '''
# day = int(input("enter days: ")) * 86400
# hour = int(input("enter hours: ")) * 3600
# minitues = int(input("enter minitues: ")) * 60
# seconds = int(input("enter seconds: "))
# time = day + hour + minitues + seconds
# print("convert all units of time into seconds",time)


'''63. Write a Python program to get an absolute file path'''
# def get_file(path_fname):
# 	import os
# 	return os.path.abspath('path_fname')
# print("absolute file path: ",get_file('1.file.txt'))

'''64. Write a Python program to get file creation and modification date/times.(not done)'''
# import os.path, time
# print("last modified: %s" % time.ctime(os.path.getmtime('2.file.txt'))) 
# print("created: %s" % time.ctime(os.path.getctime('2.file.txt')))

'''65. Write a Python program to convert seconds to day, hour, minutes and seconds'''
# seconds = int(input("enter seconds: "))
# day = seconds // 86400
# seconds %= 86400
# hour = seconds // 3600
# seconds %=3600
# minitues =seconds // 60
# seconds %=60
# print("days:hours:mins:secs--->{} : {} : {} : {} ".format(day,hour,minitues,seconds))

# 66. Write a Python program to calculate body mass index
# weight =float(input("enter in kg: ")) 
# height = float(input("enter in foot: "))
# bmi = (weight/(height)**2)*703
# print("bmi = ", bmi)

'''67. Write a Python program to convert pressure in kilopascals to pounds per square inch, a millimeter of mercury (mmHg) and atmosphere pressure'''
# kilopascals = float(input("enter kilopascals: "))
# pounds = kilopascals/6.895
# mercury = kilopascals/7.501
# atmosphere = kilopascals/101.325
# print("pressure in kilopascals to pounds per square inch :{}\nmillimeter of mercury (mmHg):{}\natmosphere pressure:{}".format(round(pounds,2), round(mercury,2), round(atmosphere,2)))

'''68. Write a Python program to calculate the sum of the digits in an integer.'''
# number = map(int, str(input('Enter a number: ')))
# print(sum(number))

'''69. Write a Python program to sort three integers without using conditional statements and loops'''
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# mx = max(a,b,c)
# mi = min(a,b,c)
# mid = a + b +c - mi - mx
# print("sort:", mi, mid, mx )

'''70. Write a Python program to sort files by date. '''
# import glob
# import os
# files = glob.glob("*.txt")
# files.sort(key = os.path.getmtime)
# print("\n".join(files))

'''71. Write a Python program to get a directory listing, sorted by creation date.'''
# from stat import S_ISREG, ST_CTIME, ST_MODE
# import os, sys, time
# dir_path =sys.argv[1] if len(sys.argv) == 2 else r'.' 
# data = (os.path.join(dir_path,fn) for fn in os.listdir(dir_path))
# data = ((os.stat(path),path)for path in data)
# data =((stat[ST_CTIME],path)
# 		for stat,path in data if S_ISREG(stat[ST_MODE]))
# for cdate, path in sorted(data):
# 	print(time.ctime(cdate), os.path.basename(path))

'''72. Write a Python program to get the details of math module.'''
# import math
# print(dir(math))

'''73. Write a Python program to calculate midpoints of a line'''
# x1 = int(input("enter value of x1:"))
# x2 = int(input("enter value of x2:"))
# y1 = int(input("enter value of y1:"))
# y2 = int(input("enter value of y2:"))
# midpoints = ( ( (x1 + x2) / 2) ,( (y1 + y2) / 2) )
# print("midpoints of line: ",midpoints)

'''74. Write a Python program to hash a word.'''
# soundex = [0,1,2,3,0,1,2,0,0,2,2,4,5,5,0,1,2,6,2,3,0,1,0,2,0,2]
# word = input("input the word to be hashed: ")
# word = word.upper()
# coded = word[0]
# for a in word[1:len(word)]:
# 	i = 65 - ord(a)
# 	coded  = coded + str(soundex[i])
# print("the coded word is :"+ coded)

'''75. Write a Python program to get the copyright information'''
# import sys
# print(sys.copyright)

'''76. Write a Python program to get the command-line arguments (name of the script, the number of arguments, arguments) passed to a script. '''
# import sys
# print("name of the scrip:",sys.argv[0])
# print("number of arguments: ",len(sys.argv))
# print("arguments: ",str(sys.argv))

'''77. Write a Python program to test whether the system is a big-endian platform or little-endian platform.'''
# import sys
# if sys.byteorder == 'big':
# 	print("big-endian platform")
# else:
# 	print("little - endian platform")

'''78. Write a Python program to find the available built-in modules.'''
# import sys
# print(sys.builtin_module_names)

'''79. Write a Python program to get the size of an object in bytes.'''
# import sys
# i = 1
# f = 10.5
# s ='four'
# print("getsize of int",sys.getsizeof(i))
# print("getsize of float",sys.getsizeof(f))
# print("getsize of string",sys.getsizeof(s))

'''80. Write a Python program to get the current value of the recursion limit.'''
# import sys
# print("current value of the recursion limit: ",sys.getrecursionlimit())

'''81. Write a Python program to concatenate N strings. '''
# l = ["red","black","yellow"]
# print('-'.join(l))

'''82. Write a Python program to calculate the sum over a container'''
# l = [10,20,30]
# print("sum over container: ",sum(l))

'''83. Write a Python program to test whether all numbers of a list is greater than a certain number'''
# l = [10, 20, 30]
# print(all(x>1 for x in l))
# print(all(y>40 for y in l ) )

'''84. Write a Python program to count the number occurrence of a specific character in a string.'''
# s = "Write a Python program to count the number "
# print(s.count('t'))

'''85. Write a Python program to check if a file path is a file or a directory.'''
# import os
# p = '/janvi/'
# if os.path.isdir(p):
# 	print("it is a directory")
# elif os.path.isfile(p):
# 	print("its a file")
# else:
# 	print("its a special file")

'''86. Write a Python program to get the ASCII value of a character.'''
# c = 'p'
# print("ascii character: " ,ord(c))

'''87. Write a Python program to get the size of a file.'''
# import sys
# print("size of file is: ",sys.getsizeof('2.file.txt'))


'''88. Given variables x=30 and y=20, write a Python program to print t "30+20=50".'''
# x = 10
# y = 20

# print("{} + {} = {}".format(x,y,(x+y))) 

'''89. Write a Python program to perform an action if a condition is true.'''
# value = 1 
# if value == 1:
# 	print("first day of the month")

'''90. Write a Python program to create a copy of its own source code.'''
# with open(file = "testfile.txt", mode='r')as f:
# 	print(f.readlines())

'''91. Write a Python program to swap two variables.'''
# a = 10
# b = 20
# print("before swapping")
# print("a = {}\nb = {}".format(a,b))
# c = b
# b = a 
# a = c 
# print("swaping a and b")
# print("a = {}\nb = {}".format(a,b))

'''92. Write a Python program to define a string containing special characters in various forms.'''
# print("/{""}$@#&")
# print("/{""}$@#&")
# print("/{""}$@#&")
# print("/{""}($@#&''')")

'''93. Write a Python program to get the identity of an object.'''
# n = 10
# print(id(n))

'''94. Write a Python program to convert a byte string to a list of integers.'''
# s = b'Abc'
# print(list(s))

'''95. Write a Python program to check if a string is numeric.'''
# s =  'a123'
# print("its numeric:",s.isdecimal())

'''96. Write a Python program to print the current call stack'''
# import traceback
# def f1():
# 	return abc()
# def abc():
# 	traceback.print_stack()
# f1()
# print()

'''97. Write a Python program to list the special variables used within the language. '''
# s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('__names i'.split()))
# print("\n".join(' '.join(s_var_names[i:i+8]) for i in range(0,len(s_var_names),8)))

'''98. Write a Python program to get the system time.'''
# import time 
# print(time.ctime())

'''99. Write a Python program to clear the screen or terminal.'''
# import os, time
# os.system('cls')

'''100. Write a Python program to get the name of the host on which the routine is running'''
# import socket
# print(socket.gethostname())

'''101. Write a Python program to access and print a URL's content to the console'''
# from http.client import HTTPConnection
# conn = HTTPConnection("google.com")
# conn.request("GET","/")
# result = conn.getresponse()
# contents = result.read() 
# print(contents)

'''102. Write a Python program to get system command output.'''
# import subprocess
# returned_txt = subprocess.check_output("dir", shell =True, universal_newlines = True)
# print("dir command to list file and directory")
# print(returned_txt)

'''103. Write a Python program to extract the filename from a given path.'''
# import os
# print(os.path.basename('/basic1.py'))

'''104. Write a Python program to get the effective group id, effective user id, real group id, a list of supplemental group ids associated with the current process.(not done)'''
# import os
# print("\nEffective group id: ",os.getgroups())
# print("Effective user id: ",os.geteuid())
# print("Real group id: ",os.getgid())
# print("List of supplemental group ids: ",os.getgroups())
# print()

'''105. Write a Python program to get the users environment.'''
# import os
# print(os.environ)

'''106. Write a Python program to divide a path on the extension separator.'''
# import os.path
# for path in ['testfile.txt','filename','G:/janvi/testfile.txt','/','']:
# 	print('"%s":' %path, os.path.splitext(path))

'''107. Write a Python program to retrieve file properties.'''	
# import os.path
# import time
# print("file: ",__file__)
# print("access time: ",time.ctime(os.path.getatime(__file__)))
# print("modified time: ",time.ctime(os.path.getmtime(__file__)))
# print("change time: ",time.ctime(os.path.getctime(__file__)))
# print("size of file: ",os.path.getsize(__file__))

'''108. Write a Python program to find path refers to a file or directory when you encounter a path name'''
# import os.path
# for file in [__file__, os.path.dirname(__file__), '/','./broken_link']:
# 	print("file: ",file)
# 	print("absolute: ", os.path.isabs(file))
# 	print("Is file: ",os.path.isfile(file))
# 	print("is dir: ", os.path.isdir(file))
# 	print("Is link: ",os.path.islink(file))
# 	print("exist: ",os.path.exists(file))
# 	print("link exist: ",os.path.lexists(file))
# 	break

'''109. Write a Python program to check if a number is positive, negative or zero'''
# def check(a):
# 	if a < 0:
# 		print("a is negavtive")
# 	elif a > 0:
# 		print("a is positive")
# 	else:
# 		print("a is 0")
# check(int(input("enter a number: ")))

'''110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function'''
# p = [10, 15, 30, 45]
# z = list(filter(lambda z : (z % 15 == 0),p))
# print(z)

'''111. Write a Python program to make file lists from current directory using a wildcard.'''
# import glob
# file_list = glob.glob('*.*')
# print(file_list)

# 112. Write a Python program to remove the first item from a specified list.
# s = [10,20,30,40,50]
# print(s)
# s.remove(s[0])
# print(s)

'''113. Write a Python program to input a number, if it is not a number generate an error message. '''
# try:
# 	s = int(input("enter a no.: "))
# except ValueError:
# 	print("pls enter a no")

'''114. Write a Python program to filter the positive numbers from a list.'''
# s = [10,20,30,-40]
# a = []
# for x in s:
# 	if x > 0:
# 		a.append(x)
# print(a)

'''115. Write a Python program to compute the product of a list of integers (without using for loop). '''
# from functools import reduce
# a = [10,20,30]
# a_prod = reduce((lambda x,y:x*y),a)
# print(a_prod)

'''116. Write a Python program to print Unicode characters'''
# str1 = u'\u004A\u0041\u004E\u0041\u0056\u0049'
# print(str1)

'''117. Write a Python program to prove that two string variables of same value point same memory location.'''
# loc_str1 = 'abc'
# loc_str2 = 'abc'
# print("location of string1: ",hex(id(loc_str1)))
# print("location of string2: ",hex(id(loc_str2)))

'''118. Write a Python program to create a bytearray from a list'''
# l = [10,20,30]
# byte_list = bytearray(l)
# for x in byte_list:
# 	print(x)

'''119. Write a Python program to display a floating number in specified numbers.'''
# pi = 3.14159
# print("the specified numbers is %f" %pi)
# print("the specified numbers is %.2f" %pi)

'''120. Write a Python program to format a specified string to limit the number of characters to 6.'''
# s = "0123456789"
# print("number of characters to 6: %.6s" %s)

'''121. Write a Python program to determine if variable is defined or not'''
# try:
# 	a = 1
# except NameError:
# 	print("variable not defined")
# else:
# 	print("variable is defined")
# try:
# 	b
# except NameError:
# 	print("variable not defined")
# else:
# 	print("variable is defined")

'''122. Write a Python program to empty a variable without destroying it'''
# n = 20
# m = {"x":20}
# p = ["x", 20]
# q = ("x",30)
# print(type(n)())
# print(type(m)())
# print(type(p)())
# print(type(q)())

'''123. Write a Python program to determine the largest and smallest integers, longs, floats'''
# import sys
# print("the longest int: ",sys.int_info)
# print("\nthe longest float: ",sys.float_info)
# print("\nthe longest long: ",sys.maxsize)

'''124. Write a Python program to check if multiple variables have the same value. '''
# x = 20
# y = 20
# z = 20
# if x == y == z == 20:
# 	print("all values are same")

'''125. Write a Python program to sum of all counts in a collections?'''
# import collections
# p = [2,3,3,4,5,6,4,2,1]
# print(sum(collections.Counter(p).values()))


'''126. Write a Python program to get the actual module object for a given object'''
# from inspect import getmodule
# from math import pow
# print(getmodule(pow))

'''127. Write a Python program to check if an integer fits in 64 bits'''
# value = 54
# print(value.bit_length())
# if value.bit_length() <= 63:
# 	print((-2**63).bit_length())
# 	print((2**63).bit_length())

'''128. Write a Python program to check if lowercase letters exist in a string.'''
# Solution 1:
# s ="HELLo"
# for x in s:
# 	if x.lower() in x:
# 		print("lowercase exist")
# solution 2
# str1 = "ABCdEFi12354"
# print(any(c.islower() for c in str1))

'''129. Write a Python program to add leading zeroes to a string.''' 
# s = '121.31'
# print("add leading zero: ",s.ljust(10,'0'))

'''130. Write a Python program to use double quotes to display strings.'''
# import json
# print(json.dumps({'A': 65, 'B' : 66, 'C' : 67}))

'''131. Write a Python program to split a variable length string into variables'''
# s = ['a', 'b', 'c']
# n = [20.20,100]
# x, y, z = (s + [""]*3)[:3]
# p, q = (n + [""]*3)[:2]
# print(x, y, z)
# print(p,q)

'''132. Write a Python program to list home directory without absolute path.'''
# import os.path
# print(os.path.expanduser('~'))

'''133. Write a Python program to calculate the time runs (difference between start and current time) of a program.'''
# from timeit import default_timer
# def timer(n):
# 	start = default_timer()
# 	for row in range(0,n):
# 		print(row)
# 	print(default_timer()- start)
# timer(10)

'''134. Write a Python program to input two integers in a single line.'''
# a, b = map(int,input("enter a & b: ").split())
# print(a, b)

'''135. Write a Python program to print a variable without spaces between values.'''
# a = 30
# print('value of a :"{}"'.format(a) ) 

'''136. Write a Python program to find files and skip directories of a given directory. '''
# import os
# print([f for f in os.listdir('/janvi') if os.path.isfile(os.path.join('/janvi',f))])

'''137. Write a Python program to extract single key-value pair of a dictionary in variables'''
# d = {"X" : 2}
# (a,b), = d.items()
# print(a)
# print(b)

'''138. Write a Python program to convert true to 1 and false to 0'''
# x = 'true'
# x = int(x=='true')
# print(x)
# x = 123
# x = int(x=='true')
# print(x)

'''139. Write a Python program to valid a IP address.'''
# import socket
# addr = '127.0.0.1'
# try:
# 	socket.inet_aton(addr)
# 	print("valid ip")
# except socket.error:
# 	print("Invalid")

'''140. Write a Python program to convert an integer to binary keep leading zeros. '''
# x = 80
# print(format(x,'08b'))
# print(format(x,'010b'))

'''141. Write a python program to convert decimal to hexadecimal'''
# x = 4
# y = 30
# print(format(x,'02x'))

'''142. Write a Python program to find the operating system name, platform and platform release date.'''
# import os
# import sys
# import platform
# import datetime
# print("operating system name: ",os.name)
# print("platform name: ",platform.system())
# print("platform release: ",platform.release())

'''143. Write a Python program to determine if the python shell is executing in 32bit or 64bit mode on operating system.'''
# import struct 
# print(struct.calcsize("P" * 8))

'''144. Write a Python program to check if variable is of integer or string'''
# print( ( isinstance('Hello',int) ) or ( isinstance('Hello',str) ) )
# print( ( isinstance(['Hello'],int) ) or ( isinstance(['Hello'],str) ) )
# print((isinstance(5,int)) or (instance(5,str)) )

'''145. Write a Python program to test if a variable is a list or tuple or a set.'''
# x = {10, 20, 30, 40}
# if type(x) == list:
# 	print("its a list")
# elif type(x) == tuple:
# 	print("its a tuple")
# elif type(x) == set:
# 	print("its a set")
# else:
# 	print("Its something else")

'''146. Write a Python program to find the location of Python module sources.'''
# import os
# import sys
# print("list of modules is system: ",sys.path)
# print("list of modules in operating sys: ",os.path)

'''147. Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.'''
# x = int(input("enter no1: ")) 
# y = int(input("enter no2: ")) 
# if x % y == 0:
# 	print("x is divisible by y")
# else:
# 	print("x is not divisible by y")

'''148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers.'''
# data = [1,65,45,87,7,5,40,0]
# mi = data[0] 
# mx = data[0]
# for items in data:
# 	if mi > items:
# 		mi = items
# 	elif mx < items:
# 		mx = items
# print("minimum number in list : ",mi)
# print("maximum number in list : ",mx)

'''149. Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. '''
# def cube(x):
# 	ad = 0
# 	c = 0
# 	s = 0
# 	for n in range(1,x):
# 		c = n**3
# 		ad = c
# 		s = ad +s
# 	print("the sum of cube : ",s)
# cube(3)

'''150. Write a Python function to find a distinct pair of numbers whose product is odd from a sequence of integer values'''
# def odd_product(l): 
# 	for i in range(len(l)):
# 		for j in range(len(l)):
# 			if i != j:
# 				prod = l[i] * l[j]
# 				if prod & 1:
# 					return True
# d1 = [1,2,3,4,6]
# d2 = [1,2,4,6] 
# print(odd_product(d1))
# print(odd_product(d2))