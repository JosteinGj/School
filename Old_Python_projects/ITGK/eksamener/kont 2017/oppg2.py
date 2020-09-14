def file_to_list(filename):
    output=[]
    file=open(filename)
    for lines in file:
        lines=lines.rstrip()
        data=lines.split("\t")
        data[2]=float(data[2])
        output.append(data)
    return output

def list_stores(datalist):
    output=[]
    for i in datalist:
        if i[0] not in output:
            output.append(i[0])
    return output
def sum_store_prices(datalist,storelist):
    output=[0]*len(storelist)
    for i in range(len(storelist)):
        for a in datalist:
            m
            if storelist[i]==a[0]:
                output[i]+=a[2]
    return output


data=file_to_list("test.txt")
stores=list_stores(data)
print(stores)
print(sum_store_prices(data,stores))

