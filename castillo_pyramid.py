# funtion for printing the pyramid pattern
def OuterLoop(x,n):
    if n!=0:
        OuterLoop(x,n-1)
        InnerLoop1(x-n)
        InnerLoop2(n*2-1)
        print("\n")
    else:
        return None

def InnerLoop1(n):
    if n!=0:
        print(" ", end="")
        InnerLoop1(n-1)
    else:
        return None

def InnerLoop2(n):
    if n!=0:
        print(InnerLoop2(n-1), end="")
        return "*"
    else:
        return "*"
 
# Print Pyramid
# If x < n the height of the pyramid will be = x and it will not print the rest of n it will only display error message
OuterLoop(5,5)

