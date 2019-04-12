'''1. Write a Python function to find the Max of three numbers.'''
# def max_func(a,b,c):
# 	if a > b and a > c:
# 		print("{} is greater".format(a))
# 	elif b > a and b > c:
# 		print("{} is greater".format(b))
# 	else:
# 		print("{} is greater".format(c))
# max_func(10,20,30)
# max_func(15,20,5)
# max_func(20,10,5)

'''2. Write a Python function to sum all the numbers in a list'''
# def total(a):
# 	s = 0 
# 	for x in range(len(a)):
# 		s += a[x]
# 	print(s)
# total([10, 20, 30])
# total([21, 19, 20])

'''3. Write a Python function to multiply all the numbers in a list.'''
# def multi(a):
# 	s = 1 
# 	for x in range(len(a)):
# 		s *= a[x]
# 	print(s)
# multi([10, 20, 30])
# multi([21, 19, 20])

'''4. Write a Python program to reverse a string'''
# def  rev(a):
# 	print("reverse",a[::-1])
# rev('1234abcd')


'''5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument'''
# def fact(n):
# 	if n == 0 :
# 		return 1
# 	else:
# 		return n * fact(n-1)
# print("the factorail is:",fact(4))

'''6. Write a Python function to check whether a number is in a given range.'''
# def check(n):
# 	if n in range(1,10):
# 		print("{} it is within range ".format(n))
# 	else:
# 		print("{} out of range".format(n))
# check(5)
# check(11)

'''7. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters'''
# def no_string(str1):
# 	upper = 0
# 	lower = 0
# 	for i in str1:
# 		if  i.islower():
# 			lower += 1
			
# 		elif i.isupper():
# 			upper += 1
# 	print("lower characters",lower) 
# 	print("upper characters",upper) 

# print(no_string("This is James"))

'''8**. Write a Python function that takes a list and returns a new list with unique elements of the first list.'''
# def unique_elements(u):
# 	e = set(u)
# 	print("unique elements: ", e )
# unique_elements([1,2,3,3,3,4])

'''9. Write a Python function that takes a number as a parameter and check the number is prime or not'''
# def prime(p):
# 	if p == 0:
# 		return False
# 	elif p == 1:
# 		return True
# 	for  n in range(2,p):
# 		if p % n == 0:
# 			return "{} is not prime no".format(p)
# 		else:
# 			return "{} is prime no".format(p)
# print(prime(10))
# print(prime(5))

'''10. Write a Python program to print the even numbers from a given list'''
# def even(e):
# 	a = []
# 	for i in e:
# 		if i % 2 == 0:
# 			a.append(i)
# 	return a
# print(even([1, 2, 3, 4, 10, 6]))

'''11. Write a Python function to check whether a number is perfect or not.'''
# def perfect(a):
# 	result = 0
# 	for i in range(1,a):
# 		if a % i == 0:
# 			result += i
# 	return result == a
# print(perfect(6))

'''12. Write a Python function that checks whether a passed string is palindrome or not'''
# def palidrome(s):
# 	s = s.lower()
# 	if s == s[::-1]:
# 		print("{} is palideome".format(s))
# 	else:
# 		print("{} is not palideome".format(s))
# palidrome('mom')
# palidrome('jane')

'''13. Write a Python function that prints out the first n rows of Pascal's triangle.(***)'''
# def pascal(n):
# 	row = [1]
# 	y = [0]
# 	for i in range(max(n,0)):
# 		print(row)
# 		row = [l+r for l,r in zip(row + y,y + row)]
# 	return n>1
# pascal(6)

'''14. Write a Python function to check whether a string is a pangram or not.(***) '''
# import string,sys
# def pangram(str1, alphabeth = string.ascii_lowercase):
# 	alphabeth= set(alphabeth)
# 	return alphabeth <= set(str1.lower())
# print(pangram('The quick brown fox jumps over lazy dog'))

'''15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.((***))'''
# def hyphen(str1):
# 	item = [n for n in str1.split('-')]
# 	item.sort()
# 	print('-'.join(item))
# hyphen('green-red-yellow-black-white')

'''16. Write a Python function to create and print a list where the values are square of numbers between 1 and 30 (both included).'''
# def square():
# 	s = [x**2 for x in range(0,21)]
# 	print(s)
# square()

'''17. Write a Python program to make a chain of function decorators (bold, italic, underline etc.) in Python.'''
# def bold(fn):
# 	def wrapped():
# 		return "<b>" + fn() +"</b>"
# 	return wrapped
# def italic(fn):
# 	def wrapped():
# 		return "<i>" + fn() +"</i>"
# 	return wrapped
# def underline(fn):
# 	def wrapped():
# 		return "<u>" + fn() +"</u>"
# 	return wrapped
# @bold
# @italic
# @underline
# def hello():
# 	return "hello world"
# print(hello())

'''18. Write a Python program to execute a string containing Python code.'''
# a = ""
# def p (a,b):
# 	print(a+b)
# p(10,20)
# ""

'''19. Write a Python program to access a function inside a function'''
# def fun():
# 	print("hello")
# 	def func1(a,b):
# 		print(a+b)
# 	return func1(10,20)
# fun()

'''20. Write a Python program to detect the number of local variables declared in a function. '''
# def local_var():
# 	a = 10
# 	str1 = 'Hello'
# print(local_var.__code__.co_nlocals)