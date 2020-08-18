import numpy as np
import cv2
import os
from os import system
from os import path
import colorama
from colorama import Fore, Back, Style
# system('mode con: cols=200 lines=49')

def main(video, color, showVid=False, invert=True,movies=[]):
	idx = 0
	while True:
		if(len(movies)>0):
			cap = cv2.VideoCapture(movies[idx])
			idx+=1;
			if(idx==len(movies)):
				idx=0
		else:
			cap = cv2.VideoCapture(video)
		frame_counter=0
		chars =[" ", ".", "-","=","X","#","D","N"]
		thresh = int(256/len(chars))+2
		while(cap.isOpened()):
			try:
				columns, rows = os.get_terminal_size(0)
			except OSError:
				columns, rows = os.get_terminal_size(1)
			ret, frame = cap.read()
			frame_counter += 1

			if frame_counter == cap.get(cv2.CAP_PROP_FRAME_COUNT):
				if(len(movies)>0):
					break
				else:
					frame_counter = 0 
					cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

			gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
			if(invert):
				gray = cv2.bitwise_not(gray)
			w = gray.shape[0]
			h = gray.shape[1]
			char=""
			cols = columns
			rows = rows
			for x in range(cols):
				for y in range(rows):
					dx = int(w*x/cols)
					dy = int(h*y/rows)
					if(dx<w and dy<h):
						val = int(gray[dx,dy]/thresh)
						char+=chars[val]

			# os.system("cls")
			print(color+char)
			if(showVid and len(movies)==0):
				cv2.imshow('frame',gray)
				if cv2.waitKey(1) & 0xFF == ord('q'):
					break
		cap.release()
		cv2.destroyAllWindows()
		if(len(movies)>0):
			continue
		else:
			break;


if __name__ == '__main__':
	colorama.init()

	stackFiles = input("Stack movies? [y/n]:")
	movies=[]
	if(stackFiles=="y"):
		stackFiles = True
		movies = []
	else:
		stackFiles=False
	videoNotFound = True
	while videoNotFound:
		video ="./data/"+input("which video?: ")
		if(path.exists(video)):
			print("")
			if(stackFiles):
				print("File exists:"+str(path.exists(video)))
				print("")
				movies.append(video)
				ans=input("Add more? [y/n]: ")
				if(ans=="n"):
					videoNotFound=False
			else:
				videoNotFound=False
				print("File exists:"+str(path.exists(video)))
				print("")
		else:
			print("")
			print("FILE NOT FOUND!")
			print("")
	while True:
		print("")
		showVid = input("show video? [y/n]: ")
		if(showVid =="y"):
			showVid=True
			break
		elif(showVid=="n"):
			showVid=False
			break
	while True:
		print("")
		invert = input("invert? [y/n]: ")
		if(invert =="y"):
			invert=True
			break
		elif(invert=="n"):
			invert=False
			break
	COLORS = ["red", "yellow", "green", "blue", "white"]
	COLORS_C=[Fore.RED,Fore.YELLOW, Fore.GREEN,Fore.BLUE,Fore.WHITE]
	color=""
	while True:
		print("")
		color = input("Which Color?: ")
		if color in COLORS:
			print("")
			print("COLOR: "+color)
			color = COLORS_C[COLORS.index(color)]
			break
		else:
			print("")
			print("Color Not Found.")

	main(video,color,showVid,invert,movies)

