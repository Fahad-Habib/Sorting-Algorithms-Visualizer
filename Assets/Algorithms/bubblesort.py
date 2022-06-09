import time
import select
# from time import sleep

x = time.time()
for i in range(16000000):
    pass
y = time.time()
print(y-x)
