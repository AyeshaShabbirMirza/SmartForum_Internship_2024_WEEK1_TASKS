import numpy as np

#1. CREATING ARRAY
a = np.array([5,7,3,8,6,4,1,7,8,8])
print("\n1. CREATING ARRAY")
print("CREATING ARRAY a: ", a)

#2. ACCESSING ELEMENT OF ARRAY
print("\n2. ACCESSING ELEMENT OF ARRAY")
print("ARRAY a: ", a)
print("ACCESSING 3rd ELEMENT OF ARRAY a: ", a[2])

#3. ARRAY SLICING
print("\n3. ARRAY SLICING")
print("ARRAY a: ", a)
print("SLICING OF ARRAY a: ", a[2:5])

#4. NEGATIVE ARRAY SLICING
print("\n4. NEGATIVE ARRAY SLICING")
print("ARRAY a: ", a)
print("NEGATIVE SLICING OF ARRAY a: ", a[-2:-5])

#5. SLICING WITH STEP
print("\n5. SLICING WITH STEP")
print("ARRAY a: ", a)
print("SLICING OF ARRAY a WITH STEP: ", a[1:2:6])

#6. CHECKING THE DATA TYPE OF ARRAY
print("\n6. CHECKING THE DATA TYPE OF ARRAY")
print("ARRAY a: ", a)
print("CHECKING THE DATA TYPE OF ARRAY a: ", a.dtype)

#7. CREATING ARRAY WITH STRING DATA TYPE
print("\n7. CREATING ARRAY WITH STRING DATA TYPE")
b = np.array([6,2,9,5], dtype='S')
print("CREATING ARRAY b WITH STRING DATA TYPE", b)
print("CHECKING THE DATA TYPE OF ARRAY b: ", b.dtype)

#8. CONVERTING DATA TYPE OF ARRAY
print("\n8. CONVERTING DATA TYPE OF ARRAY")
c = a.astype(float)
print("ARRAY a: ", a)
print("CONVERTED ARRAY FROM INTEGER DATA TYPE ARRAY a TO FLOAT DATA TYPE ARRAY c: ", c)
print("CHECKING DATA TYPE OF CONVERTED ARRAY c", c.dtype)

#9. COPY & MODIFY AN ARRAY
print("\n9. COPY & MODIFY AN ARRAY")
d = a.copy()
d[0] = 42
print("ORIGINAL ARRAY THAT WILL BE COPIED a: ", a)
print("COPIED AND MODIFIED ARRAY d: ", d) 

#10. VIEW & MODIFY AN ARRAY
print("\n10. VIEW & MODIFY AN ARRAY")
e = a.view()
e[0] = 42
print("ORIGINAL ARRAY THAT IS VIEWD a: ", a)
print("COPIED AND MODIFIED ARRAY e: ", e)

#11. GETTING THE SHAPE OF 2D ARRAY
print("\n11. GETTING THE SHAPE OF 2D ARRAY")
f = np.array([[3,5,7,2], [2,5,4,7]])
print(f.shape)

#12. ITERATE ON THE ELEMENTS OF ARRAY
print("\n12. ITERATE ON THE ELEMENTS OF ARRAY")
print("ARRAY a: ", a)
print("ITERATE ON THE ELEMENTS OF ARRAY a: \n")
for x in a:
  print(x)

#13. ARRAY CONCATENATION
print("\n13. ARRAY CONCATENATION")
g1 = np.array([2,4,6])
g2 = np.array([7,3,9])
g = np.concatenate((g1, g2))
print("ARRAY g1: ", g1)
print("ARRAY g2: ", g2)
print("CONCATENATED ARRAY g: ", g)

#14. SPLITTING ARRAY
print("\n14. SPLITTING ARRAY")
h = np.array_split(a, 2)
print("ARRAY a: ", a)
print("SPLITTED ARRAY a IN TWO PARTS: ", h)

#15. SEARCHING THE ARRAY
print("\n15. SEARCHING THE ARRAY")
i = np.where(a == 8)
print("ARRAY a: ", a)
print("SEARCHING THE INDEX OF ARRAY a WHERE VALUE IS 8", i)

#16. SORTING ARRAYS
print("\n16. SORTING ARRAYS")
j = np.array(['mango', 'strawberry', 'orange'])
print("ORIGINAL ARRAY j: ", j)
print("SORTED ARRAY j: ", np.sort(j))

#17. FILTERING ARRAYS
print("\n17. FILTERING ARRAYS")
k = np.array([32,56,32,23])
l = [False, True, True, False]
m = k[l]
print("ORIGIBAL ARRAY k: ", k)
print("FILTERED ARRAY m: ", m)

#18. FINDING L.C.M
print("\n18. FINDING L.C.M")
NUM1 = 24
NUM2 = 50
LCM = np.lcm(NUM1, NUM2)
print("LCM OF 24 & 50 IS: ", LCM)

#19. TAKING PRODUCT OF THE ELEMENTS OF ARRAY
print("\n19. TAKING PRODUCT OF THE ELEMENTS OF ARRAY")
PRO = np.prod(a)
print("ARRAY a: ", a)
print("PRODUCT OF THE ELEMENTS OF ARRAY a: ", PRO)

#20. SUMMING ARRAYS
print("\n20. SUMMING ARRAYS")
SUM = np.add(a, a)
print("ARRAY a1: ", a)
print("ARRAY a2: ", a)
print("SUMMING ARRAY a1 & a2: ", SUM)

