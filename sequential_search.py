def sequential_search(data, key):
    found= False
    index=0
    while (not found):
        #compare each data
        if (key==data[index]):
            found=True
        else:
            #move index to move to next data
            index+=1
    if (not found): #in the event if it is not found
        index=-1
    return index 




