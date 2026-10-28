# Functionality of tuple is similar to List
# BUT Note: List --> Mutable, Tuple --> immutable
# Syntax: t1 = (val1, val2,..., valn)
t1 = (1, 2, 3, 4, 5)
print(t1, type(t1))  # (1, 2, 3, 4, 5) <class 'tuple'>

t2 = (100, "Pratik", 55.5, 'Pune')
print(t2, type(t2))  # (100, 'Pratik', 55.5, 'Pune') <class 'tuple'>

print(len(t1)) # 5
print(len(t2)) # 4

# Syntax: t1 = "Pratik", 45.54, 100, 4.5+56j, "Thorat"

t3 = "Pratik", 45.54, 100, 4.5+56j, "Thorat"
print(t3) # ('Pratik', 45.54, 100, (4.5+56j), 'Thorat')
# ---------------------------------------------------------------------------

t4 = (100, 200, 334.56, "Thorat", "PYTHON")
print(t4, type(t4))

# t4[0] = 300
# print(t4) # Error ----> TypeError: 'tuple' object does not support item assignment
# because it is not allowing to change it is immutable

print("--------------------------------------------------------------------------------------")

# Conversion list to tuple or tuple to list

# Convert this list to tuple
L1 = ["Pratik", 27, "Thorat", 99.99]
print(L1, type(L1)) # ['Pratik', 27, 'Thorat', 99.99] <class 'list'>

t1 = tuple(L1)
print(t1, type(t1)) # ('Pratik', 27, 'Thorat', 99.99) <class 'tuple'>

# Convert this tuple to list
ta2 = (100, 3458.5834, "Python", 45.05 - 5j)
print(ta2, type(ta2)) # (100, 3458.5834, 'Python', (45.05-5j)) <class 'tuple'>

La1 = list(ta2)
print(La1, type(La1)) # [100, 3458.5834, 'Python', (45.05-5j)] <class 'list'>

# ================================================================================================
t =(100, "Rossum", 55.55, 'Python')
print(t[0:3]) # (100, 'Rossum', 55.55) 

 