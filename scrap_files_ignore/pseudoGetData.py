import time
import json
import random
c = 0
while True:
    time.sleep(0.3)
    output = []
    for _ in range(1,42):
        output.append(random.randint(10000,1000000000000000000000))
        # data.append(output)
    print(json.dumps(output))
    c = c + 1 
