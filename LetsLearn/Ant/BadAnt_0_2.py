import random

# user data
# How many N do you have?
n = 2000

#Introduce proportions of each columns percent between 0 and 100! 
VarProps = [0,90, 45, 39, 10, 11, 34, 24, 89, 100, 1]


# Main functions
def FillColumn(n,proportion):
    percent = float(proportion)/float(100) # it is only in Python 2... 
    numbersof = int(round(n*percent,0))
    column = random.sample(([i for i in range(1,n+1)]),numbersof)#change numbersof
    return sorted(column) #sorted  is  added optional in this case

def SetOneInColumn(n,args):
    count = 1
    column=[]
    while count <= n:
        if count in args:
            column.append(1)
        else:
            column.append(0)
        count+=1
    return column

#This function joins columns
FullMatrix = []
for i in range(len(VarProps)):
    FullMatrix.append(SetOneInColumn(n,FillColumn(n,VarProps[i])))

def TransMatrix(matrix):
    count = 0
    for row in matrix:
        for i in range(len(row)):
            count = count + 1
    matrixLenght = count/len(matrix)
    return  [[row[i] for row in matrix] for i in range(matrixLenght)]
              

# This function creates file with matrix
def WriteIt(FullMatix):
    transTab = TransMatrix(FullMatrix)
    f=open('Matrix.txt', 'w')
    for item in transTab:
        f.write("%s\n" % item)
    f.close()
    print "Ok, it's done.\n Your file calls 'Matrix.txt'"

WriteIt(FullMatrix)

