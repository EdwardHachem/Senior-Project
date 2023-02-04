#this will visualize wav files
from scipy.io.wavfile import read
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
user_fil = input("Enter name of wav file: ")
input_data = read(user_fil)
audio = input_data[1]
rate_num = input_data[0]
print(rate_num)
print(len(audio))
vid_dur = float(len(audio)/rate_num)
print(vid_dur)
plt.plot(audio[0:62581760])
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()
