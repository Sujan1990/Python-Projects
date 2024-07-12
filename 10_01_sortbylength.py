# def myfunc(n):
#   return abs(n - 50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)

def myfunc(n):
  return len(n)

new_list = ['BABBON', 'BEAR', 'ELEPHANT', 'GIRRAFE', 'LION', 'TIGER', 'Hippopotamus', 'cat', 'dog']

new_list.sort(key =myfunc)
print(new_list)
