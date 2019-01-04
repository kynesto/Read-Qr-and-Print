
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
  # testString = "$FA0133999$5042850180$AB080228/2$PS 49119204 - F58$RC_0019U001$_3$E1200042$200$3$330$8,3$6702.383.332$BOSCH NUERNBERG$39812$5"
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
  versatzy = 240
  versatzx = 24
  linesize = 50
  Image.blank() # clear or generate
  Image.WriteTo((versatzx,versatzy-7), tool.Customer)
  Image.WriteTo((versatzx,versatzy+linesize), "Mat:")
  Image.WriteTo((versatzx+100,versatzy+linesize), tool.MaterialNr)
  Image.WriteTo((versatzx,versatzy+2*linesize), "Drw:")
  Image.WriteTo((versatzx+100,versatzy+2*linesize), tool.DrawingNr)
  Image.WriteTo((versatzx,versatzy+3*linesize+7), "MADE IN GERMANY")
  if int(tool.Kw) <10:
    Image.WriteTo((versatzx,versatzy+4*linesize), "CW:0"+tool.KwDate+"  "+tool.FA)
  else:
    Image.WriteTo((versatzx,versatzy+4*linesize), "CW:"+tool.KwDate+"   "+tool.FA)

  # generate and add datamatrix
  matrix = Matrix()
  matrix.create("$"+str(tool.Kw)+"$"+tool.FA+"$"+tool.MaterialNr+"$"+tool.DrawingNr)
  matrix.merge(Image.get(),180)
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
