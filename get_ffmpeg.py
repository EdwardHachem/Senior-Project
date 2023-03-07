import subprocess
import os
#ffmpeg = '/opt/homebrew/Cellar/ffmpeg/5.1.2_3/bin/ffmpeg' #local location
ffmpeg = '/usr/bin/ffmpeg' #remote location
class ffmpeg_automation:
    def __init__(self,remoteFileList):
        self.remoteFileList = remoteFileList
    
    def buildCommand(self, videoInput): #builds the command string
        inVid = videoInput
        removeExt = len(inVid)-3
        outVid = inVid[:removeExt]+'wav'
        command = ffmpeg+" -i "+inVid+" "+outVid
        return command
    
    def buildList(self): #generates list of files that need to be converted
        curr_dir = os.path.join('/home/ubuntu/test_data/')
        for filename in os.listdir(curr_dir):
            removeExt = len(filename)-3
            if(filename[removeExt:]=='wav'):
                continue
            else:
                self.remoteFileList.append(curr_dir+filename)
        #self.remoteFileList.remove(curr_dir+'.DS_Store')
    
    def runCommand(self): #iteratively run command for all files need to be converted
        self.buildList()
        myList = self.remoteFileList
        for fileName in myList:
            currCommand = self.buildCommand(fileName)
            print(currCommand)
            subprocess.call(currCommand,shell=True)
        print("All files have been converted.")
    
    def clean_old(self):
        curr_dir = os.path.join('/home/ubuntu/test_data/')
        for filename in os.listdir(curr_dir):
            if(filename.endswith('.wav')):
                continue
            else:
                os.remove(os.path.join(curr_dir,filename))
                print(filename+' Deleted')
        
        
if __name__ == "__main__":
    nameList = []
    ffAuto = ffmpeg_automation(nameList)
    ffAuto.runCommand()
    ffAuto.clean_old()
    

