def digital_root(n):
    chars=str(n)
    sum=int(n)
    while int(sum)>10:
        add=0
        for i in range(0,len(chars),1):
            add+=int(chars[i])
        sum=add
    return sum

print digital_root(333)