num = int(input())
inputs = []

for i in range(num):
    user_input = input()  
    inputs.append(user_input)  

test = "amfoss"
for input_string in inputs:
    count = 0
    for i in range(min(len(input_string), len(test))):
        if input_string[i] != test[i]:   
            count+=1
    # count += abs(len(input_string) - len(test))
    print(count)
