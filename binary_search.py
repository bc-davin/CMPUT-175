def binary_search(data, key):
    found=False
    low=0
    high=len(data)-1
    while (not found and low<=high):
        guess=(high+low)//2
        if (key==data[guess]):
            found=True
        else:
            if (key<data[guess]):
                high=guess-1;
            else:
                low=guess+1
    if (not found):
        guess=-1
    return guess 

