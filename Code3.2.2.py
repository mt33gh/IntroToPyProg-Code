#3.2 Operators: Membership, Identity
#3.2.2 Identity
# Run the following code:

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# returns True because z is the same object as x

print(x is y)
# returns False because x is not the same object as y, even if they have the same content

print(x == y)
# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#But in the following examples, each variable holds the same value, and the same value is supposed to be the same object.
x = 5
y = 5
z = x   # x's value is assined to z.

print(x is z)   #True
print(x is y)   #True
print(x == y)   #True

#time = 70
