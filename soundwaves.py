import pyaudio
import struct 
import numpy as np
import scipy.fftpack 
import os
import matplotlib.pyplot as plt
import time

def valMap(val,start1,stop1,start2,stop2):
	return start2 + (stop2 - start2) * ((val - start1) / (stop1 - start1))

CHUNK = 1024 * 4
FORMAT = pyaudio.paInt16 
CHANNELS = 1 
RATE = 44100


p = pyaudio.PyAudio()

stream = p.open(
	format=FORMAT,
	channels=CHANNELS,
	rate=RATE,
	input=True,
	output=True,
	frames_per_buffer=CHUNK
	)


x = np.arange(CHUNK/2)
print(x.shape)

while True:
	try:
		columns, rows = os.get_terminal_size(0)
	except OSError:
		columns, rows = os.get_terminal_size(1)
	data = stream.read(CHUNK)
	data_int = np.array(struct.unpack(str(2*CHUNK)+ 'B',data), dtype='b')

	fourier = scipy.fftpack.fft(data_int)
	fourier_real = fourier[0:len(fourier)//4]
	
	char = ""

	for i in range(rows):
		for j in range(columns):
			index = len(fourier_real)*j//columns - 1
			val = np.abs(np.real(fourier_real[index]))
			n = valMap(val, 0, 250000, 0, columns)
			if (rows-i-n<=0):
				char+="*"
			else:
				char+=" "
	os.system("cls")
	print(char)