a = '''My name is Sujan.
I am learning multistring variable in python.
This is a multistring.'''

print(a)

#gives true false by checking if python is present or not in a.
print("python" in a) 
print("python" not in a)

#or
#If in

if "python" in a:
    print("Yes 'python' is in ", a)

# not in

if "Hello" not in a:
    print("Hello is not in ", a)

b = "Sujan"
#Because in python strings are stored as arrays

print(b[0])
print(len(b))

for x in "Hari":    
    print(x)
