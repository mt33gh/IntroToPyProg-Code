#5.2 Variable Scope

# Run the following code:

## This will result in an error
def some_function():
    word = "hello"
print(word)            #NameError

## This works fine
def some_function():
    word = "hello"      # word in this function is different from word in the function below
    print(word)
def another_function():
    word = "goodbye"
    print(word)
some_function()
another_function()

## This works fine
word = "hello"       #global
def some_function():
    print(word)      #accessing the global variable
some_function()

## This is tricky
word = "hello"       #global
def some_function():
    word = "good-bye"  #local
    print(word)      #accessing the local variable
some_function()
print(word)          #global

#Notice that we can still access the value of the global variable `word` within this function. However, the value of a global variable can not be __modified__ inside the function. If you want to modify that variable's value inside this function, it should be passed in as an argument. You'll see more on this in the next quiz.
#Scope is essential to understanding how information is passed throughout programs in Python and really any programming language.



#time = 70
