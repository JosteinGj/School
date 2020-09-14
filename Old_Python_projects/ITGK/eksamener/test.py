def datacap(array,minval,maxval):
    for i in range(len(array)):
        print(array[i])
        if array[i]<minval:
            array[i]=minval
        elif array[i]>maxval:
            array[i]=maxval
    return array

print(datacap([-90,20,100],-50,50))