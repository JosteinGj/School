import random

def randList(size=10,lower=0,upper=100):
    return_value=[]
    for i in range(1,size):
        return_value.append(random.randrange(lower,upper))
    return return_value
print (randList())
def comparelist(list1,list2):
    return list(set(list1).union(set(list2)))
    #å ikke bruke innebygdefunksjoner,
    #er som å runke når dama vil pule
def comparelist_tull(list1,list2):
    output=[]
    for i in list1:
        if i in list2 and i not in output :
            output.append(i)
    return output
print(comparelist_tull([0,1,2,3],[2,3,4,5,6]))
