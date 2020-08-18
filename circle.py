import numpy as np
import os 
from scipy.spatial import distance
from perlin import PerlinNoiseFactory
import colorama
from colorama import Fore, Back, Style
from config import circle_config

def valMap(val,start1,stop1,start2,stop2):
	return start2 + (stop2 - start2) * ((val - start1) / (stop1 - start1))

def main(noise, speed,scale,height_scale,offSetHeight, character):
	COLORS_C=[Fore.BLUE,Fore.GREEN, Fore.YELLOW, Fore.RED,Fore.RED,Fore.YELLOW, Fore.GREEN,Fore.BLUE]
	xOff1 = 277
	while True:
		try:
			columns, rows = os.get_terminal_size(0)
		except OSError:
			columns, rows = os.get_terminal_size(1)
		#3D vector for center point, offset z by height
		height = offSetHeight
		center = np.array([columns/2, rows/2, height])
		#Defines width and radius or circle
		maxDist = columns/2
		minDist = columns/3
		stretch = maxDist-minDist
		#output (canvas)
		char = ""
		#shifting noise field
		xOff1+=speed
		xOff = xOff1
		for x in range(columns):
			yOff = 1235
			for y in range(rows):
				#current point's height
				n = noise(xOff,yOff)
				yOff +=scale
				#current point vector
				point = np.array([x,y,n*height_scale])
				#get distance between center and current point
				dist = distance.euclidean(center,point)
				#define the width and radius here
				if(dist<maxDist and dist > minDist):
					c = int(valMap(dist,minDist,maxDist,0,len(COLORS_C)))
					char+=COLORS_C[c]+character+Style.RESET_ALL
				else:
					char+=" "
			xOff +=scale
		os.system("cls")
		print(char)

if __name__ == '__main__':
	noise = PerlinNoiseFactory(2,1)

	conf = input("use config? [y/n]: ")

	if(conf=="y"):
		speed = circle_config['speed']
		scale = circle_config['scale']
		height_scale = circle_config['height_scale']
		offSetHeight = circle_config['offset_height']
		character = circle_config['character']
	else:
		speed = float(input("speed? [0.001-2]: "))
		scale = float(input("scale? [0.001-1]: "))
		height_scale = float(input("height scale? [0-30]: "))
		offSetHeight =float(input("off set height? [0-30]: "))
		character = input("plotting character: ")

	main(noise, speed,scale,height_scale,offSetHeight, character)
