'''1. Write a Python program to create a tuple.'''
# t = (10,20,30)
# print("tuple: ",t)

'''2. Write a Python program to create a tuple with different data types. '''
# t = (10,20.5,"hii",True)
# print(" tuple with different data types:\n",t)

'''3. Write a Python program to create a tuple with numbers and print one item.'''
# t= 10,20,30
# t = (10,)
# print("print one item: ",t)

'''4. Write a Python program to unpack a tuple in several variables.'''
# a = ("ABC", 25000,"Mumbai")
# (name, salary, place) = a
# print("name: ", name)
# print("salary: ", salary)
# print("place: ",place)

'''5. Write a Python program to add an item in a tuple.'''
# def tuple_add(t):
# 	f = list(t)
# 	f.append(int(input("enter no: ")))
# 	print("updated: ", tuple(f)) 
# tuple_add((10,20,30))

'''6. Write a Python program to convert a tuple to a string.'''
# t = 's','t', 'r', 'i', 'n', 'g'
# s = ''.join(t)
# print(s)

'''7. Write a Python program to get the 4th element and 4th element from last of a tuple.'''
# t = 's','t', 'r', 'i', 'n', 'g'
# print( "the 4th element of a tuple: " ,t[3])
# print("4th element from last of a tuple: ",t[-4])

'''8. Write a Python program to create the colon of a tuple.'''
# t = 's','t', 'r', 'i', 'n', 'g'
# s = ':'.join(t)
# print(s)

'''9. Write a Python program to find the repeated items of a tuple.'''
# from copy import deepcopy
# t = ("hello", 5, [], True)
# print(t)
# t_copy = deepcopy(t)
# t_copy[2].append(10)
# print(t_copy)


'''10. Write a Python program to check whether an element exists within a tuple.'''
# s = 50, 20, 5, 30
# print(50 in s)
# print("r" in s) 

'''11. Write a Python program to convert a list to a tuple.'''
# l = [10, 20, 30, 40]
# print("in list format: ",l)
# print("List in tuple: ",tuple(l))

'''12. Write a Python program to remove an item from a tuple'''
# t = 10, 20, 30
# s = list(t)
# s.remove(10)
# print(tuple(s))

'''13. Write a Python program to slice a tuple'''
# t = 10,20,'hello'
# print(t[:-1])
# print(t[1:])
# print(t[:])

'''14. Write a Python program to find the index of an item of a tuple.'''
# t = 10,20,30,40
# print("index: ", t.index(40))

'''15. Write a Python program to find the length of a tuple'''
# t = 10, 20, 30, 40
# print("length of tuple: ",len(t))

'''16. Write a Python program to convert a tuple to a dictionary.'''
# t = ( (10,'ten'), (20, "twenty") )
# print(dict((y,x) for x,y in t))

'''17. Write a Python program to unzip a list of tuples into individual lists'''
# l = [(1, 2), (3, 4), (5, 6)]
# print(list(zip(*l)))

'''18. Write a Python program to reverse a tuple.'''
# t = 10, 20, 30, 40
# print("reverse: ",t[::-1])

'''19. Write a Python program to convert a list of tuples into a dictionary.'''
# t = ( (10,'ten'), (20, "twenty") )
# d = {}
# for a, b in t:
# 	d.setdefault(a,[]).append(b)
# print(d)

'''20. Write a Python program to print a tuple with string formatting'''
# t = 10, 20, 30, 40
# print("{} tuple in string format".format(t))

'''21. Write a Python program to replace last value of tuples in a list'''
# lt = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]
# print([t[:-1] + (100,) for t in lt])

'''22. Write a Python program to remove an empty tuple(s) from a list of tuples.'''
# t = [(),(),('',),('a','b'),('a','b','c')]
# p = [x for x in t if x]
# print(p)

'''23. Write a Python program to sort a tuple by its float element.'''
# t = [('item1',12.20),('item2',15.30),('item3',24.00)]
# print(sorted(t, key = lambda x :float(x[1]),reverse = True ))

'''24. Write a Python program to count the elements in a list until an element is a tuple.'''
# t = [10, 20, 30, (40,50), 60]
# c = 0
# for f in t:
# 	if isinstance(f,tuple):
# 		break
# 	c += 1
# print(c)