def my_search( data, key ):
    found = False
    low = 0
    count = 0
    print(len(data))
    high=len(data)-1
    while ( not found and low<=high):
        print(high, low)
        guess = (high+low)//2
        print('guess: ', guess)
        if ( key == data[guess] ):
            found = True
            count = 1
            k = guess - 1
            while k>=0 and data [k] == key:
                count += 1
                k -= 1
            k = guess + 1
            while k < len(data) and data [k] == key:
                count += 1
                k += 1
        else:
            if (key < data[guess]):
                high=guess-1
            else:
                low = guess+1
    print('count:', count)
    return count
def main():
    my_search([1,1,2,2,3,3,3,3,3,3,6,7], 1)
    print()
    my_search([1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 6, 7, 7, 7, 7], 7)
    print()
    my_search([1, 1, 2, 2, 3, 3, 3, 3, 3, 3, 6, 7, 7, 7, 7], 6.5)
main()

