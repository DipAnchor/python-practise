def solution(n):
    #using dict to achieve
    single=n%10
    tens=(n-n%10)%100
    hunders=(n-n%100)%1000
    thousands=(n-n%1000)%10000
    dictsingle={0:'',1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII',8:'VIII',9:'IX'}
    dicttens={0:'',10:'X',20:'XX',30:'XXX',40:'XL',50:'L',60:'LX',70:'LXX',80:'LXXX',90:'XC'}
    dicthunders={0:'',100:'C',200:'CC',300:'CCC',400:'CD',500:'D',600:'DC',700:'DCC',800:'DCCC',900:'CM'}
    dictthousands={0:'',1000:'M',2000:'MM',3000:'MMM'}
    result=dictthousands.get(thousands)+dicthunders.get(hunders)+dicttens.get(tens)+dictsingle.get(single)
    return result

print solution(1999)