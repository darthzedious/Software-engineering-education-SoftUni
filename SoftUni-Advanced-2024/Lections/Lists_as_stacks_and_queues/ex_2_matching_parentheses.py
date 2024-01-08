expression = input()
stack = []
for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    if expression[i] == ")":
        start_index = stack.pop() # the index of the last "("
        print(expression[start_index:i+1])
