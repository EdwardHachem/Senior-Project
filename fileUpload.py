import os
import paramiko
from scp import SCPClient
class get_files():
    def __init__(self,listOfNames):
        self.listOfNames = listOfNames
    def get_local(listFolders): #temp solution to rename files on local machine
        na_count = 17 #not aggressive file count
        ia_count = 17 #is aggressive file count
        print(len(listFolders))
        for x in listFolders:
            curr_dir = os.path.join('/Users/nickfulton/audio_dataset/',x)
            print(curr_dir)
            for filename in os.listdir(curr_dir):
                if(x=='Aggressive'):
                    ia_count +=1
                    temp ='aggression'+str(ia_count)+'.m4a'
                    print(temp)
                    os.rename('/Users/nickfulton/audio_dataset/'+x+'/'+filename,'/Users/nickfulton/audio_dataset/'+temp)
    def get_fileNames(self):
        curr_dir = os.path.join('/Users/nickfulton/audio_dataset/curr_audio/')
        for filename in os.listdir(curr_dir):
            self.listOfNames.append(filename)
        self.listOfNames.remove('.DS_Store')

    def send_files(self):
        curr_dir = os.path.join('/Users/nickfulton/audio_dataset/curr_audio/')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(hostname='34.227.101.9',username='ubuntu',key_filename='/Users/nickfulton/documents/ec2key.pem')
        
        for x in self.listOfNames:
            localPath = os.path.join(curr_dir+x) #path to local file
            remotePath = os.path.join('/home/ubuntu/test_data/'+x) #path for destination on ec2

            with SCPClient(ssh.get_transport()) as scp:
                scp.put(localPath,remotePath)
            print('done')
        
        ssh.close()



    
        
                    
if __name__ == "__main__":
    #list_folders = ['Aggressive']
    #get_files.get_local(list_folders)
    nameList = []
    gFiles = get_files(nameList)
    gFiles.get_fileNames()
    #gFiles.listOfNames.remove('/Users/nickfulton/audio_dataset/curr_audio.DS_Store')
    gFiles.send_files()
                
