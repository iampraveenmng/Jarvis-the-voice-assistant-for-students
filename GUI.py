from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import webbrowser
import requests
import json





def changeOnHover(button, colorOnHover, colorOnLeave):
  
    # adjusting backgroung of the widget
    # background on entering widget
    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))
  
    # background color on leving widget
    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))
    
    


  

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
        
        label=Label(root,text="JARVIS - THE VOICE ASSISTANT FOR STUDENTS",font=("Times New Roman",18),bg="#090e38", fg="white")
        label.place(relx=0.19,rely=0,relheight=0.15,relwidth=0.8)
        #imgg=anim.ImageLabel( ImageTk.PhotoImage(anim.ImageLabel.load('lena.jpg')))
        frame=Frame(root)
        frame.place(relx=0,rely=0.12,relheight=0.7,relwidth=0.6)
        imgg = ImageTk.PhotoImage(Image.open('e.jpg'))
        panel = Label(frame, image=imgg)
        panel.pack()
        
        frame=Frame(root,bg="#090e38")
        frame.place(relx=0,rely=0.62,relheight=0.4,relwidth=0.6)
        #img = ImageTk.PhotoImage(Image.open('e.jpg'))
        button=Button(frame,text="Speak",bg="white",fg="black",font=("Times New Roman",15),command=lambda:self.clicked())
        button.place(relx=0.2,rely=0.1,relheight=0.15,relwidth=0.2)
        changeOnHover(button, "red", "white")
        
        button=Button(frame,text="Close",bg="white",fg="black",font=("Times New Roman",15),command=lambda:self.clickedd())
        button.place(relx=0.5,rely=0.1,relheight=0.15,relwidth=0.2)
        changeOnHover(button, "red", "white")
        
        frame1=Frame(root,bg="white")
        frame1.place(relx=0.59,rely=0.2,relheight=0.4,relwidth=0.4)
        
        frame1=Frame(root,bg="white")
        frame1.place(relx=0,rely=0.75,relheight=0,relwidth=1)
        
        #frame1=Frame(root,bg="white")
        #frame1.place(relx=0,rely=0.98,relheight=0,relwidth=1)
        
        frame1=Frame(root,bg="#090e38")
        frame1.place(relx=0,rely=0.77,relheight=0.2,relwidth=0.98)
        button=Button(frame1,text="COLLEGE PORTAL",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.01,rely=0.1,relheight=0.3,relwidth=0.18)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="NEWTON",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.2,rely=0.1,relheight=0.3,relwidth=0.09)
        changeOnHover(button, "red", "white")
        
        
        button=Button(frame1,text="EPASS",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.3,rely=0.1,relheight=0.3,relwidth=0.1)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="NSP",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.41,rely=0.1,relheight=0.3,relwidth=0.1)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="STACKOVERFLOW",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.52,rely=0.1,relheight=0.3,relwidth=0.17)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="GITHUB",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.7,rely=0.1,relheight=0.3,relwidth=0.09)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="PYTHON COMPILER",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.8,rely=0.1,relheight=0.3,relwidth=0.2)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="LINKEDIN",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.01,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="SPOTIFY",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.14,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="SHUTDOWN",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.27,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        button=Button(frame1,text="WHATSAPP",bg="white",fg="black",font=("Times New Roman",13))
        button.place(relx=0.4,rely=0.54,relheight=0.3,relwidth=0.12)
        changeOnHover(button, "red", "white")
        
        
        
        
        
       #button=Button(frame,text="Close",bg="white",fg="black",font=("Times New Roman",15))
        #button.place(relx=0,rely=0.7,relheight=0.1,relwidth=0.1)
        #changeOnHover(button, "red", "white")
        
        #button=Button(frame,text="Speak",bg="white",fg="black",font=("Times New Roman",15),command=lambda:self.clicked())
        #button.place(relx=0.2,rely=0.1,relheight=0.15,relwidth=0.2)
        #changeOnHover(button, "red", "white")
        #lee_voice('How can i help you Group13?')
        
        root.iconbitmap('assistant2.ico')
        root.mainloop() 
        
        
    def clicked(self):
        frame1=Frame(bg="white")
        frame1.place(relx=0.59,rely=0.2,relheight=0.4,relwidth=0.4)
        label = Label(text= "Hey whatsup bro, i am doing something very interresting.")
        label = Label(text= "Hey whatsup bro, i am doing something very interrestingF.")
    #this creates a new label to the GUI
        label.place(relx=0.59,rely=0.2,relheight=0.4,relwidth=0.4)
    
        print("working")
        webbrowser.open_new_tab("https://google.co.in")
        
    def clickedd(self):
        frame1=Frame(bg="white")
        frame1.place(relx=0.59,rely=0.2,relheight=0.4,relwidth=0.4)
        label = Label(text= "Hey whatsup bro, i am doing something very interresting.")
        label = Label(text= "Hey.")
    #this creates a new label to the GUI
        label.place(relx=0.59,rely=0.2,relheight=0.4,relwidth=0.4)
    
        print("working")
        webbrowser.open_new_tab("https://google.co.in")
        
w=Widget()