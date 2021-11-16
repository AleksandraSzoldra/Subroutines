
#Zad3, sum of number digits


def sum(x):
    sum=0
    while x !=0:
        sum= sum + (x%10)
        x=x//10
        
    return sum

g=int(input("Pl: "))
print (sum(g)) 