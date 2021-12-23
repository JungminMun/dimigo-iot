#Filter in over face

import cv2
from PIL import Image
import numpy as np

def hello():
	print("1. head Ghost")
	print("2. real Ghost")
	print("3. real filter")

while True:
	hello()
	userInput = input()

	# 강아지, 선글라스

	if(userInput == "1"):
		maskPath = "headGhost.png"

		faceCascade = cv2.CascadeClassifier('face.xml')

		mask = Image.open(maskPath)

		def thug_mask(frame):
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			faces = faceCascade.detectMultiScale(gray, 1.15)

			# NumPy 배열을 Image 객체로 바꿀 때
			background = Image.fromarray(frame)

			for (x,y,w,h) in faces:
				resized_mask = mask.resize((w, h), Image.ANTIALIAS)
				background.paste(resized_mask, (x,y - h), mask=resized_mask)

			return np.asarray(background)

		cap = cv2.VideoCapture(0)

		while True:
			flag, img = cap.read()

			cv2.imshow('VIDEO', thug_mask(img))

			key = cv2.waitKey(1)

			if key == ord('q'):
				break

	elif(userInput == "2"):
		maskPath = "newGhost.png"

		faceCascade = cv2.CascadeClassifier('face.xml')

		mask = Image.open(maskPath)

		def thug_mask(frame):
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			faces = faceCascade.detectMultiScale(gray, 1.15)

			# NumPy 배열을 Image 객체로 바꿀 때
			background = Image.fromarray(frame)

			for (x,y,w,h) in faces:
				resized_mask = mask.resize((w * 2, h * 2), Image.ANTIALIAS)
				neyX = x * 0.25
				background.paste(resized_mask, (int(x - neyX),y), mask=resized_mask)

			return np.asarray(background)

		cap = cv2.VideoCapture(0)

		while True:
			flag, img = cap.read()

			cv2.imshow('VIDEO', thug_mask(img))

			key = cv2.waitKey(1)

			if key == ord('q'):
				break


	elif(userInput == "3"):
		maskPath = "filter1.png"

		faceCascade = cv2.CascadeClassifier('face.xml')

		mask = Image.open(maskPath)

		def thug_mask(frame):
			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

			faces = faceCascade.detectMultiScale(gray, 1.15)

			# NumPy 배열을 Image 객체로 바꿀 때
			background = Image.fromarray(frame)

			for (x,y,w,h) in faces:
				resized_mask = mask.resize((w, h), Image.ANTIALIAS)
				background.paste(resized_mask, (x ,y), mask=resized_mask)

			return np.asarray(background)

		cap = cv2.VideoCapture(0)

		while True:
			flag, img = cap.read()

			cv2.imshow('VIDEO', thug_mask(img))

			key = cv2.waitKey(1)

			if key == ord('q'):
				break
	elif(userInput == "Q"):
		exit()
