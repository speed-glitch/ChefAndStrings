t = int(input())
a = []
for i in range (t):
    n = int(input())
    n_list = list(int(num) for num in input().strip().split())[:n]
    count = 0
    j=1
    for i in range(len(n_list)):
        if j<len(n_list):
            if (n_list[i]==n_list[j]):
                k=0
            else:
                k = abs(n_list[i]-n_list[j])-1
                i+=1
                j+=1
                count += k
    a.append(count)
for _ in range (t):
     print("%d"%(a[_]))
