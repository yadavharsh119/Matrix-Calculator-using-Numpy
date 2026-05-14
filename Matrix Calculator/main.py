import numpy as np
class Matrix:
    amatrix = np.array([])
    bmatrix = np.array([])
    def inputm(self):
        dim = {}
        ndims = int(input("Enter Number of Dimensions of matrix A: "))
        ashape = tuple(map(int,input("Enter value of dimensions seperated by commas: ").split(",")))
        print("Input matrix A: ")
        self.amatrix = np.array(list(map(int,input("Enter elements seperated by commas: ").split(","))))
        self.amatrix = self.amatrix.reshape(ashape)   
        print(f"Matrix A: {self.amatrix}") 
        mdims = int(input("Enter Number of Dimensions of matrix B: "))    
        bshape = tuple(map(int,input("Enter value of dimensions seperated by commas: ").split(",")))
        print("Input matrix B: ")
        self.bmatrix = np.array(list(map(int,input("Enter elements seperated by commas: ").split(","))))
        self.bmatrix = self.bmatrix.reshape(bshape)   
        print(f"Matrix B: {self.bmatrix}") 
    def matrixadditn(self):
        # ~ if(np.ndim(amatrix) != np.ndim(bmatrix)):
            # ~ print("Dimensions of the provided matrix are not same")
            # ~ return []
        # ~ if(amatrix.shape != bmatrix.shape):
            # ~ print("Shape of the provided matrix are not same")
            # ~ return []
        # ~ else:
            # ~ cmatrix = np.ones(amatrix.shape)
            # ~ for i in range(cmatrix.shape[0]):
                # ~ for j in range(cmatrix.shape[1]):
                    # ~ cmatrix[i,j] = amatrix[i,j] + bmatrix[i,j]
        print("Addition of two Matrices is:")
        return self.amatrix + self.bmatrix
    def matrixsubtraction(self):
        print("Subtraction of two Matrices is:")
        return self.amatrix - self.bmatrix
    def matrixmultiplicatn(self):
        cmatrix = np.zeros((self.amatrix.shape[0],self.bmatrix.shape[1]))
        # ~ for i in range(self.amatrix.shape[0]):
            # ~ for j in range(self.bmatrix.shape[1]) :
                # ~ for k in range(self.amatrix.shape[1]):
                    # ~ cmatrix[i,j] += self.amatrix[i,k]*self.bmatrix[k,j]
        choice = int(input("Elementwise Multiplication(0) or Matrix Multiplication(1) or Dot Product? "))
        if(choice):
            return self.amatrix*self.bmatrix
        elif choice == 0:
            return self.amatrix@self.bmatrix
        else:
            return np.dot(amatrix,bmatrix)
o1 = Matrix()
o1.inputm()
print(o1.matrixmultiplicatn())

