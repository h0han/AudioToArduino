# import serial
import time
import pyaudio
import numpy as np
from scipy.io import wavfile
import soundfile as sf
import socket
import threading

# 이 부분은 블루투스 활용하는 거라 serial로 여시면 됩니다.
# bt=socket.socket(socket.AF_BLUETOOTH,socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)#
# pc_bt='c4:03:a8:53:5a:1f'
# port=13
# esp_bt='24:4c:ab:2c:e2:16'
# port2=1
# bt.bind((pc_bt,port))
# bt.connect((esp_bt,port2))
CHUNK = 4096
data, samplerate = sf.read('B_04546.wav')
print("Data", len(data))
print("Samplerate", samplerate)
for i in range(int(samplerate / CHUNK * (len(data) / samplerate))):
    part = data[range(CHUNK * i, CHUNK * (i + 1))]
    # bt.sendto(part,(esp_bt,port2))
    print(i)
print("rslt", int(samplerate / CHUNK * (len(data) / samplerate)))


