import threading
import time


class MyThread(threading.Thread):
	def __init__(self, threadId, name, delayTime):
		threading.Thread.__init__(self)
		self.threadId = threadId
		self.name = name
		self.delayTime = delayTime

	def run(self):
		print("Starting thread: ", self.name)

		threadLock.acquire()

		print_time(self.name, self.delayTime, 3)

		print("Finishin thread:", self.name)

		threadLock.release()

def print_time(name, delayTime, counter):
	while counter:
		time.sleep(delayTime)
		print(name, time.ctime(time.time()))
		counter -= 1

threadLock = threading.Lock()

thread1 = MyThread(1, "First", 1)
thread2 = MyThread(2, "Second", 1)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Program finished")