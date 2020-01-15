A=[(11,12),[21,22]]
# print(A[1])

# A=[(1),[2,3],[4]]
# print(A[2])

A.extend([3,'pop'])
print(A)

B=[1]
B=B+[2,3,4,5]
print(B)
del(B[0])
print(B)

x='1,2,3,4'.split(',')
print(x)

# clone A
B=A[:]
print(B)