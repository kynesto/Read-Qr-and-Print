
from tkinter import *
import datetime
from genPrintImg import ImageGen
from toolData import Tool

tool = Tool()
window = Tk()
window.title("Label Druck")
window.geometry('350x200')

# Set default Values, to be replaced with scanned params
Customer = "Kunde"
MaterialNr= "Material"
DrawingNr = "Zeichnung"
dateTimeInstance = datetime.datetime.now()
Kw = dateTimeInstance.isocalendar()[1]
Year = dateTimeInstance.isocalendar()[0]
KwDate = F"{Kw}/{Year}"
FA = "beispielFA"

# values are allocated in Gui
description = Label(window, text=Customer)
description.grid(column=1, row=0)
mat = Label(window, text=MaterialNr)
mat.grid(column=1, row=1)
drw = Label(window, text=DrawingNr)
drw.grid(column=1, row=2)
kwyear = Label(window, text=KwDate)
kwyear.grid(column=1, row=3)
fa = Label(window, text=FA)
fa.grid(column=1, row=4)
#var to set default spinbox to 1 
var =IntVar()
var.set(1)
NrOfTools = Spinbox(window, from_=0, to=500, width=5, textvariable=var)
NrOfTools.grid(column=1,row=5)

# Gui labels
Kunde = Label(window, text="Kunde:")
Kunde.grid(column=0, row=0)
MatNr = Label(window, text="Mat.-no.:")
MatNr.grid(column=0, row=1)
DrwNr = Label(window, text="Drw.-no.:")
DrwNr.grid(column=0, row=2)
KW = Label(window, text="KW:")
KW.grid(column=0, row=3)
FA = Label(window, text="FA:")
FA.grid(column=0, row=4)
ToolNr = Label(window, text="Stückzahl:")
ToolNr.grid(column=0, row=5)

# config for enter triggering
e = Entry(window, width=5)
e.grid(column=0, row=6)
e.focus_set()

def enter(event=None): 
  tool.put(e.get().split("$"))
  e.delete(0, END)

  # update Gui
  description.configure(text=tool.Customer)
  mat.configure(text=tool.MaterialNr)
  drw.configure(text=tool.DrawingNr)
  kwyear.configure(text=tool.KwDate)
  fa.configure(text=tool.FA)

def startPrint():
  # do printing and image generation here
  Image.blank() # clear or generate
  Image.WriteTo((5,130), tool.Customer)
  Image.WriteTo((5,150), "Mat.-no.:  "+tool.MaterialNr)
  Image.WriteTo((5,170), "Drw.-no.:  "+tool.DrawingNr)
  # input qr code
  Image.WriteTo((200,190), "MADE IN GERMANY")
  Image.WriteTo((200,210), tool.KwDate+"   "+tool.FA)
  Image.img.show()

  for i in range(int(NrOfTools.get())):
    print(i)

# print button
btn = Button(window, text="Print", command=startPrint) 
btn.grid(column=1, row=6)
window.bind('<Return>',enter)

Image = ImageGen()

while True:
    window.update_idletasks()
    window.update()
