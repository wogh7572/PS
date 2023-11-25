for _ in range(int(input())):
    p = input()
    n = int(input())
    s = input()
    s = s[1:-1].split(',')
    if s==['']:
        s=[]
    flag_left = True
    cnt_left, cnt_right = 0, 0
    flag = True
    cnt=len(s)
    print(s)
    for f in p:
        if f=='R':
            if flag_left==True:
                flag_left=False
            elif flag_left==False:
                flag_left=True
        if f=='D':
            if cnt==0:
                flag=False
                break
            if flag_left:
                cnt_left+=1
                cnt-=1
            else:
                cnt_right+=1
                cnt-=1  

    s = s[cnt_left:len(s)-cnt_right]
    if flag:
        if flag_left:
            print('['+','.join(s)+']')
        else:
            print('['+','.join(s[::-1])+']')
    else:
        print("error")
