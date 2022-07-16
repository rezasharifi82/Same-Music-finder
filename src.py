#In The Name Of God
import os

from mutagen.mp3 import MP3

basepath = input("Enter Your Folder Path: ")
count=1
result={}
resultset=[]
lenres=os.scandir(basepath)
resultset=0
for entry in lenres:
    if os.path.isfile(os.path.join(basepath, entry)):
        if(entry.name.endswith(".mp3")):
            resultset+=1
            name=(entry.name)
            audio=MP3(entry.path)
            length=(audio.info.length)
            temp={}
            temp[length]=name
            # values=list(result.values())
            
            
            if(length not in result):
                result.update(temp)
            else:
                t1=result.get(length)
                print("Number: %d"%count)
                print("File  1 :    "+t1)
                print("File  2 :     "+ name)
                print("Which both same at: "+str(length))
                
                count+=1
                Address1=os.path.join(basepath,t1)
                Address2=os.path.join(basepath,name)
                
                w=int(input("Now Which one to delete : "))
                if(w==1):
                    os.remove(Address1)
                elif(w==2):
                    os.remove(Address2)
                else:
                    continue
                
                
                
                    
            
                print("___________________________")
            
            
print("At first you had: %d number of musics"%(resultset))
print("Now you have %d number of music"%len(result))
print("Finish!")           
#print(type(resultset))
#print(result)
        