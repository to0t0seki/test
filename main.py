from threading import Thread

print("Hello World")
print("Hello World")
t = Thread(target=print, args=("Hello World",))
t.start()
t.join()
