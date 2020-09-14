def in_order(list1):
    for i in range(len(list1)-1):
        while list1[i]>list1[i+1]:
            return False
    return True

def bubble_sort(list1):
    while not in_order(list1):
        for i in range(len(list1)-1):
            if list1[i]>list1[i+1]:
                temp=list1[i+1]
                list1[i+1]=list1[i]
                list1[i]=temp
    return list1

print(bubble_sort([2,4,6,43,3,6,7]))
def selection_sort(list1):
    output=[]
    while len(list1)!=1:
        for i in range(len(list1)-1):
             if list1[i] == min(list1):
                 output.append(list1.pop(i))
    output.append(list1[0])
    return output
print(selection_sort([1,4,2]))


#hvilken som er best kommer an på hva som skal sorteres, denne implementasjonen av selection sort vil bruke like lang tid uansett hvor sortert inputen er
# mens bubble sort trenger bare sjekker om listen er sortert hvis den allerede er det. begge har O(n^2) tidskompleksitet.
