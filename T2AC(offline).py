import pyttsx3
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import Font
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 130)


def preview():
    ui = text_box.get(0.0, END)
    engine.say(ui)
    engine.runAndWait()
    engine.stop()


def save():
        msg = messagebox.askquestion('Save', 'Do you want to save this file?')
        if msg == 'yes':
            ui = text_box.get(0.0, END)
            way2alert = [('MP3 FILE', '*.mp3')]
            saver = filedialog.asksaveasfilename(title='Select your destination', filetypes=way2alert,
                                                 defaultextension=way2alert)
            engine.save_to_file(ui, saver)
            engine.runAndWait()


def male_voice():
    try:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
    except EXCEPTION:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)


def female_voice():
    try:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
    except EXCEPTION:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)


root = Tk()
root.title('Text 2 Audio Converter')
root.config(bg='yellow')

canvas = Canvas(root, width=1280, height=720,
                bd=-2.9, bg='#feed01')
image = ImageTk.PhotoImage(Image.open('./res/IMG-20201115-WA0003.jpg'))
canvas.create_image(1, 1, anchor=NW, image=image)
canvas.pack()

logo = PhotoImage(file='./res/logoo.png')
logo_main = Label(root, image=logo, bg='black')
logo_main.pack(pady=10)

text_box_type = Font(family='arial', size=11, weight='bold')
text_box = Text(root, width=64, height=17,
                fg='#002750', font=text_box_type, bg='#fff842',
                selectbackground='light blue', selectforeground='black',)

text_box.place(x=197, y=254)

preview_btn = Button(root, text='Preview', command=preview,
                     height=1, width=10, bg='#002750',
                     fg='#ffca00', activebackground='red', activeforeground='#ffca00')
save_btn = Button(root, text='Save', command=save,
                  height=1, width=10, bg='#002750',
                  fg='#ffca00', activebackground='red', activeforeground='#ffca00')
clear_btn = Button(root, text='Clear', command=lambda: text_box.delete(0.0, END),
                   height=1, width=10, bg='#002750',
                   fg='#ffca00', activebackground='red', activeforeground='#ffca00')
exit_btn = Button(root, text='Exit', command=lambda: sys.exit(),
                  height=1, width=10, bg='#002750',
                  fg='#ffca00', activebackground='red', activeforeground='#ffca00')

preview_btn.place(x=800, y=420)
save_btn.place(x=900, y=420)
clear_btn.place(x=1000, y=420)
exit_btn.place(x=1100, y=420)

var1 = IntVar()
rb1 = Radiobutton(root, text='Male voice', variable=var1,
                  value=1, command=male_voice, bg='#feed01')
rb1.place(x=900, y=300)

rb2 = Radiobutton(root, text='Female voice', variable=var1,
                  value=2, command=female_voice, bg='#feed01')
rb2.place(x=900, y=350)


root.mainloop()