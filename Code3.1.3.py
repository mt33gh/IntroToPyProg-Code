#3.1 Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures
#3.1.3 Sets
# A set is a collection which is unordered, unchangeable*, and unindexed.
# * Note: Set items are unchangeable, but you can remove items and add new items.
# Run the following code:

countries = ['France', 'Germany', 'India', 'United States', 'India', 'China'] # list
print(countries)
c = set(countries) #change it into a set
print(c)
print(len(c)) 

c.add('Italy')
print(c)
c.remove('United States')
print(c)

print(c[0])  # error

#time = 70
