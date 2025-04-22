#1.2 Spacing is important
#Run the following code:

x = 5
x = input("Enter an integer:")
x = int(x)
if x + 4 > 20:
    print("x+4は、20より大きい")
else:
    print("x+4は、20または20より小さい")

# Now, delete the indentation before "print()".  What happens?

#time = 20
#This code is completely fine.
#Since x*4 = 5*4 = 20, which is equel to 20.  So x * 4 > 20 is false.
#As a result, the else clause is executed.
#Then, delete the space before print() on line 6, which causes an error.