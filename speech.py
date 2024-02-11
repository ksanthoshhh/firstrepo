import pyttsx3
from time import sleep
b=open("C:/Users/santh/OneDrive/Documents/demo.txt","r")
book=b.readlines()
engine=pyttsx3.init()
for i in book:
    engine.say(i)
    engine.runAndWait()
    sleep(1)
b.close()
