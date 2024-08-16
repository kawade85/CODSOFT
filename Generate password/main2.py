# generate a password
#type 2

import string
import random
print("Generate a Password.")

if __name__ == "__main__" :
    m1 = string.ascii_lowercase
    m2 = string.ascii_uppercase
    m3 = string. digits
    m4 = string.punctuation

    passlen = int(input("Enter Password length : "))

    m = []
    m.extend(list(m1))
    m.extend(list(m2))
    m.extend(list(m3))
    m.extend(list(m4))

    random.shuffle(m)
    print("".join(m[0:passlen]))

