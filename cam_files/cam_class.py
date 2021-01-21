import cv2

# cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0)                      
# waitframe = 100     


class MyCamera():
	def __init__(self):
		self.cap = cv2.VideoCapture(0)
		self.waitframe = 100
	def cap_status(self):
		if not self.cap.isOpened():
			print("Cannot open camera")
			exit()
	def cap_read_status(self):
		ret, frame = self.cap.read()
		if not ret:
			print("Can't receive frame (stream end?). Exiting ...")
			exit()
		return ret, frame

	def basic_test(self):
		while True:
			success, img = self.cap.read()
			if not success:
				break
			cv2.imshow("basic_test", img)
			ch = cv2.waitKey(self.waitframe)
			if ch == 27 or ch == ord('q') or ch == ord('Q'):
				cv2.waitKey(300)
				print('Quitting')
				break
		self.cap.release()
		cv2.destroyWindow("basic_test")

	def color_test(self):
		import numpy as np
		# 啟動Camera設定變數
		ret, frame = self.cap.read()
		rows, cols, _ = frame.shape
		x_medium = int(cols / 2)
		center = int(cols / 2)
		cap_status()

		while (True):
			# color to gray
			hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

			# yellow color
			low_yellow = np.array([26, 43, 46])
			high_yellow = np.array([34, 255, 255])
			yellow_mask = cv2.inRange(hsv_frame, low_yellow, high_yellow)

			contours, _ = cv2.findContours(yellow_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
			contrours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

			for cnt in contrours:
				(x, y, w, h) = cv2.boundingRect(cnt)
				cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
				x_medium = int((x + x + w) / 2)
				y_medium = int((y + y + h) / 2)
				print("x_medium", x_medium, "y_medium", y_medium)
				# cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 0, 255), 2)
				break

			# 顯示圖片
			cv2.imshow('color_test', frame)
			cv2.imshow("color_mask", yellow_mask)
			# 按下 q 鍵離開迴圈
			if cv2.waitKey(1000) == ord('q'):
				break

		# 釋放該攝影機裝置
		self.cap.release()
		cv2.destroyWindow("color_test")
		cv2.destroyWindow("color_mask")

	def face_test(self):
		ret, frame = self.cap.read()
		rows, cols, _ = frame.shape
		x_medium = int(cols / 2)
		center = int(cols / 2)

		if not self.cap.isOpened():
			print("Cannot open camera")
			exit()

		faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
		cap = cv2.VideoCapture(0)
		while (cap.isOpened()):
			ret, imagename = self.cap.read()
			if not ret:
				print("Can't receive frame (stream end?). Exiting ...")
				break
			faces = faceCascade.detectMultiScale(imagename, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
												 flags=cv2.CASCADE_SCALE_IMAGE)
			cv2.rectangle(imagename, (10, imagename.shape[0] - 20), (110, imagename.shape[0]), (0, 0, 0), -1)
			cv2.putText(imagename, "Find " + str(len(faces)) + " face!", (10, imagename.shape[0] - 5),
						cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
			for (x, y, w, h) in faces:
				cv2.rectangle(imagename, (x, y), (x + w, y + h), (128, 255, 0), 2)
			cv2.imshow("face_test", imagename)

			x_medium = int((imagename.shape[1]) / 2)
			cv2.line(frame, (x_medium, 0), (x_medium, 480), (0, 0, 255), 2)

			k = cv2.waitKey(1)
			# 按下 z 鍵離開迴圈
			if k == ord("z") or k == ord("Z"):
				break

		# 釋放該攝影機裝置
		cap.release()
		cv2.destroyWindow("face_test")

if __name__ == "__main__":
	# MyCamera().basic_test()
	# MyCamera().color_test()
	MyCamera().face_test()