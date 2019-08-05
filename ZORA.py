import pyttsx3 as pt
import datetime as dt
import speech_recognition as sr
import wikipedia as wp
import webbrowser as wb
import os
import random
engine=pt.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices',voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()


def wishme():
	hour=int(dt.datetime .now().hour)
	if hour>=0 and hour<=12:
		speak("good morning")
	elif hour>12 and hour<18:
		speak("good afternoon")
	else:
		speak("good evening")	
	speak('i am zora ,How can i help u')		


def takecommand():
	r=sr.Recognizer()
	with sr.Microphone() as source:
		speak("i am here to take orders")
		print("listening....")
		r.pause_thresold=5
		audio=r.listen(source)

	try :
		
		print("recognizing...")	
		query=r.recognize_google(audio,language='en-in')
		print(f"you said:{query}\n")

	except Exception as e:
		print(e)
		print("say that again please...")
		return "None"

	return query	

def actions() :
	
	while(True): 
		query=takecommand().lower()
		if 'wikipedia' in query:
			speak('searching wikipedia....')
			query=query.replace("wikipedia"," ")
			results=wp.summary(query,sentences=2)
			speak('according to wikipedia....')
			speak(results)
			print(results)
		elif 'open youtube' in query:
			wb.open("youtube.com")
		
		elif 'open google'	in query:
			wb.open("google.com")
		elif 'the time' in query:
			strtime=dt.datetime.now().strftime("%H:%M:%S")
			speak(f"sir,the time is {strtime}")
		elif 'play music' in query: 
			music_dir='F:\\videos\\New folder\\Muzika\\audios\\SHAREit'
			song=os.listdir(music_dir)
			os.startfile(os.path.join(music_dir,song[random.randint(0,(len(song)-1))]))
	
		elif 'kiss' in query :
			kiss_dir='C:\\Users\\Rutik\\Desktop\\MY PROJECT\\KISS SOUNDS'	
			kiss=os.listdir(kiss_dir)
			os.startfile(os.path.join(kiss_dir,kiss[random.randint(0,(len(kiss)-1))]))
		elif 'bye-bye' in query :
			speak('bye-bye...see u again...have a great day!')
			break
		else: 
			continue		
	

if __name__=="__main__":
	
	wishme()
	actions()
	

	
