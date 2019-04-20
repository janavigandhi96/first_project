'''1. Write a Python program to calculate the length of a string.'''
# s = 'Hello'
# print("lenght of the string", len(s))

'''2. Write a Python program to count the number of characters (character frequency) in a string.(***)'''
# s = 'google.com'
# dict={}
# for n in s:
# 	keys = dict.keys()
# 	if n in keys:
# 		dict[n]+=1
# 	else:
# 		dict[n] = 1
# print(dict)


'''3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.'''
# def first_last(s): #= 'percentage'
# 	list(s)
# 	if len(s)>2:
# 		s1 = s[0:2]
# 		s2 = s[-2:]
# 		print("concat",s1 + s2)
# 	else:
# 		print("single character")

# first_last('hello')
# first_last('h')
# first_last('hello world')


'''4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.(***)'''
# def change(s):
# 	char = s[0]
# 	s = s.replace(char,'$')
# 	s = char + s[1:]
# 	print(s)
# change('restart')


'''5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.'''
# a = 'abc'
# b = 'xyz'

# new_a = b[0:2]+a[2]
# new_b = a[0:2]+b[2]
# c = new_a + " " + new_b
# print(c)


'''6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.'''
# def adding(str1):
# 	if len(str1) >= 3:
# 		print("")
# 		if 'ing' in str1:
# 			print("adding ly in end:",str1+'ly')
# 		else:
# 			print("adding ing in end:", str1+'ing')
# adding('if')
# adding('end')
# adding('string')


'''7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string'''
# def replace_poor(s):
# 	if 'not' in s:
# 		loc_not = s.find('not')
# 		print(s.replace(s[loc_not:], 'poor'))
# 	elif 'good' in s:
# 		loc_good = s.find('good')
# 		print(s.replace(s[loc_good:], 'poor'))
# replace_poor('the lyrics is not that poor')
# replace_poor('food is good')


'''8. Write a Python function that takes a list of words and returns the length of the longest one. '''
# def long_word(words):
# 	words = sorted(words, key=lambda x: len(x), reverse=True)
# 	return words[0]
# print(long_word(["PHP", "Exercises", "Backend"]))


'''9. Write a Python program to remove the nth index character from a nonempty string.'''
# a = 'hello'
# n = int(input("index no in range of a:"))
# remove = a.replace(a[n],'')
# print(remove)


'''10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged'''
# a = 'efgh'
# print(a)
# b = a[-1]+a[1:-1]+a[0]
# print(b)

'''11. Write a Python program to remove the characters which have odd index values of a given string.'''
# a = 'hello'
# rem =''
# for n in range(len(a)):
# 	if n%2 == 0:
# 		rem = rem + a[n]
# print(rem)

'''12. Write a Python program to count the occurrences of each word in a given sentence.'''