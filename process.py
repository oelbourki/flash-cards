import os
from multiprocessing import Process
import winsound
from time import sleep
def playsound(filename):
	print("playing " + filename)
	winsound.PlaySound(filename, winsound.SND_ASYNC)
	sleep(10)
def child_process():
	p = "./sounds/frPhysicsveuxwant2.wav"
	print(f"Child process, pid = {os.getpid()}")
	playsound(filename=p)

def parent_process():
	print(f"Parent process, pid = {os.getpid()}")
	p = Process(target=child_process)
	p.start()
	p.join()

if __name__ == '__main__':
	parent_process()