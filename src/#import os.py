#import os
#if __name__ == '__main__':
 #   print("Welcome ")
  #  while True:
   #     x = input("What do you want Sovi  ")
        #if x == "quit":
          #  os.system("Bye Bye Sovi")
         #   break
      #  command = f"say {x}"
       # os.system(command)

import win32com.client as wincom
import time
speak = wincom.Dispatch("SAPI.SpVoice")
while True:
    text = input("What do you want to speak Sovi    ")
    if text == "quit":
        speak.Speak("Bye Bye Sovi")
        break
    speak.Speak(text)

# 3 second sleep
#time.sleep(3)

#text = "This text is read after 3 seconds"
#speak.Speak(text)