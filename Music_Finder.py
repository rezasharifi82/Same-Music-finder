#In The Name Of God
from collections import deque
import os
from mutagen.mp3 import MP3
import pandas as pd
class filert:
    all_files=[]
    def __init__(self,path) -> None:
        self.path=path
        self.file=MP3(path)
        self.length=self.file.info.length
        self.size=os.stat(path).st_size
        sep=os.path.pathsep
        sep=str(sep)
        self.name=str(path).split(sep)[-1]

        # self.name=
    def __eq__(self, __o) -> bool:
        if(self.length == __o.length or self.size == __o.size):
            return True
        else: return False
    def __str__(self) -> str:
        return str(self.name)
    def __int__(self) ->int:
        return int(self.length)
def make_list(that_object:tuple):
    base_path=that_object[0]
    for i in that_object[-1]:
        path=os.path.join(base_path,i)
        if(path.endswith(".mp3")):
            try:
                b=filert(path)
                # if("Felitsa" in path):
                filert.all_files.append(b)
            except:
                pass
                # print(path)
            # print(b)

a=os.walk(".\Music")
for i in a:
    # print(i[0])
    make_list(i)
print("We've "+str(len(filert.all_files)))

print("**********************")
c=0
UP="\033c"
CLEAR = '\x1b[2K'
ins=0
inj=1%len(filert.all_files)
while(ins < len(filert.all_files)):
    alpha=10000000
    inj=ins+1
    while(inj<len(filert.all_files)):
        i:filert
        j:filert
        i=filert.all_files[ins]
        j=filert.all_files[inj]
        
        if(i==j):
            c+=1
            print("\n\nIter: {}".format(c))
            print("----------")
            print("Option 1: \n Name: {} \n Size: {} \n Length: {} \n Path: {} ".format(i.name,i.size,i.length,i.path))
            print("---------")
            print("Option 2: \n Name: {} \n Size: {} \n Length: {} \n Path: {} ".format(j.name,j.size,j.length,j.path))
            print("-----------")
            w=int(input("\nWhich one to delete?"))
            if(w==1):
                os.remove(i.path)
                filert.all_files.pop(ins)
                # alpha=min(alpha,ins)
                inj=ins+1
                # break

                # alpha=1
            elif(w==2):
                os.remove(j.path)
                filert.all_files.pop(inj)
                # ins-=1
            elif(w==3):
                ins+=1
                inj=ins+1
            # print("",end="\r")
            os.system('cls')
        else:
            inj+=1
    ins+=1
    # print(ins)
    # if(alpha==1):
    #     alpha=0
    #     continue
print("*****************")
print("\n We had {} same file!".format(c))
