test=int(input())
answer=[]
for x in range(test):
    cities=int(input())
    cities_list=[]
    for i in range(cities):
        city=input()
        cities_list.append(city)
    cities_set=set(cities_list)
    answer.append(len(cities_set))    

for x in range(0, len(answer)):
    print(answer[x])