import random
import time
def inorder(list1):
    i=0
    while i+1<len(list1):
        if list1[i] > list1[i+1]:
            return False
        i += 1
    return True

def bogo(lust):
    while not inorder(lust):
        random.shuffle(lust)
    return lust
list_1=[]
for i in range(11):
    list_1.append(random.randint(1,100))
print(list_1)


start =time.time()
print ("before: ",list_1)
list_1=bogo(list_1)
print ("after:",list_1)
print ("%.2f seconds" %(time.time()-start))
