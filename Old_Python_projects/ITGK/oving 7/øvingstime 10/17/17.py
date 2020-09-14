list_1 = list(range( 10 ))
print( list_1 )
list_1 [ -1 ] = 5
print(list_1)
list_1[0::2]= [2]*(len(list_1) // 2)
print(list_1)
def half_list(list1):
    return list1[:len(list1) // 2]
print(half_list(list_1))


print(list_1[1:7:2])