# import the opencv library 
import cv2 

class Camera():
	def __init__(self):
		self.vid = cv2.VideoCapture(0)
		self.vid .set(cv2.CAP_PROP_FPS, 60)
		
		
	def capture(self):
		_, self.frame = self.vid.read() 
		self.frame =  cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
		return self.frame


		