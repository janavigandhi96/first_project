'''1. Write a Python program to create an array of 5 integers and display the array items. Access individual element through indexes'''
# a = [10,12,15,20]
# for items in (a):
# 	print(items)
# print(a[0],a[1],a[-1])

'''2. Write a Python program to append a new item to the end of the array.'''
# a = [10, 20, 30]
# print("old list:",a)
# a.append(40)
# print("appended list:",a)

'''3. Write a Python program to reverse the order of the items in the array.'''
# a = [10, 20, 30]
# print(a)
# print("reverse:",a[-1::-1])

'''4. Write a Python program to get the length in bytes of one array item in the internal representation (***)'''
# from array import *
# a = array('i',[10,20,30])
# print("original array: "+str(a))
# print("lenght of bytes of one array item"+str(a.itemsize))

'''5. Write a Python program to get the current memory address and the length in elements of the buffer used to hold an array?s contents and also find the size of the memory buffer in bytes.  (***)'''
# from array import *
# a = array('i',[10,20,30])
# print("original array:",str(a))
# print("current memory address:",str(a.buffer_info()))
# print("Buffer size:"+ (str(a.buffer_info()[1] * a.itemsize)))

'''6. Write a Python program to get the number of occurrences of a specified element in an array. '''
# from collections import Counter
# a = [10,20,30,40,20]
# print(a.count(20))
			
'''7. Write a Python program to append items from inerrable to the end of the array.'''
# a = [10, 2, 4, 2, 1]
# a.extend(a)
# print("extended array",a)

'''8.Write a Python program to convert an array to an array of machine values and return the bytes representation.(***) '''
# from array import *
# a = array('b',[119, 51, 114, 101,  115, 111, 117, 114, 99, 101])
# print("bytes representation",a.tobytes())




'''9. Write a Python program to append items from a specified list. '''
# from array import *
# a_list = [10,20,30]
# ap_list = array('b',[])
# print("a_list :" + str(a_list))
# print("apending list")
# ap_list.fromlist(a_list)
# print("ap_list: " + str(ap_list))

'''10. Write a Python program to insert a new item before the second element in an existing array. '''
# a = [10,30,40,50]
# print("old array:", a)
# a[2:] = a[1:]
# a[1] = 20
# print("after inserting new element:",a)

'''11. Write a Python program to remove a specified item using the index from an array'''
# ar_ray = [10, 20, 30, 4, 0]
# ar_ray.remove(ar_ray[0])
# print(ar_ray)


'''12. Write a Python program to remove the first occurrence of a specified element from an array.'''
ar_ray = [10, 20, 2, 5, 15, 10, 6, 10]
print("without removing element:", ar_ray)
ar_ray.remove(10)
print("removing first occurrance: ",ar_ray)




'''13. Write a Python program to convert an array to an ordinary list with the same items. '''
# a = [10, 20, 30]
# print("array:",a)
# l = list(a)
# print("In list format:",l)