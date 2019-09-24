def national_flag(A,i):
    less,equal,more = [],[],[]
    for a in A:
        if a < A[i]:
            less.append(a)
        elif a == A[i]:
            equal.append(a)
        else:
            more.append(a)
    A = less + equal + more
    return A



A = [0,1,1,2,2,3,3]
A = [2,1,0,1,1,2,3]
print(national_flag(A,int(len(A)/2)))