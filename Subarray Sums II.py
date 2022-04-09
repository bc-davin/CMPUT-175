n=int(input())
x=int(input())
a_list=[]
count=0
for i in range(0, n):
    user_input = input()
    a_list.append(user_input)
for i in range(0, len(a_list)):
    for j in range(i, len(a_list)):
        if(a_list[i]!=a_list[j]):
            if int(a_list[i])+int(a_list[j])==x:
                count+=2
print(count)