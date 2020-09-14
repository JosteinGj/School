import numpy as np
def allunique(list):
    if len(list)== len(set(list)):
        return True




def removeDuplicates(lists): return list(set(lists))
print(removeDuplicates([2,3,2,2,2]))
def inAbutnotB(a,b): return list(set(a).difference(set(b)))
def areorthagonal(a,b):
    return bool(np.dot(np.array(a),np.array(b)))
print(areorthagonal((0,1),[0,1]))

print((np.transpose(np.arange(1,16).reshape(3,5))))

