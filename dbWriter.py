import mysql.connector
import os
import sys
class writeData:
    def __init__(self,curr):
        self.curr = curr

    def writeData(self):
        trainPath = '/home/ubuntu/spec_TRAIN/'
        testPath = '/home/ubuntu/spec_TEST/'
        for filename in os.listdir(testPath): #write for test set
            fName = filename
            if(fName.__contains__('nonaggression')):
                binClass = False
            else:
                binClass = True
            self.curr.execute("INSERT INTO AUDIO_SET (fileName, binClass) VALUES (?, ?)",
                          (fName,binClass))
        for filename in os.listdir(trainPath): #write for trainset
            fName = filename
            if(fName.__contains__('nonaggression')):
                binClass = False
            else:
                binClass = True
            self.curr.execute("INSERT INTO AUDIO_SET (fileName, binClass) VALUES (?, ?)",
                          (fName,binClass))
        
if __name__ == "__main__":
    configFile = open('/home/ubuntu/dbLogin.txt','r')
    configLines = configFile.readlines()
    myUser =str(configLines[0])
    myPass =str(configLines[1])
    myHost =str(configLines[2])
    myPort =int(configLines[3])
    myData =str(configLines[4])
         
    try:
        conn = mysql.connector.connect(
            user=myUser,
            password=myPass,
            host=myHost,
            port=myPort,
            database=myData
        )
    except mysql.connector.Error as e:
        print(f"Error connecting to MariaDB Platform: {e}")
        sys.exit(1)
    curr = conn.cursor()
    myWriter = writeData(curr)
    myWriter.writeData()
    
        

    

