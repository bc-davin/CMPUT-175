def  bubbleSort(data):
    # siding from the last elements to front (ascending order)
    for last in range(len(data)-1,0,-1):
        for current in (last):
            if (data[current]>data[current+1]):
                #swap
                temp=data[current]
                data[current]=data[current+1]
                data[current+1]=temp

def bubbleSort_2(data):
    #siding from last elements to front(ascending order)
    # stop after list is sorted
    exchange=True
    last=len(data)-1
    while exchange and last>0:
        exchange=False
        for current in range(last):
            if (data[current]>data[current+1]):
                #swap
                temp=data[current]
                data[current]=data[current+1]
                data[current+1]=temp
                exchange=True
        last-=1
        
