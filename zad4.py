#Function that checks if the number is within the given range

def give_range(x,y,z):
    if z>=x and z<=y:
        return True
    else:
        return False
    

x=int(input("Give the first number: "))
y=int(input("Give the second number: "))
z=int(input("Give the specific number: "))

print(give_range(x,y,z))
    