n, m = map(int, input().split())

lst = []
cnt = [] 

for _ in range(n):
    lst.append(input())

for i in range(n-7):
    for j in range(m-7):
        w=0 #w로 시작하는 경우
        b=0 #b로 시작하는 경우

        for k in range(i,i+8):
            for l in range(j, j+8):
                if(l+k)%2 == 0:
                    if lst[k][l] != 'W':
                        w+=1
                    else: 
                        b+=1
                else:
                    if lst[k][l] !='B':
                        w+=1
                    else:
                        b+=1
        cnt.append(w)
        cnt.append(b)

print(min(cnt))

        