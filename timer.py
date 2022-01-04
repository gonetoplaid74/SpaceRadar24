from time import time, sleep

while True:
    sleep(1 - time() % 1)
    exec(open('hst1.py').read()) 
    exec(open('iss.py').read())
    exec(open('TIANHE.py').read())