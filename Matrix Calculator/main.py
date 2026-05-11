import numpy as np
def inputm():
    dim = {}
    ndims = int(input("Enter Number of Dimensions of matrix A: "))
    ashape = tuple(map(int,input("Enter value of dimensions seperated by spaces: ").split()))
    print(ashape)
    print("Input matrix A: ")
    amatrix = np.array(list(map(int,input("Enter elements seperated by commas: ").split(","))))
    amatrix = amatrix.reshape(ashape)   
    print(amatrix) 
    mdims = int(input("Enter Number of Dimensions of the matrix B: "))
    
    print("Input matrix B")
    
inputm()
