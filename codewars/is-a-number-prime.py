import math
def is_prime(num):
  isprime=True
  if num>2:
    for i in range(2,int(math.sqrt(num)+1),1):
        pass
        if num%i==0:
            isprime=False
  if num<=0 or num==1:
      isprime=False
  if num==2:
      isprime=True
  return isprime
  

print is_prime(2)