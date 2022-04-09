test=int(input())
for i in range(test):
    user_input=input()
    if '=' in user_input:
        print("skipped")
    else:
        user_input=user_input.split("+")
        answer= int(user_input[0])+int(user_input[1])
        print(answer)
