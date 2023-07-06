

matrix = [
    ["a1","b1","c1","c2","b2","a2"],
    ["d1","e1","f1","f2","e2","d2"],
    ["g1","h1","i1","i2","h2","g2"],
    ["g4","h4","i4","i3","h3","g3"],
    ["d4","e4","f4","f3","e3","d3"],
    ["a4","b4","c4","c3","b3","a3"]
]


def turnMatrixToLeft(parMatrix):
    for item in parMatrix:
        item = item.reverse()
    return parMatrix

def turnMatrixToTop(parMatrix):
    parMatrix = parMatrix[::-1]
    return parMatrix

def getTopLeftSquare(parMatrix):
    miniMatrix = []
    for i in range(0,len(parMatrix)//2):
        line = []
        for j in range(0,len(parMatrix)//2):
            line.append(parMatrix[i][j])
        miniMatrix.append(line)
    
    print('top left matrix')
    for item in miniMatrix:
        print(item)
    
    return miniMatrix

def replaceMatrixHighValues(matrix1,matrix2):
    newMatrix = []
    for i in range(0,len(matrix1)):
        line = []
        for j in range(0,len(matrix1)):
            if matrix1[i][j] > matrix2[i][j]:
                line.append(matrix1[i][j])
            else:
                line.append(matrix2[i][j])
        newMatrix.append(line)
        
    print('High values')
    for item in newMatrix:
        print(item)
    return newMatrix

def sumMatrixNumbers(matrixPar):
    total = 0
    for i in range(0,len(matrixPar)):
        for j in range(0,len(matrixPar)):
            total += matrixPar[i][j]
    return total

def getMaximumSumFromTopLeft(numMatrix):
    firstTop = getTopLeftSquare(numMatrix)
    numMatrix = turnMatrixToLeft(numMatrix)
    secondTop = getTopLeftSquare(numMatrix)
    numMatrix = turnMatrixToTop(numMatrix)
    thirdTop = getTopLeftSquare(numMatrix)
    numMatrix = turnMatrixToLeft(numMatrix)
    fourthTop = getTopLeftSquare(numMatrix)
    
    firstMaxTop = replaceMatrixHighValues(firstTop,secondTop)
    secondMaxTop = replaceMatrixHighValues(firstMaxTop,thirdTop)
    thirdMaxTop = replaceMatrixHighValues(secondMaxTop,fourthTop)
    
    maxSum = sumMatrixNumbers(thirdMaxTop)
    
    print("Result: ",maxSum)
    

# Original matrix
print('Original matrix')
for item in matrix:
    print(item)
    

mini = getTopLeftSquare(matrix)

    
# # Reverse each row
# for item in matrix:
#     item = item.reverse()
    
print('Reverse each row')
matrix = turnMatrixToLeft(matrix)
for item in matrix:
    print(item)
    

mini = getTopLeftSquare(matrix)

# # Reverse the matrix
# matrix = matrix[::-1]

print('Reverse the matrix')
matrix = turnMatrixToTop(matrix)
for item in matrix:
    print(item)


mini = getTopLeftSquare(matrix)
# # Reverse each row
# for item in matrix:
#     item = item.reverse()
    
print('Reverse each row')
matrix = turnMatrixToLeft(matrix)
for item in matrix:
    print(item)
    

mini = getTopLeftSquare(matrix)

    
    
matrixNums = [    
    [112,42,83,119],
    [56,125,56,49],
    [15,78,101,43],
    [62,98,114,108]
]

getMaximumSumFromTopLeft(matrixNums)

matrixNums2 = [    
    [107,54,128,15],
    [12,75,110,138],
    [100,96,34,85],
    [75,15,28,112]
]
getMaximumSumFromTopLeft(matrixNums2)