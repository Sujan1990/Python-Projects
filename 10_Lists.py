#list stores collection of data. 
#in pyhton 4 data type stores collection of data i.e. tuble, set, dict and list
#list items are ordered - like first to last, [indexed], changeable -tuple is not changable, and allow duplicate values.
#list items can of any data type.
#list can also contain different data type in its items
#we can create list by using list constructor i.e. list()

thislist = ["apple", "banana", "cherry", "blueberry" , "watermelon"]
# print(thislist) 
# print(len(thislist))

mylist = list(('mango','khasiko masu','bhat','golveda ko achar','kauli','saag'))
# print(mylist)

#negative indexing means staring from the end, -1 is the end there is no 0 in the end (only at the beginning)
# print(mylist[-1])
# print(mylist[-2])

# #we can also define range of indexes
# print(mylist[2:5]) #here 5 is excluded
# print(mylist[:4])
# print(mylist[1:])
# print(mylist[-4:-1]) #here -1 is excluded

#in can be used in list (why no not in?)

# if 'masu' in mylist:
#     print("Yes, 'masu' is in the list.")
# elif 'khasiko masu' in mylist:
#     print("Yes 'khasiko masu' is in the list")
# else:
#     print("Sorry no masu.")

#changing item value
# print(mylist.index('kauli'))
mylist[4] = 'kakro'
# print(mylist)

#changing can also be done in a range
thislist[1:3] = ['mango', 'edberen']
# print(thislist)

#if we insert more items than indicated in range, the item will be inserted
#where specified and existing items with be pushed back
thislist[3:4] = ["grapes", "guava"]
# print(thislist)

thislist[1:3] = ["sitafal"]  #if less items are inserted the item for whom the value was not assinged will be removed
# print(thislist)

#we can insert new without replacing by insert()
thislist.insert(2, "banana")
# print(thislist)

#append list items
mylist.append("mohi")
# print(mylist)

#extend list is used to join two lists or add any iterable. it can be tuble, sets, dicts etc.
mylist.extend(thislist)
# print(mylist)

#remove deletes specifc item
mylist.remove('sitafal')
# print(mylist)

#to remove specified index use pop()
mylist.pop(9)
# print(mylist)
# here if we do not sepcify index pop removed the last item
mylist.pop()
mylist.pop()    
# print(mylist)

#del can also be used to remove the specified index
# or the list completely if index is not specified
del mylist[8]
# print(mylist)
# del mylist 
#del will delete the lsit hence we will get error message

#clear() empties the list, the list remains but has no items, no error message
# print(thislist)
thislist.clear()
# print(thislist)

#loop list by using for.

looplist = ['A','B','C','D','E','F','G']

# for x in looplist:
#     print(x)

#we can also loop through the index numbers
# for i in range(len(looplist)):
#     print(looplist[i])

#using while loop in list
# i = 0
# while i < len(looplist):
#     print(looplist[i])
#     i += 1 #same as i = i + 1, only for integeres as i+=1 can be used for list dict also, will learn later

#looping using list comprehension
# listcomprehension = [print(x.lower()) for x in looplist]

#List Comprehension
#it provides a shorter syntax for when you want to create a new list based on the values of 
#existing list
animals = ['tiger','lion','elephant','bear','babbon','girrabe']

# print(animals)
# for i in animals:
#     print(i)

#animals containing b in thier name
# b_list =[]
# for i in animals:
#     if 'b' in i:
#         b_list.append(i)
# print(b_list)

#with the help of list comprehension this can be done in single line

b_list = [x for x in animals if 'b' in x]
# print(b_list)

#syntax for list comprehension is as follows:
# newlist = [expression 'for' item 'in' iterable 'if' condition == True] 
# in python expression is a result of some operation, here it is the current item in the iteration which is the outcome or which can be maniputaled before appending in the list
#condition part is optional however most of the times reason of doing lsit comprehension

nob_list = [x for x in animals if x != 'girrabe']
# print(nob_list)

new_list = [x for x in animals]
# print(new_list)

#range() can be used to create iterable
new_list = [x for x in range(10)]
# print(new_list)

new_list = [x for x in range(10) if x <= 5]
# print(new_list)

new_list = [x.upper() for x in animals]
# print(new_list)

new_list = [x if x!='GIRRABE' else 'GIRRAFE' for x in new_list]
# print(new_list)

#sorting list in python
#sort() will sort the list alphnumerically ascending order automatically
new_list.sort()
#print(new_list.sort()) this does not work as .sort() does not return a value, it only modifies the original list.
# print(new_list)

#for descending sort, use argument reverese = Ture
new_list.sort(reverse=True)
# print(new_list)

# we can also use our own sort function by using the keyword argument key = function

def myfunc(n):
    return len(n)

new_list.sort(key =myfunc)
# print(new_list)

new_list.extend(['cat','dog'])
new_list.sort()     #sort is case sensative i.e. cpaital letters are sorted before lower case
# print(new_list)

#so we can build in case-insensative sort function
new_list.sort(key = str.lower)
print(new_list)


#Reserve() will reverese the current sorting order of the elements irrespective of alphabets.
# print(mylist)
mylist.reverse()
print(mylist)

# Copying of lsit (not list1=list2)
list1 = ['ABC','DEF','GHI']
list2 = ['MNO','XYZ','PQR']

list3 = list1.copy()
print(list3)

#use built in list() function

list4=list(list2)
print(list4)

#join or concatenate list 
#using + operator
list3 = list1+list2
print(list3)

#using for loop

for x in list2:
    list1.append(x)

print(list1)

new_list.extend(mylist)
print(new_list)