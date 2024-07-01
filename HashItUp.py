import hashlib
import time


time.sleep(1)
print("Hey")

time.sleep(1)
print("Im 0xRekin")

time.sleep(1)
print("I will hash your message using the SHA-256 algorithm")

time.sleep(1)
answer = input("Write me your message: ")
encoded_answer = answer.encode('utf-8')

h = hashlib.new("sha256") #You can change the hash algorithm

h.update(encoded_answer)

time.sleep(1)
print("SHA-256 Hash:", h.hexdigest())

time.sleep(10)

