import random
def randList(size=10, lower=1,upper=100):
    output=[]
    for i in range(size):
        random.randrange(lower,upper)
    return output

def compare_list_builtins(list1,list2):         #slick,sexy, small understandable, gets all the girls
    return list(set(list1).union(set(list2)))       #"not using builtins is like jerking it when your girl wants to fuck" - Ghandi

def compare_LIST_tull(list1,list2):             #mr slicks retarded cousin, does the same it just more shitty in every way
    output=[]
    for i in list1:
        if i in list2 and i not in output:
            output.append(i)
    return output
def complists(lists):
    output=[]
    temp=[]
    for n in range(len(lists)-1):
        output.append((compare_list_builtins(lists[n],lists[n+1])))
    for ind in output:
        for i in ind:
            temp.append(i)
    return set(temp)
print (complists([[1,2,3,4,5],[1,2,4,5,6,7,8],[9,6,10,3,2,4,5,6,3,3,3,5],[2,3,2,1,2,4,5],[1,2,3,4,5,6,7,8]]))