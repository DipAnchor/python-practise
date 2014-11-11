def disemvowel(string):
    string=list(string)
    for i in range(0,len(string),1):
        word=string[i]
        print word
        if word=="a" or word=="A" or word=="e" or word=="E" or word=="i" or word=="I" or word=="o" or word=="O" or word=="u" or word=="U":
            string[i]=""
    string="".join(string)
    return string

answer=disemvowel("This website is for losers LOL!")

print answer