def binToDec(binary):
    l=[]
    dec=0
    for i in binary:
        l.append(int(i))
    l.reverse()
    for i in range(len (l)):
        dec+=l[i]*2**i
    return dec
        
while True:
    b=input("Enter binary to convert to decimal and 0 to exit: ")
    if b=='0':
        print("end")
        break
    if b.isalnum():
        if '1' not in b or "0" not in b:
            print("error input")
            continue
        else:
            print(binToDec(b))
    else:
        print("error input")
