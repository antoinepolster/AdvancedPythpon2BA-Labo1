import time
import threading

def hello():
    while True:
        time.sleep(1)
        print('hello')

thread = threading.Thread(target=hello, daemon=True)

thread.start()
while True:
    time.sleep(1)
    print('bye')