
from tkinter import *
import datetime
from genPrintImg import ImageGen
from PIL import ImageFilter
from toolData import Tool
from genDatamatrix import Matrix
import os

tool = Tool()
window = Tk()
window.title("Label Druck")
window.geometry('200x180')

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
  # # Testing without scanner
  # testString = "$FA0134253$5154482061$AB080331&3$ST016373 & Schweizer ESO$49186$Drw_1234$M1100037G$3$3$330$4,3$Mat_1234$SCHWEGLER BURSA$49186$"
  # tool.put(testString.split("$"))
  # Normal code with scanner
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
  Image.WriteTo((10,256), tool.Customer, "cour.ttf", 40)
  Image.WriteTo((10,306), "Mat:")
  Image.WriteTo((100,300), tool.MaterialNr, "courbd.ttf",44)
  Image.WriteTo((10,356), "Drw:")
  Image.WriteTo((100,350), tool.DrawingNr, "courbd.ttf",44)
  Image.WriteTo((10,406), "MADE IN GERMANY", "courbd.ttf")
  if int(tool.Kw) <10:
    Image.WriteTo((10,446), "CW:0"+tool.KwDate+"  "+tool.FA, "cour.ttf",32)
  else:
    Image.WriteTo((10,446), "CW:"+tool.KwDate+"   "+tool.FA, "cour.ttf",32)

  # generate and add datamatrix
  matrix = Matrix()
  matrix.create("$"+str(tool.Kw)+"$"+tool.FA+"$"+tool.MaterialNr+"$"+tool.DrawingNr)
  matrix.merge(Image.get(),240)
  # Image.img = Image.img.rotate(180)
  Image.img.save('temp.bmp')

  # # Debug
  # Image.img.show()
  # Image.img.save('sample.jpg')


  for i in range(int(NrOfTools.get())):
    os.system('i_view32.exe temp.bmp /print')

# print button
btn = Button(window, text="Print", command=startPrint) 
btn.grid(column=1, row=6)
window.bind('<Return>',enter)

Image = ImageGen()

while True:
    window.update_idletasks()
    window.update()
