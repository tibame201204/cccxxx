import time
import threading
from adafruit_servokit import ServoKit
import os
url = os.path.dirname(os.path.abspath(__file__))
os.chdir(url) 

class MyServo():
	def __init__(self):
		self.kit = ServoKit(channels=16)

	def servo(self, channel, angle_list):
		for angle in angle_list:
			self.kit.servo[channel].angle = angle
			time.sleep(0.5)

	def motion(self):
		# 把線程加入清單
		threads = []
		threads.append(threading.Thread(target = self.servo, args = (0, [90, 0, 45, 0])))
		threads.append(threading.Thread(target = self.servo, args = (3, [0, 90, 0, 45])))
		# 開啟多線程
		for i in range(len(threads)):
			threads[i].start()
		# 等待所有子執行緒結束
		for i in range(len(threads)):
			threads[i].join()
		print("motion Done...")


if __name__ == '__main__':
	# MyServo().servo(0, [90, 0, 45, 0])
	MyServo().motion()