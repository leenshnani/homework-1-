def func(k,v):
    d=dict()
    for i in range(len(k)):
        d[k[i]]=v[i]
    return d

L1=['HTTP','HTTPS','FTP','DNS']
L2=[80,443,20,53] 
print(func(L1,L2))
