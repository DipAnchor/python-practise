def digital_root(n):
    chars=str(n)
    add=0
    for i in range(0,len(chars),1):
         add+=int(chars[i])
    if add<10:
        return add
    else:
        return digital_root(add)
    

print digital_root(1245)
