while True:
    s = input()
    flag=True
    if s=='.':
        break
    stack = []
    for i in s:
        if i=='[':
            stack.append(i)
        elif i=='(':
            stack.append(i)
        elif i==']':
            if len(stack)==0:
                flag=False
                break
            if stack.pop()=='[':
                continue
            else:
                flag=False
                break
        elif i==')':
            if len(stack)==0:
                flag=False
                break
            if stack.pop()=='(':
                continue
            else:
                flag=False
                break
    if stack:
        flag=False
    if flag:
        print('yes')
    else:
        print('no')