#2.2 Operators: Arithmetic, Assignment, Comparison, Logical
#2.2.3 Comparison Operators and Logical Operators
#Comparison Operators
#Symbol Use Case	Bool	Operation
#   5 < 3	        False	Less Than
#   5 > 3	        True	Greater Than
#   3 <= 3	        True	Less Than or Equal To
#   3 >= 5	        False	Greater Than or Equal To
#   3 == 5	        False	Equal To
#   3 != 5	        True	Not Equal To

#Logical Use	        Bool	Operation
#   5 < 3 and 5 == 5	False	and - Evaluates if all provided statements are True
#   5 < 3 or 5 == 5	    True	or - Evaluates if at least one of many statements is True
#   not 5 < 3	        True	not - Flips the Bool Value

#Run the following code:

age = 14
is_teen = age > 12 and age < 20
print(is_teen) # True

#time = 50
# This code demonstrates comparison and logical operators.