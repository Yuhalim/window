from tkinter import *
import json
p=Tk()
def ent():
    b=a.get()
    data = json.load(open('data.json'))

    def translate(b):
        try:
            b = b.lower()
            Label(text=data[b]).grid(row=4,column=1)
        except:
            Label(text='word cant be found').grid(row=4)

    print(translate(b))


p.title('DICTIONARY')
p.geometry('500x400')
a=StringVar()
Label(text='WELCOME TO THE DICTIONARY', bg='red', font=20).grid(row=0,column=1)
Label(text='which word would you like to search', font=('roman', 10, 'italic')).grid(row=1,column=1)
Entry(text=a).grid(row=2)
Button(text='SEARCH', command=ent).grid(row=3)

p.mainloop()