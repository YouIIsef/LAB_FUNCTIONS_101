
def Triangle(Number):
    """Print numbers from Number to 1""" # Here I define the function

    for i in range(Number,0,-1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
Triangle(5)