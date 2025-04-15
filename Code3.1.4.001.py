#3.1 Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures
#3.1.4 Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Run the following code:

elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print("carbon" in elements)  #True   'in' is an operator (membership)

print(elements.get("dilithium"))  #None
print(elements.get("helium"))     # 2

n = elements.get("dilithium")
print(n is None)        #identity
print(n is not None)
print(n == None)        #equality
print(n != None)

#time = 70
