from numpy import array, dot

matriksA = array([[1,2,3], [4,5,6], [7,8,9]])
matriksB = array([[1,2,3], [4,5,6], [7,8,9]])

print("Matriks A: \n")
print(matriksA)
print("\n")

print("Matriks B: \n")
print(matriksB)
print("\n")

# sum matriksA and matriksB
matriksC = matriksA + matriksB
# print matriksC
print("Result of sum matriksA and matriksB: \n")
print(matriksC)
print("\n")

# multiply matriksA and matriksB (matriks can be multiply only when matriks that have number of column same with the other matriks row )
matriksD = dot(matriksA, matriksB)
# print matriksD
print("Result of multiply matriksA with matriksB: \n")
print(matriksD)
print("\n")

# new way to multiply matriks in python above 3.5
matriksD = matriksA @ matriksB
# print matriksD
print("Result of multiply matriksA with matriksB: \n")
print(matriksD)
print("\n")

# multiply matriks with scalar
scalar = 5
matriksE = matriksA * scalar
# print matriksE
print("Result of multiply matriksA with scalar/number: \n")
print(matriksE)
print("\n")