import os
import random
import librosa
from matplotlib import pyplot as plt
import numpy as np
class mel_auto:
    def __init__(self,testList, trainList): #class is defined by test and train list
        self.testList = testList
        self.trainList = trainList
    def convert_audio_to_mel_spectogram(self, filename, trainTestPath): #takes wav, outputs spec to path specified by trainTestPath
        extLen = len(filename)-3
        getPathLen = len('/home/ubuntu/test_data/')
        png_name = filename[getPathLen:extLen]+'png'
        y, sr = librosa.load(filename, sr=44100)
        s = librosa.feature.melspectrogram(y=y,sr=sr,n_mels=128,fmax=8000)
        fig,ax = plt.subplots()

        S_dB = librosa.power_to_db(s, ref = np.max)
        img = librosa.display.specshow(S_dB,  sr=sr,
                             fmax=8000, ax=ax)
        plt.savefig(trainTestPath+png_name)
        
    def partitionSets(self): #partitions data into train and test split
        curr_dir = os.path.join('/home/ubuntu/test_data/')

        for filename in os.listdir(curr_dir):
            self.trainList.append(curr_dir+filename)
        self.testList = random.sample(self.trainList,20) #randomly chosen test data

        for x in self.testList:
            self.trainList.remove(x)
        
    def runSpec(self): #point of execution
        trainPath = '/home/ubuntu/spec_TRAIN/'
        testPath = '/home/ubuntu/spec_TEST/'
        for x in self.trainList:
            self.convert_audio_to_mel_spectogram(x,trainPath)
            print('done '+x)
        for y in self.testList:
            self.convert_audio_to_mel_spectogram(y,testPath)
            print('done '+y)
    
    
    
if __name__ == "__main__":
    test = []
    train = []
    specAuto = mel_auto(test,train)
    specAuto.partitionSets()
    specAuto.runSpec()
    
