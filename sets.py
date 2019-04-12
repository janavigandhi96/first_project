'''1. Write a Python program to create a set.'''
# a = [10, 2, 5, 74, 45, 1, 15]
# print("List", a)
# a_set = set(a)
# print("As a set", a_set)


'''2. Write a Python program to iteration over sets.'''
# a_set = set([10,12,45,13,35,6,55,31])
# print("\nbefore iteration:", a_set)
# print("\nIterating:")
# for items in a_set:
# 	print(items)


'''3. Write a Python program to add member(s) in a set.'''
# a_set = set()
# a_set.add(50)
# print(a_set)
# a_set.update([100,200])
# print(a_set)


'''4. Write a Python program to remove item(s) from set '''
# a_set = set([10,12,45,13,35,6,55,31])
# print(a_set)
# a_set.remove(45)
# print(a_set)


'''5. Write a Python program to remove an item from a set if it is present in the set.'''
# a_set = set([10,12,45,13,35,6,55,31])
# print(a_set)
# if 13 in a_set:
# 	a_set.remove(13)
# 	print("after removing:", a_set)
# else:
# 	print("not present")


'''6. Write a Python program to create an intersection of sets.'''
# a_set = set([10, 20, 30, 40, 50])
# b_set = set([50, 60, 70, 80, 90])
# print("intersection", a_set.intersection(b_set))


'''7. Write a Python program to create a union of sets.'''
# a_set = set([10, 20, 30, 40, 50])
# b_set = set([50, 60, 70, 80, 90])
# print("union", a_set.union(b_set))


'''8. Write a Python program to create set difference'''
# a_set = set([10, 20, 30, 40, 50])
# b_set = set([50, 60, 70, 80, 90])
# print("difference in a_set", a_set.difference(b_set))
# print("difference in b_set", b_set.difference(a_set))


'''9. Write a Python program to create a symmetric difference'''
# a_set = set([10, 20, 30, 40, 50])
# b_set = set([50, 60, 70, 80, 90])
# print("symmetric difference in a_set", a_set.symmetric_difference(b_set))


'''10. Write a Python program to issubset and issuperset'''
# a_set = set([1, 2, 3, 4, 5])
# b_set = set([3, 4, 5])
# print("b_set subset of a_set: ", b_set.issubset(a_set))
# print("a_set subset of b_set: ", a_set.issubset(b_set))
# print("b_set supperset of a_set", b_set.issuperset(a_set))
# print("a_set supperset of b_set", a_set.issuperset(b_set))


'''11. Write a Python program to create a shallow copy of sets.'''
# a_set = set([1, 2, 3, 4, 5])
# b_set = set([3, 4, 5])
# c_set = a_set.copy()
# print("shallow copy", c_set)


'''12. Write a Python program to clear a set'''
# a_set = set([1, 2, 3, 4, 5])
# print(a_set)
# a_set.clear()
# print("cleared ",a_set)

'''13. Write a Python program to use of frozensets. '''
# a_set = frozenset([1,2,3,4,5])
# print(a_set)
# b_set = frozenset([3, 4, 5])
# print(b_set)
# print("union: ",a_set | b_set )
# print("intersection",a_set & b_set)

'''14. Write a Python program to find maximum and the minimum value in a set'''
# a_set = set([1, 2, 3, 5])
# print("minimum", min(a_set))
# print("maximum",max(a_set))


'''15. Write a Python program to find the length of a set.'''
# a_set = set([1, 2, 3, 4, 5, 6])
# print("lenght of a_set:",len(a_set))