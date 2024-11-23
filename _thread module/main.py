import _thread
import time


def print_out(name, *args):
	print(name, *args)


thread1 = _thread.start_new_thread(print_out, ("Frank", 1))
thread2 = _thread.start_new_thread(print_out, ("Frank", 1, 2))

time.sleep(0.5)