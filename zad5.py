#Potegi

def power(x,n):
    s=x
    if n==1:
        return x
    else:
        for i in range (n-1):
            s=s*x
        return s
    
x=int(input("X: "))
n=int(input("N: "))

print(power(x,n))
        