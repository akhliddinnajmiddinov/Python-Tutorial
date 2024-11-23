import threading
import time

def print_out(name, t, *args):
	time.sleep(t)
	print(name, *args)


thread1 = threading.Thread(target=print_out, args=("Salom", 2, 3))
thread2 = threading.Thread(target=print_out, args=("Salom", 1, 2, 3))


thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Program finished")