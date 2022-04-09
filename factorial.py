def factorial(n):
    if (n==1 or n==0): #base cases 
        return 1
    else:
        answer=n*factorial(n-1) #inductive step 
    return answer