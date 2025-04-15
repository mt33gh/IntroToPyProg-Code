#3.1 Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures
#3.1.2 Tuples
# Unlike lists, however, tuples are immutable
#  - you can't add and remove items from tuples, or sort them in place.
# Run the following code:

location = (36.2048, 138.2529) # tuple
print("Latitude:", location[0])
print("Longitude:", location[1])
#location.append(250)  #causes an error

a = [36.2048, 138.2529]   # list
a.append(250)             # append() is a method
print(a)

#time = 60
