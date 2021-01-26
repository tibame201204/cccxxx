import time
from adafruit_servokit import ServoKit
import os
url = os.path.dirname(os.path.abspath(__file__))
os.chdir(url) 

class MyServo():
	def __init__(self):
		self.kit = ServoKit(channels=16)
	
	def run(self):
		self.kit.servo[0].angle = 180
		time.sleep(0.5)
		self.kit.servo[0].angle = 0
		time.sleep(0.5)
		self.kit.servo[0].angle = 180
		time.sleep(0.5)
		self.kit.servo[0].angle = 0



if __name__ == '__main__':
	MyServo().run()