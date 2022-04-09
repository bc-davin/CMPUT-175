def selectionSort(data):
    #ascending order
    for index in range(len(data)):
        smallIndex=index
        #find smallest
        for i in range(index+1, len(data)):
            if (data[i]<data[smallIndex]):
                smallIndex=i
        #swap 
        temp=data[index]
        data[index]=data[smallIndex]
        data[smallIndex]=temp


