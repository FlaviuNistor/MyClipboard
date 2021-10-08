import tkinter
import pyperclip
from subprocess import check_call

top = tkinter.Tk()
top.title('Copy to clipboard')
top.geometry('400x400')

canvas1 = tkinter.Canvas(top, width = 300, height = 300)
canvas1.pack()

var1 = tkinter.IntVar()

def IDCallBack():
   global label
   label.configure(text='ID was copied to clipboard')
   B1.configure(background='green')
   B2.configure(background='gray')
   B3.configure(background='gray')
   pyperclip.copy('90127067')
   #cmd='echo '+"90127067"+'|clip'
   #return check_call(cmd, shell=True)

def MailCallBack():
   global label
   label.configure(text='MAIL was copied to clipboard')
   B1.configure(background='gray')
   B2.configure(background='green')
   B3.configure(background='gray')
   pyperclip.copy('flaviu.nistor@continental-corporation.com')
   #cmd='echo '+"flaviu.nistor@continental-corporation.com"+'|clip'
   #return check_call(cmd, shell=True)

def GMailCallBack():
   global label
   label.configure(text='GMAIL was copied to clipboard')
   B1.configure(background='gray')
   B2.configure(background='gray')
   B3.configure(background='green')
   pyperclip.copy('flaviu.nistor@gmail.com')
   #cmd='echo '+"flaviu.nistor@gmail.com"+'|clip'
   #return check_call(cmd, shell=True)

def Refresh():
   global content
   if ( var1.get() == 1 ):
      content.configure(text=pyperclip.paste())
   else:
      content.configure(text='')

   str = pyperclip.paste()
   if ( str != '90127067'):
      B1.configure(background='gray')
   if (str != 'flaviu.nistor@continental-corporation.com'):
      B2.configure(background='gray')
   if ( str != 'flaviu.nistor@gmail.com'):
      B3.configure(background='gray')
   top.after(500, Refresh)

def Check_sel():
   if (var1.get() == 1):
      content.configure(text=pyperclip.paste())
   else:
      content.configure(text='')

B1 = tkinter.Button(top, text ="ID", background='gray', height = 1, width = 5, command = IDCallBack)
B2 = tkinter.Button(top, text ="MAIL", background='gray', height = 1, width = 5, command = MailCallBack)
B3 = tkinter.Button(top, text ="GMAIL", background='gray', height = 1, width = 5, command = GMailCallBack)

CB = tkinter.Checkbutton(text='See current clipboard', font=('helvetica',10) ,variable=var1, onvalue=1, offvalue=0, command=Check_sel)

B1.pack()
canvas1.create_window(150, 80, window=B1)
B2.pack()
canvas1.create_window(150, 120, window=B2)
B3.pack()
canvas1.create_window(150, 160, window=B3)

label = tkinter.Label(top, text= '', fg='green', font=('helvetica', 12, 'bold'))
taglabel = canvas1.create_window(150, 220, window=label)

CB.pack
canvas1.create_window(150, 280, window=CB)

content = tkinter.Label(top, text= '', fg='black', font=('helvetica', 12, 'bold'))
tagcontent = canvas1.create_window(150, 300, window=content)

top.after(1000, Refresh)
top.mainloop()
