x = "awesome"

def myfun ():
    x = "fantastic"
    print("Python is " + x)

myfun()

print("Python is " + x)

"""
variables defined within and outside functions are different. 
Variables defined outside are GLobal i.e. can be used everywhere. (Gloval variable)
Variables inside function are specific to the function. (local variable)
To define global variable within a function we can use "global" syntax
"""

def sujan():
    global y
    y = "Global defined within function."
    x="Have a great"
    print(x + " Day")
sujan()
print(y)



