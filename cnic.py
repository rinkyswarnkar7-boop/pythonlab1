def CBIC(x,y,z):                #name of the function is CBIC and argument to the function is x
   # k=2*x**3+4*y**2
    k=4*z**2+3*y+x**2           # body of the function
    return k                    #statement to the return computed result
a=int(input("enter a number:"))
b=int(input("enter a number:")) # taking integer type of input
c=int(input("enter a number:"))
print(CBIC(a,b,c))              #function call inside print
