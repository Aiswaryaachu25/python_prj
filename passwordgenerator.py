import random
import string
password=""
l_min=int(input("enter the minimum limit"))
l_max=int(input("enter the maximum limit"))
limit = random.randint(l_min,l_max)
for i in range(limit):
        password =password+ random.choice(string.ascii_letters+string.digits+"#@!%&*$")
        
print(password)