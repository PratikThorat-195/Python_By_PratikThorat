# My requirement is to store the following details in single object
#  Student Number
#  Studnet Name
#  Internal Marks in three marks 
#  External marks in three marks
#  College Name

lst1 = [100, "Pratik", [25, 27, 32], [81, 78, 92], "SIEM"]
print(lst1, type(lst1), id(lst1)) # [100, 'Pratik', [25, 27, 32], [81, 78, 92], 'SIEM'] <class 'list'> 1272963426368

for val in lst1:
    print(val, type(val))

# 100 <class 'int'>
# Pratik <class 'str'>
# [25, 27, 32] <class 'list'>
# [81, 78, 92] <class 'list'>
# SIEM <class 'str'>

#==================================================================================
#
lst3 = [200, "Python",[23, 45, 56], [], "Rossum"]
print(lst3) 


print("-------------------------------------------------------------------")
lst2 = ["Pratik", 101, [67,89,92], [16,18, 20], "SIEM"]

for val in lst2:
    print(val, type(val))

lst2[2].append(91)
print(lst2)

lst2[3].insert(1, 68)
print(lst2)

lst2[2].sort()
print(lst2)


lst2[3].sort(reverse = "true")
print(lst2)

lst2[2].clear()
print(lst2)

del lst2[2]
print(lst2)

del lst2[3]
print(lst2)


lst2 = ["Pratik", 101, [67,89,92], [16,18, 20], "SIEM"]
print(lst2)

del lst2[2]
del lst2[3]
print(lst2)

lst2 = ["Pratik", 101, [67,89,92], [16,18, 20], "SIEM"]
del lst2[2]
del lst2[2]
print(lst2)

lst2.insert(3, [76, 77, 72])
print(lst2)

lst2[3][2] = 91
print(lst2)