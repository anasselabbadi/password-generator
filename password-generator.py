import random
import time
from string import digits,punctuation, ascii_letters
length=20
symbols=ascii_letters+digits+punctuation
secure_random = random.SystemRandom()
password="".join(secure_random.choice(symbols)for i in range (length))
print(password)
time.sleep(6)
