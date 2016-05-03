from tkinter import *
root = Tk()
topframe = Frame(root)
topframe.pack()
bottomframe =Frame(root)
bottomframe.pack(side=BOTTOM)


button1 = Button(topframe, text="I am a button")
button2 = Button(topframe, text="Me too!")
button3 = Button(topframe, text="clickme!~")
button4 = Button(bottomframe, text="Butt")
button5 = Button(bottomframe, text="""           I AM A BIG BUTTON                 """)
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)
button5.pack(side=BOTTOM)
root.mainloop()



root.mainloop()
