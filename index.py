from gtts import gTTS 
import os
file = open("abc.txt", "r").read()

speech = gTTS(text=file, lang='en', slow=False)
speech.save("voice.mp3")
os.system("vlc -I dummy --no-video voice.mp3")

#print(file)