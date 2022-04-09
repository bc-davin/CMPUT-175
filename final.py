greeting=input()
count=0;
for element in range(0, len(greeting)):
    if greeting[element]=='e':
        count+=1;
greeting = greeting[0]+'e'*count*2+greeting[-1]
print(greeting)
