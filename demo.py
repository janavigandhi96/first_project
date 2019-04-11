# odd even 

# num=[1,2,3,4,5,6,7,8,9,10]
# for nums in num:
#   if(nums%2==0):
#       print(nums, "is even")
#   else:
#       print(nums," is odd")


# print largest number
# a=1
# b=2
# c=3
# if(a>b and a>c):
#   print(a,"is largest")
# elif b>a and b>c:
#   print(b,"is largest")
# else:
#   print(c ,"is largest")


#arithmatic operations(input bt user)
# v1=int(input("type variable 1: \n"))
# v2=int(input("type variable 2: \n"))
# print("1.Addition")
# print("2.Subtraction")
# print("3.division")
# print("4.floor division")
# print("5.multiplication")
# print("6.modulo")
# print("7.square root")
# print("8.power")
# print("9.percentage")
# print("\n")

# v3=int(input("type variable 3:"))

# if(v3==1):
#   print("1.addition of v1 & v2=",v1+v2)
# elif v3==2:
#   if v2 > v1:
#       print('Subtraction not possible...v2 > v1')
#   else:
#       print("2.subtraction of v1 & v2=",v1-v2)
# elif v3==3:
#   try:
#       print("3.division of v1 & v2=",v1/v2)
#   except:
#       print("cant divide by 0")
# elif v3==4:
#   try:
#       print("4.floor divide of v1&v2=",v1//v2)
#   except:
#       print("cant divide by 0")
# elif v3==5:
#   print("5.multiplication of v1&v2=",v1*v2)
# elif v3==6:
#   print("6.modulo of v1 & v2=",v1%v2)
# elif v3==7:
#   x=v1**(1.0/float(v2))
#   print("7.square root of v1 and v2=",x)
# elif v3==8:
#   print("8.power of v1 & v2=",v1**v2)
# elif v3==9:
#   print("9.percentage of v1 and v2=",(v1/v2)*100)
# else:
#   print("invalid")


# addition matrices
# a=[[1,0,0],[0,1,0],[0,0,1]]
# a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
# b=[[1,2,3],[3,2,1],[1,1,1,]]
# m=[[0,0,0],[0,0,0],[0,0,0]]

# a = [[1, 1], [1, 1]]
# b = [[3, 3], [3, 3]]


# if(len(a)==len(b)):
#   m = [[0 for x in range(len(a))] for y in range(len(b))]
#   print(m)
#   for i in range(len(a)):
#       for j in range(len(b)):
#           m[i][j]=a[i][j]+b[i][j]
# for matrix in m:
#   print(matrix)

# # multiplication matrices
# a = [[1, 2, 3], [4, 5, 6],[7, 8, 9]]
# b = [[3, 3], [3, 3],[3,3]]

# if(len(a[0])==len(b)):
#   m = [[0 for x in range(len(b[0]))] for y in range(len(a))]
#   for i in range(len(a)):
#       for j in range(len(b[0])):
#           for k in range(len(m)):
#               m[i][j]+=a[i][k]*b[k][j]
#   for matrix in m:
#       print(matrix)
# else:
#   print("r2 and c1 does not match")

# Palidrome
# str=input()

# str_lower=str.lower()
# print("In lower case: ",str_lower)

# str_rev=str_lower[-1::-1]
# print("String is reverse: ",str_rev)

# str_strip=str_lower.strip()
# print("Strig is strip:",str_strip)

# if str_rev == str_strip:
#   print("Its Palidrome")
# else:
#   print("Its not Palidrome")

# str="JANAVI"
# print(str.lower())

# 	====================
def src_dest(str1,str2):
	set1 = set(str1)
	set2 = set(str2)
	print(set1,set2) 
	temp = str1[:] 
	t = []
	for i in str2:
		if i in str2:
			t.append
		diff = len(str2)-len(t)
	for i in range(diff):
		t.append('0')
	if len(t) == len(str2):
		for i in range(len(str2)):
			if t[i] ==str2[i]:
				pass
			else:
				out = t[i]
				t[i] = str2[i]
				for  j in range(len(str2[i:])):
					if out ==str2[i+j]:
						t[i+j] =out
	print(''.join(t))
	i = len(set1.intersection(set2))
	x = len(str1) - i
	y = len(str2) - i
	print(y-x)
	
src_dest('april','aprilia')
