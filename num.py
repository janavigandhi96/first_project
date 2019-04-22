'''1.Write a NumPy program to get the numpy version and show numpy build configuration.'''
# import numpy as np
# print(np.__version__)
# print(np.show_config())

'''2. Write a NumPy program to  get help on the add function.'''
# import numpy as np 
# print(np.info(np.add))

# 3. Write a NumPy program to test whether none of the elements of a given array is zero
# import numpy as np
# a = [0,1,2,3]
# print(np.all(a))

'''4. Write a NumPy program to test if any of the elements of a given array is non-zero.'''
import numpy as np
a = [0,1,2,3]
print(np.any(a))
a = [0,0,0,0]
print(np.any(a))