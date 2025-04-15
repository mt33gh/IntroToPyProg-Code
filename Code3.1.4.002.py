#3.1 Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures
#3.1.4 Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Run the following code:

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
#print(elements[2])   # error
print(elements["carbon"])   

elements["oxygen"] = 8
print(elements)

elements.update({"Nitrogen": 7})
print(elements)


#time = 70
