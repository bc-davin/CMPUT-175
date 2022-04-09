def hanoi(n,fromPole,toPole,withPole):
    if n==1:
        print('Move disk '+str(n)+' from '+fromPole+' to '+toPole) #base case 
    else:
        #inductive steps 
        hanoi(n-1,fromPole,withPole,toPole)
        print('Move disk '+str(n)+' from '+fromPole+' to '+toPole)
        hanoi(n-1, withPole,toPole,fromPole)
