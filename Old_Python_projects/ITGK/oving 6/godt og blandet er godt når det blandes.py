def is_six_at_edge(list1):
    if list1[0]==6 or list1[-1]==6:
        return True
    else:
        return False
def avg(list):
    return sum(list)/len(list)
def median(list):
    list.sort()
    return list[len(list)//2]