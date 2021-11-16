#Anonymous function that returns true when the first number is greater than the second one

which_greater = lambda x,y: x>y

x=int(input("First: "))
y=int(input("Second: "))
print(which_greater(x,y))