#3.1 Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures
#3.1.4 Dictionaries
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# How can I sort a dictionary by values?
# Run the following code:

elements = {'helium': 2, 'hydrogen': 1, 'carbon': 6, 'oxygen': 8, 'Nitrogen': 7}
print(elements)

# Sorting the dictionary by values in ascending order
elements = dict(sorted(elements.items(), key=lambda item: item[1]))
print(elements)

#another way of soting
mylist = list(elements.items())
mylist.sort(key=lambda i: i[1])
print(mylist)
print(dict(mylist))

#time = 70
