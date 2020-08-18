import pyaudio
import struct
import numpy as numpy
import os 
from perlin import PerlinNoiseFactory
import colorama
from colorama import Fore, Back, Style



def createChars(noise, xOff2, xOffDown2, columns, rows,color,scale):
	char=""
	xOff=xOff2
	xOffDown=xOffDown2
	for i in range(rows):
		yOff=123
		yOffDown=23
		for j in range(columns):
			n = noise(xOff,yOff)
			nd = noise(xOffDown, yOffDown)
			if(n>-0.06 and nd>-0.05):
				char+="#"
			else:
				char+=" "
			yOff += scale
			yOffDown += scale
		xOff+=scale
		xOffDown+=scale
	os.system("cls")
	print(color+ char)

if __name__ == '__main__':
	colorama.init()
	noise = PerlinNoiseFactory(2,1)
	scale=0
	xOff2 = 213
	xOffDown2 =1337
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
	speed = 0
	while True:
		try:
			print("")
			speed = float(input("Speed?: "))
			break
		except KeyboardInterrupt:
			exit()
			pass
		except:
			pass
	scale = 0.01
	while True:
		try:
			print("")
			scale = float(input("Scale?: "))
			break
		except KeyboardInterrupt:
			exit()
			pass
		except:
			pass

	while True:
		try:
			columns, rows = os.get_terminal_size(0)
		except OSError:
			columns, rows = os.get_terminal_size(1)
		xOff2 +=speed
		xOffDown2-=speed
		
		createChars(noise, xOff2, xOffDown2, columns, rows, color, scale)




# CHUNK = 1024* 4
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE=44100


# p = pyaudio.PyAudio()

# stream = p.open(
# 	format=FORMAT,
# 	channels=CHANNELS,
# 	rate=RATE,
# 	input=True,
# 	output=True,
# 	frames_per_buffer=CHUNK
# )

# data = stream.read(CHUNK)
# data_int = np.array(struct.unpack(str(2*CHUNK)+'B',data), dtype='b')[::2]+127





