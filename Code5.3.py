#5.3 Lambda Expressions

# Run the following code:

#function
def multiply(x, y):
    return x * y
print(multiply(2,5))

#lambda
multiply = lambda x, y: x * y     # f(x,y) = x * y
print(multiply(2,5))

#creating a new function with lambda
def volume(z):
    return lambda x, y: x * y * z
v = volume(10)                # Now, v = lambda x, y: x*y*10
print(v(2,3))

#time = 70
