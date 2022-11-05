from numpy import array, empty, zeros, ones, triu, tril, diag
from numpy import identity

# create matriks
matriks = array([[2,9,8],[7,6,5],[4,3,2]])
# print matriks
print("Matriks: \n")
print(matriks)
print("\n")

# create matriks contain random number
randomMatriks = empty([2,3])
# print randomMatriks
print("Show random matriks: \n")
print(randomMatriks)
print("\n")

# create matriks contain zeros
zerosMatriks = zeros([4,2])
# print zerosMatriks
print("Show zero matriks: \n")
print(zerosMatriks)
print("\n")

# create matriks with all the item value are one
oneMatriks = ones([3,3])
# print oneMatriks
print("Show one matriks: \n")
print(oneMatriks)
print("\n")

# create lower triangle matriks
lowerTriangleMatriks = tril(matriks)
# print lower triangle matriks
print("Show lower triangle matriks: \n")
print(lowerTriangleMatriks)
print("\n")

# create upper triangle matriks
upperTriangleMatriks = triu(matriks)
# print upper triangle matriks
print("Show upper triangle matriks: \n")
print(upperTriangleMatriks)
print("\n")

# extract diagonal vector
diagonalVector = diag(matriks)
# create diagonal matriks
diagonalMatriks = diag(diagonalVector)
# print diagonal matriks
print("Show diagonal matriks: \n")
print(diagonalMatriks)
print("\n")

# create identity matriks
identityMatriks = identity(5)
# print identity matriks
print("Show identity matriks: \n")
print(identityMatriks)
print("\n")
