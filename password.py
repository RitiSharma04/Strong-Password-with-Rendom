# import string
# import random 
# print("welcome")
# def len(a):
#     b=string.digits
#     c=string.ascii_lowercase
#     d=string.ascii_uppercase
#     e=string.punctuation
#     sum=b+c+d+e
#     f=random.sample(sum,a)
#     password="".join(f)
#     print(password)
# a=int(input("enter the leanth  of password"))
# len(a)

import string
import random
from unicodedata import digit
b=int(input("enter the num:-"))
letter=string.ascii_letters
digits=string.digits
spacial_ch=string.punctuation
a=letter+digits+spacial_ch
s=list(a)
random.shuffle(s)
i=0
while i<=b:
    print(s[i],end="")
    i=i+1



