import string
import random

def gen():
    s1 = string.ascii_lowercase

    s2 = string.ascii_uppercase


    s4 = string.digits

    s5 = string.punctuation

    passlen = int(input("enter the length of the password\n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s4))
    s.extend(list(s5))
    

    random.shuffle(s)
    pas = ("".join(s[0:passlen]))
    print(pas)

gen()    