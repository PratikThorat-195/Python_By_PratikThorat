t = 10, "PT", 45.65
print(t, type(t)) #------------> (10, 'PT', 45.65) <class 'tuple'>

print(t.index(10)) #-----------> 0

print(t.count(10)) #-----------> 1

t1 = -89,89,-18,99,-9,76,-77,-54,0
print(t1, type(t1)) #----------> (-89, 89, -18, 99, -9, 76, -77, -54, 0) <class 'tuple'>

x = sorted(t1)

print(x, type(x)) #------------> [-89, -77, -54, -18, -9, 0, 76, 89, 99] <class 'list'>

t2 = tuple(x)

print(t2, type(t2)) #----------> (-89, -77, -54, -18, -9, 0, 76, 89, 99) <class 'tuple'>

# ---------------------------
# The Functions not present in tuple
# ---------------------------
# append()
# insert()
# remove()
# clear()
# pop(index)
# pop()
# reverse()
# sort()
# copy()
# extend()
# ---------------------------------------
# NOTE:-   By Using  del Operator we can't  delete values of tuple object By using Indexing and   slicing but we can delete entire object