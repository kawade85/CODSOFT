#program to create a random password 
#type 1

import random
import string
print("Generate A Random Password.")

def my_fun():
    length = int(input("Enter the desired length of the password : "))
    lowdata = string.ascii_lowercase
    updata = string.ascii_uppercase
    digdata = string.digits
    symdata = string.punctuation

    combine = lowdata + updata + digdata + symdata
    x = random.sample(combine,length)
    password = "".join(x)
    print(password)
    my_fun()

my_fun() 