# import the opencv library 
import cv2 

class Camera():
	def __init__(self):
		self.vid = cv2.VideoCapture(0)
		_, self.frame = self.vid.read() 
		
	def capture(self):
		return self.frame


		