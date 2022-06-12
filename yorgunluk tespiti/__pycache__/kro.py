import time
from datetime import datetime
a=0
b=-1
while True:
    time.sleep(0.1)
    if(a%30==0):
        b+=1
        print("b:",b)
    a+=1
    an = datetime.now()
    qwe=time.time()
    asd=str(time.time()).split('.')
    print(a)