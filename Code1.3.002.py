#1.3 Use error messages to help you learn.
#Run the following code:

x = 5
y = 1
while y > 0.0000000001:
    y = 0.1 * y
    z = x / y
    print("y = ", y, "  z = ", z)

#time = 30
#This is a while loop.  It repeats the indented portion while the condition is met.
# For the first turn, y = 1
# For the second turn, y = 0.1*1=0.1  
# For the third turn, y = 0.1*0.1 = 0.01
# This is an example that explains what is 5 divided by 0