# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
from mydb import DataBase
from tkinter import messagebox
from myapi import API
import json
class Nlpcloud:
    def __init__(self):
        self.dbo=DataBase()
        self.apio= API()

        self.root=Tk()
        self.root.title("NLP Application")
        self.root.geometry('600x600')
        self.root.configure(bg="#6A4A87")
        self.login_gui()
        self.root.mainloop()
    def login_gui(self):
        self.clear()
        heading=Label(self.root,text="Welcome to NLP App",bg="#6A4A87",fg="black")
        heading.pack(pady=("13","13"))
        heading.pack()
        heading.configure(font=("Timesnewroman",15,"bold"))

        label1=Label(self.root,text="Enter Email")
        label1.pack(pady=("5","5"))

        self.email_input=Entry(self.root,width=30)
        self.email_input.pack(pady=("14","14"),ipady=3)

        label2 = Label(self.root, text="Enter Password")
        label2.pack(pady=("14","14"))

        self.password_input = Entry(self.root,width=30,show="*")
        self.password_input.pack(pady=("14","14"),ipady=3)

        log_button=Button(self.root,text="Log in",width=20,height=1,command=self.perform_login)
        log_button.pack(pady=(10,10))

        label1 = Label(self.root, text="Not a member")
        label1.pack(pady=("10", "3"))

        redirect_button = Button(self.root, text="Register Now", width=10, height=1,command=self.register_now)
        redirect_button.pack(pady=(10, 10))
    def register_now(self):
        self.clear()
        heading = Label(self.root, text="Welcome to NLP App", bg="#6A4A87", fg="black")
        heading.pack(pady=("13", "13"))
        heading.pack()

        heading.configure(font=("Timesnewroman", 15, "bold"))

        label0 = Label(self.root, text="Enter your name")
        label0.pack(pady=("5", "5"))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=("14", "14"), ipady=3)

        label1 = Label(self.root, text="Enter Email")
        label1.pack(pady=("5", "5"))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=("14", "14"), ipady=3)

        label2 = Label(self.root, text="Enter Password")
        label2.pack(pady=("14", "14"))

        self.password_input = Entry(self.root, width=30, show="*")
        self.password_input.pack(pady=("14", "14"), ipady=3)

        register_button = Button(self.root, text="Register", width=20, height=1,command=self.perform_registration)
        register_button.pack(pady=(10, 10))

        label1 = Label(self.root, text="Already a member")
        label1.pack(pady=("10", "3"))

        redirect_button = Button(self.root, text="Login now", width=10, height=1, command=self.login_gui,)
        redirect_button.pack(pady=(10, 10))

    def clear(self):
        for i in self.root.pack_slaves():
            (i.destroy())

    def perform_registration(self):
        name=self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response=self.dbo.add_data(name,email,password)

        if response:
            messagebox.showinfo("Success","Registration Successfully.You can login now")
        else:
            messagebox.showerror("Error","Email already exist")

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response=self.dbo.search(email,password)

        if response:
            messagebox.showinfo("Successful", "Login Successful")
            self.home_gui()
        else:
            messagebox.showerror("Error","Email/Password incorrect")

    def home_gui(self):
        self.clear()
        heading = Label(self.root, text="Welcome to NLP App", bg="#6A4A87", fg="black")
        heading.pack(pady=("13", "13"))
        heading.pack()
        heading.configure(font=("Timesnewroman", 15, "bold"))

        sentiment_button = Button(self.root, text="Sentiment Analysis", width=30, height=4, command=self.sentiment_gui)
        sentiment_button.pack(pady=(15, 15))

        ner_button = Button(self.root, text="Named Entity Recognization", width=30, height=4,
                                  command=self.ner_gui)
        ner_button.pack(pady=(15, 15))

        emotion_button = Button(self.root, text="Emotion Prediction", width=30, height=4,
                                  command=self.emotion_prediction)
        emotion_button.pack(pady=(15, 15))

        logout_button = Button(self.root, text="Logout", width=10, height=1, command=self.login_gui, )
        logout_button.pack(pady=(30, 10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text="Welcome to NLP App", bg="#6A4A87", fg="black")
        heading.pack(pady=("13", "13"))
        heading.pack()
        heading.configure(font=("Timesnewroman", 15, "bold"))

        heading2 = Label(self.root, text="Sentiment Analysis", bg="#6A4A87", fg="black")
        heading2.pack(pady=("13", "13"))
        heading2.pack()
        heading2.configure(font=("Timesnewroman", 15,))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(10, 10), ipady=4)

        sentiment_btn = Button(self.root, text='Analyze Sentiment', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='', bg='#6A4A87', fg='black')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('Timesnewroman', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def ner_gui(self):
        self.clear()

        heading = Label(self.root, text="Welcome to NLP App", bg="#6A4A87", fg="black")
        heading.pack(pady=("13", "13"))
        heading.pack()
        heading.configure(font=("Timesnewroman", 15, "bold"))

        heading2 = Label(self.root, text="Named Entity Recognization", bg="#6A4A87", fg="black")
        heading2.pack(pady=("13", "13"))
        heading2.pack()
        heading2.configure(font=("Timesnewroman", 15,))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(10, 10), ipady=4)

        ner_btn = Button(self.root, text='Analyze Named Entity Recognization', command=self.do_ner_analysis)
        ner_btn.pack(pady=(10, 10))

        self.ner_result = Label(self.root, text='', bg='#6A4A87', fg='black')
        self.ner_result.pack(pady=(10, 10))
        self.ner_result.configure(font=('Timesnewroman', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def emotion_prediction(self):
        self.clear()

        heading = Label(self.root, text="Welcome to NLP App", bg="#6A4A87", fg="black")
        heading.pack(pady=("13", "13"))
        heading.pack()
        heading.configure(font=("Timesnewroman", 15, "bold"))

        heading2 = Label(self.root, text="Named Entity Recognization", bg="#6A4A87", fg="black")
        heading2.pack(pady=("13", "13"))
        heading2.pack()
        heading2.configure(font=("Timesnewroman", 15,))

        label1 = Label(self.root, text='Enter the text')
        label1.pack(pady=(10, 10))

        self.emotionpre_input = Entry(self.root, width=50)
        self.emotionpre_input.pack(pady=(10, 10), ipady=4)

        emotion_btn = Button(self.root, text='Predict Emotion', command=self.do_emotion_predict)
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg='#6A4A87', fg='black')
        self.emotion_result.pack(pady=(10, 10))
        self.emotion_result.configure(font=('Timesnewroman', 16))

        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))

    def do_sentiment_analysis(self):
        text=self.sentiment_input.get()
        result=self.apio.sentiment_analysis(text)

        txt = ''
        for i in result['sentiment']:
            txt = txt + i + ' -> ' + str(result['sentiment'][i]) + '\n'

        print(txt)
        self.sentiment_result['text'] = txt

    def do_ner_analysis(self):
        text = self.name_input.get()
        result = self.apio.ner(text)

        txt = ""
        for i in result['entities']:
            txt += i + ' -> ' + str(result['entities'][i]) + '\n'

        print(txt)
        self.ner_result['text'] = txt

    def do_emotion_predict(self):
        text = self.emotionpre_input.get()
        result = self.apio.emotion_prediction(text)
        txt = ""
        for i in result['emotion']:
            txt += i + ' -> ' + str(result['emotion'][i]) + '\n'

        print(txt)
        self.emotion_result['text'] = txt


n=Nlpcloud()
