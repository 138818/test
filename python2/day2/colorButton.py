import tkinter
from functools import partial

win = tkinter.Tk()
lb1 = tkinter.Label(win, text='my test windows could', font='Arial 16 red')
# button1 = tkinter.Button(win, fg='white', bg='blue', text='quit', command=win.quit)
myButton = partial(tkinter.Button(win, fg='white', bg='blue'))
button1 = myButton(text='one')
button2 = myButton(text='two')
buttonquit = myButton(text='quit', command=win.quit)
button1.pack()
win.mainloop()

