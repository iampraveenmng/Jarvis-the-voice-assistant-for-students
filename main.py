import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import wolframalpha
import json
import requests
from covid_india import states
from gtts import gTTS
import random
import playsound
import loadgui
import gifgui
import datetime
import ecapture
import pyjokes
import pywhatkit as py
import pyautogui
from time import sleep

#print('Loading your AI personal assistant - Jarvis')

#listener = sr.Recognizer()
#engine=pyttsx3.init('sapi5')
#voices=engine.getProperty('voices')
#engine.setProperty('voice','voices[1].id')
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))

def Jarvis(text):
    engine.say(text)
    engine.runAndWait()
    print(text)

"""def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        Jarvis("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour>=12 and hour<18:
        Jarvis("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        Jarvis("Hello,Good Evening")
        print("Hello,Good Evening")"""

def takecommand():
    r=sr.Recognizer()
    r.dynamic_energy_threshold = False
    #r.energy_threshold = 3000
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening... How can I Help you today!!!!")
        audio=r.listen(source)
        statement=''

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"User said:{statement}\n")

        except Exception as e:
            Jarvis("Pardon me, please say that again")
            return "None"
        return statement
    
def isContain(txt, lst):
	for word in lst:
		if word in txt:
			return True
	return False

"""def Jarvis(audio_string):
    #Play audio text to voice
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)"""
    

#Jarvis("Loading your AI personal assistant Jarvis")
#wishMe()

class Widget: #GUI OF VIRTUAL ASSISTAND AND COMMANDS

    def __init__(self):
        
        root = Tk()
        root.title('J.A.R.V.I.S')
        root.geometry('920x620')
        root.configure(background='#090e38')
        
     
        #root.colspan="3"
        frame=Frame(root,bg="#090e38")
        frame.place(relx=0,rely=0,relheight=0.1,relwidth=0.1)
        img = ImageTk.PhotoImage(Image.open('assistant2.png'))
        panel = Label(root,bg="#090e38",image=img)
        panel.place(relx=0.1,rely=0,relheight=0.15,relwidth=0.1)
        
        label=Label(root,text="JARVIS - THE VOICE ASSISTANT FOR STUDENTS",
                    font=("Times New Roman",16),bg="#090e38", fg="white")
        label.place(relx=0.19,rely=0,relheight=0.15,relwidth=0.7)
        #imgg=anim.ImageLabel( ImageTk.PhotoImage(anim.ImageLabel.load('lena.jpg')))
        frame=Frame(root)
        frame.place(relx=0,rely=0.12,relheight=0.7,relwidth=0.6)
        imgg = ImageTk.PhotoImage(Image.open('e.jpg'))
        panel = Label(frame, image=imgg)
        panel.pack()
        
        frame=Frame(root,bg="#090e38")
        frame.place(relx=0,rely=0.62,relheight=0.4,relwidth=0.6)
        #img = ImageTk.PhotoImage(Image.open('e.jpg'))
        #Jarvis command
        button=Button(frame,text="Jarvis",bg="white",fg="black",font=("Times New Roman",15),
                      command=lambda:self.clicked())
        button.place(relx=0.2,rely=0.1,relheight=0.15,relwidth=0.2)
        changeOnHover(button, "red", "white")
        
        button=Button(frame,text="Close",bg="white",fg="black",font=("Times New Roman",15),
                      command=root.destroy)
        button.place(relx=0.5,rely=0.1,relheight=0.15,relwidth=0.2)
        changeOnHover(button, "red", "white")
        
        frame1=Frame(root,bg="#19232d")
        frame1.place(relx=0.59,rely=0.2,relheight=0.4,relwidth=0.4)
        
        frame1=Frame(root,bg="white")
        frame1.place(relx=0,rely=0.75,relheight=0,relwidth=1)
        
        #frame1=Frame(root,bg="white")
        #frame1.place(relx=0,rely=0.98,relheight=0,relwidth=1)
        
        frame1=Frame(root,bg="#090e38")
        frame1.place(relx=0,rely=0.77,relheight=0.2,relwidth=0.98)
        button=Button(frame1,text="COLLEGE PORTAL",bg="white",fg="black",
                      command=lambda:self.college(),font=("Times New Roman",11))
        button.place(relx=0.01,rely=0.1,relheight=0.3,relwidth=0.18)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="NEWTON",bg="white",fg="black",
                      command=lambda:self.newton(),font=("Times New Roman",11))
        button.place(relx=0.2,rely=0.1,relheight=0.3,relwidth=0.09)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="EPASS",bg="white",fg="black",
                      command=lambda:self.epass(),font=("Times New Roman",11))
        button.place(relx=0.3,rely=0.1,relheight=0.3,relwidth=0.1)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="NSP",bg="white",fg="black",
                      command=lambda:self.nsp(),font=("Times New Roman",11))
        button.place(relx=0.41,rely=0.1,relheight=0.3,relwidth=0.1)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="STACKOVERFLOW",bg="white",fg="black",
                      command=lambda:self.stack(),font=("Times New Roman",10))
        button.place(relx=0.52,rely=0.1,relheight=0.3,relwidth=0.17)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="GITHUB",bg="white",fg="black",
                      command=lambda:self.git(),font=("Times New Roman",11))
        button.place(relx=0.7,rely=0.1,relheight=0.3,relwidth=0.09)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="PYTHON COMPILER",bg="white",fg="black",
                      command=lambda:self.comp(),font=("Times New Roman",11))
        button.place(relx=0.8,rely=0.1,relheight=0.3,relwidth=0.2)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="LINKEDIN",bg="white",fg="black",
                      command=lambda:self.link(),font=("Times New Roman",11))
        button.place(relx=0.01,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="SPOTIFY",bg="white",fg="black",
                      command=lambda:self.spot(),font=("Times New Roman",11))
        button.place(relx=0.14,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="SHUTDOWN",bg="white",fg="black",
                      command=lambda:self.shut(),font=("Times New Roman",11))
        button.place(relx=0.27,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="WHATSAPP",bg="white",fg="black",
                      command=lambda:self.what(),font=("Times New Roman",11))
        button.place(relx=0.4,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="EDYST",bg="white",fg="black",
                      command=lambda:self.edyst(),font=("Times New Roman",11))
        button.place(relx=0.53,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="TALENTINO",bg="white",fg="black",
                      command=lambda:self.tal(),font=("Times New Roman",11))
        button.place(relx=0.66,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="INDIABIX",bg="white",fg="black",
                      command=lambda:self.bix(),font=("Times New Roman",11))
        button.place(relx=0.79,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="????",bg="white",fg="black",
                      command=lambda:self.bix(),font=("Times New Roman",11))
        button.place(relx=0.92,rely=0.54,relheight=0.3,relwidth=0.1)
        changeOnHover(button, "red", "white")
        
        
        
        
       #button=Button(frame,text="Close",bg="white",fg="black",font=("Times New Roman",15))
        #button.place(relx=0,rely=0.7,relheight=0.1,relwidth=0.1)
        #changeOnHover(button, "red", "white")
        
        #button=Button(frame,text="Jarvis",bg="white",fg="black",font=("Times New Roman",15),command=lambda:self.clicked())
        #button.place(relx=0.2,rely=0.1,relheight=0.15,relwidth=0.2)
        #changeOnHover(button, "red", "white")
        #Jarvis('How can i help you Group13?')
        #Jarvis('How can i help you group 13?')
        root.iconbitmap('assistant2.ico')
        root.mainloop() 
        
        
    def clicked(self):
    #BUTTON CALLING
        print("working...")
        statement = takecommand()
        statement = statement.lower()
    
        if 'play' in statement:
            
            song = statement.replace('play', '')
            Jarvis('playing ' + song)
            py.playonyt(song)
            
            frame1=Frame(bg="#19232d")
            frame1.place(relx=0.59,rely=0.2,relheight=0.4,relwidth=0.3)
            label = Label(text="Playing the requested song!!\n Enjoy!!!",
                          font=("Times New Roman",15,"bold"),bg="#19232d",fg="white")
            #label = Label(text= "Hey whatsup bro, i am doing something very interrestingF.")
        #this creates a new label to the GUI
            label.place(relx=0.59,rely=0.2,relheight=0.4,relwidth=0.4)
            #mport antigravity
            
        if "take" in statement or "screenshot" in statement:
            
            pyautogui.screenshot("1223.png")
 
        if "whatsapp" in statement or "send a whatsapp message" in statement:
            
            #py.sendwhatmsg(f"+91{7993472079}","This is a test",16,22)
            py.sendwhatmsg_to_group(f"Kf6myU6XrEWBSe2lwQfu3i", "This is a auto generated message",18,12)
            
        if "search" in statement:
            s=statement.replace("search","")
            py.search(s,3)
            
            
        if "convert image" in statement:
            py.image_to_ascii_art(r"q.jpg")
            
            
        if "information" in statement:
            s=statement.replace("search","")
            py.info(s,3)
            
        if "hand" in statement or "text to hand" in statement:
            
            py.text_to_handwriting("hello there")
            
            
            
        if "classroom" in statement or "attend" in statement:
            
            hour=datetime.datetime.now().hour
            if hour>=9 and hour<=9.19:
                webbrowser.open_new_tab("https://griet.newtonclassroom.com/")
                sleep(10)
                pyautogui.click(1303,752)
                pyautogui.click(1158,881)
        
            
        if 'who are you' in statement:
            Jarvis('My name is Lena and I was Programmed by batch No 13,Praveen,sanjay,amrez,satish')
        
        
        elif 'wikipedia' in statement or "who is" in statement:
            Jarvis('Searching Wikipedia...')
            statement = statement.replace("wikipedia", "")
            results = wikipedia.summary(statement, sentences = 3)
            Jarvis("According to Wikipedia")
            print(results)
            Jarvis(results)
            
        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            Jarvis("Google chrome is open now")
            
            
        elif "calculate" in statement:
            
             
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Client(app_id)
            indx = statement.lower().split().index('calculate')
            statement = statement.split()[indx + 1:]
            res = client.query(' '.join(statement))
            answer = next(res.results).text
            print("The answer is " + answer)
            Jarvis("The answer is " + answer)
            
            
       
            
        elif 'joke' in statement:
            Jarvis(pyjokes.get_joke())
             
        elif 'time' in statement:
            
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            Jarvis(f"the time is {strTime}")
            
        elif 'how are you' in statement:
            
            Jarvis("I am fine, Thank you")
            Jarvis("How are you, Sir")
         
        elif 'fine' in statement or "good" in statement:
            
            Jarvis("It's good to know that your fine")
                
            
       
            
        
            
        
        elif 'spotify' in statement:
           os.system("spotify")
           
           
        elif 'notepad' in statement:
           os.system("notepad")
            
           
        elif 'play music' in statement or "play song" in statement:
              Jarvis("Here you go with music")
              # music_dir = "G:\\Song"
              music_dir = "C:\\Users\\91703\\Music"
              songs = os.listdir(music_dir)
              print(songs)   
              random = os.startfile(os.path.join(music_dir, songs[1]))
        
            
        elif 'college website' in statement or 'open gokaraju website' in statement or 'open college' in statement:
            webbrowser.open_new_tab("http://www.griet.ac.in/")
            print("Opening College Portal")
            Jarvis("opening college website")
            Jarvis("College Portal is open now")
            print("Griet portal is open now")
        
    def college(self):
        webbrowser.open_new_tab("http://www.griet.ac.in/")
        
    def newton(self):
       webbrowser.open_new_tab("https://griet.newtonclassroom.com/")
       
    def epass(self):
       webbrowser.open_new_tab("https://telanganaepass.cgg.gov.in/")
       
    def nsp(self):
       webbrowser.open_new_tab("https://scholarships.gov.in/")
       
       
    def stack(self):
       webbrowser.open_new_tab("https://stackoverflow.com/")
       
    def git(self):
       webbrowser.open_new_tab("https://github.com/")
       
    def comp(self):
       webbrowser.open_new_tab("https://www.programiz.com/python-programming/online-compiler/")
       
    def link(self):
       webbrowser.open_new_tab("https://www.linkedin.com/")
    
    def spot(self):
       webbrowser.open_new_tab("https://www.spotify.com/")
       
    def shut(self):
       webbrowser.open_new_tab("http://www.griet.ac.in/")
       
    def what(self):
       webbrowser.open_new_tab("https://web.whatsapp.com/")
       
    def edyst(self):
       webbrowser.open_new_tab("https://edyst.com/")
     
    def tal(self):
       webbrowser.open_new_tab("https://talentio.io/")
       
    def bix(self):
       webbrowser.open_new_tab("https://www.indiabix.com/")
       
       
       
        
        

if __name__== '__main__':
    widget = Widget()
time.sleep(1)
while 1:
    statement = takecommand()
    respond(statement)

speaker.runAndWait()





