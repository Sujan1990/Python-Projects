#list stores collection of data. 
#in pyhton 4 data type stores collection of data i.e. tuble, set, dict and list
#list items are ordered - like first to last, [indexed], changeable -tuple is not changable, and allow duplicate values.
#list items can of any data type.
#list can also contain different data type in its items
#we can create list by using list constructor i.e. list()

thislist = ["apple", "banana", "cherry", "blueberry" , "watermelon"]
print(thislist) 
# print(len(thislist))

mylist = list(('mango','khasiko masu','bhat','golveda ko achar','kauli','saag'))
print(mylist)

#negative indexing means staring from the end, -1 is the end there is no 0 in the end (only at the beginning)
# print(mylist[-1])
# print(mylist[-2])

# #we can also define range of indexes
# print(mylist[2:5]) #here 5 is excluded
# print(mylist[:4])
# print(mylist[1:])
# print(mylist[-4:-1]) #here -1 is excluded

#in can be used in list (why no not in?)

if 'masu' in mylist:
    print("Yes, 'masu' is in the list.")
elif 'khasiko masu' in mylist:
    print("Yes 'khasiko masu' is in the list")
else:
    print("Sorry no masu.")

#changing item value
print(mylist.index('kauli'))
mylist[4] = 'kakro'
print(mylist)

#changing can also be done in a range
thislist[1:3] = ['mango', 'edberen']
print(thislist)

#if we insert more items than indicated in range, the item will be inserted
#where specified and existing items with be pushed back
thislist[3:4] = ["grapes", "guava"]
print(thislist)

thislist[1:3] = ["sitafal"]  #if less items are inserted the item for whom the value was not assinged will be removed
print(thislist)

#we can insert new without replacing by insert()
thislist.insert(2, "banana")
print(thislist)

#append list items
mylist.append("mohi")
print(mylist)

#extend list is used to join two lists or add any iterable. it can be tuble, sets, dicts etc.
mylist.extend(thislist)
print(mylist)