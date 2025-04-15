#3.1 Types of Data Structures: Lists, Tuples, Sets, Dictionaries, Compound Data Structures
#3.1.5 Compound Data Structures

# Run the following code:

elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
print(elements)

#We can access elements in this nested dictionary like this.
h = elements["helium"]
hw = elements["helium"]["weight"]
print(h,"\n",hw)

#You can also add a new key to the element dictionary.
elements["oxygen"] = {"number":8,"weight":15.999,"symbol":"O"} 
print(elements)


#time = 70
