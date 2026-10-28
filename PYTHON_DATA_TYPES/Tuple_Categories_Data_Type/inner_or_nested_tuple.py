# Inner or nested Tuple 
fq = (10, 100.99, "PT", (45,34,50), ("val1", "val2","Py"), "SIEM")
print(fq,type(fq)) # ---> (10, 100.99, 'PT', (45, 34, 50), ('val1', 'val2', 'Py'), 'SIEM') <class 'tuple'>

print(fq[0]) # ---> 10

print(fq[2], type(fq[2]), type(fq)) #---> PT <class 'str'> <class 'tuple'>

print(fq[0:3]) # ---> (10, 100.99, 'PT')
# ---------------------------------------------------------------------------------------------------------
print("---------------------------------------------------------------------------------------------------------")

# List in another List
lst = [100, 200, [101, 202, 303], [111,222,333], 300]

print(lst, type(lst)) #---> [100, 200, [101, 202, 303], [111, 222, 333], 300] <class 'list'>

print(lst[3][2]) #---> 333

print("---------------------------------------------------------------------------------------------------------")

# Tuple in another Tuple
tp = ("PT", "SC", "PM" ,("SIEM", "TTT","QQQ"), ("FFF", "UUU", "JJJ"),"CM")

print(tp, type(tp)) # ---> ('PT', 'SC', 'PM', ('SIEM', 'TTT', 'QQQ'), ('FFF', 'UUU', 'JJJ'), 'CM') <class 'tuple'>

print(type(tp[3])) # ---> <class 'tuple'>

print(type(tp[-2])) # ---> <class 'tuple'>

print(tp[-3][1]) # ---> TTT

print("---------------------------------------------------------------------------------------------------------")

# list in another tuple
lst_tp = (10, 20, "PT", ["UT", "AT", "PPT"], [70, 90, 98], 900990909)

print(lst_tp, type(lst_tp)) #---> (10, 20, 'PT', ['UT', 'AT', 'PPT'], [70, 90, 98], 900990909) <class 'tuple'>

print(type(lst_tp[3])) #---> <class 'list'>

lst_tp[3].append(11.11)

print(lst_tp) #---> (10, 20, 'PT', ['UT', 'AT', 'PPT', 11.11], [70, 90, 98], 900990909)

# lst_tp[1].append(12.12) ---> AttributeError: 'int' object has no attribute 'append'

# convert list to tuple

inner_lst = tuple(lst_tp[-3])

print(inner_lst) #---> ('UT', 'AT', 'PPT', 11.11)

# lst_tp[3] = inner_lst  TypeError: 'tuple' object does not support item assignment

print(lst_tp)

print("---------------------------------------------------------------------------------------------------------")

tp_lst = [10, 20, "PT", ("UT", "AT", "PPT"), (70, 90, 98), 900990909]

print(tp_lst, type(tp_lst)) #---> [10, 20, 'PT', ('UT', 'AT', 'PPT'), (70, 90, 98), 900990909] <class 'list'>

inner_tp = list(tp_lst[3])

tp_lst[3] = inner_tp

print(inner_tp, type(inner_tp)) #---> ['UT', 'AT', 'PPT'] <class 'list'>

print(tp_lst) #---> [10, 20, 'PT', ['UT', 'AT', 'PPT'], (70, 90, 98), 900990909]