def NrImp(x,y):
    nr = 0
    for i in range(x,y+1):
        cnt = 0
        for j in range(1, i+1, 2):
            if i%j == 0:
                cnt = cnt +1


        if cnt == 3:
            nr = nr + 1

    return nr


print(NrImp(4,50))
print()

def divizor(a,b,k):
    nr = 0
    for i in range(a, b+1):
        if i%k == 0 and i%10 == k:
            nr = nr + 1

    return nr

print(divizor(3,50,4))
print()


def afisare(x,y,k):
    cnt = 0
    for i in range(x,y+1):
        cnt = cnt + 1
        print(i, end=" ")
        if cnt%k == 0:
            print("*" , end=" ")

    if cnt%k != 0:
        print("*")


afisare(11,22,4)


print()

def divX(n,x):
    list = []
    cnt = 0
    for i in range(1, 9999) :
        if i%x == 0:
            cnt = cnt + 1
            list.append(i)
            if cnt == n:
                break

    for i in range(cnt-1, -1, -1):
        print(list[i], end =" ")

divX(4,30)