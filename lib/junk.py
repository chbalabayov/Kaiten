import string
from random import *

junk_code = ""
characters = string.ascii_letters + string.digits

for random_junk in range(150 or 250):
     junk_code += "\n// " + str("".join(choice(characters) for x in range(randint(30, 60))))