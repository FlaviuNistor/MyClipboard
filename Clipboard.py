import tkinter
from subprocess import check_call

top = tkinter.Tk()
top.title('Copy to clipboard')

canvas1 = tkinter.Canvas(top, width = 300, height = 300)
canvas1.pack()

def IDCallBack():
   global label
   label.configure(text='ID was copied to clipboard')
   B1.configure(background='green')
   B2.configure(background='gray')
   B3.configure(background='gray')
   cmd='echo '+"90127067"+'|clip'
   return check_call(cmd, shell=True)

def MailCallBack():
   global label
   label.configure(text='MAIL was copied to clipboard')
   B1.configure(background='gray')
   B2.configure(background='green')
   B3.configure(background='gray')
   cmd='echo '+"flaviu.nistor@continental-corporation.com"+'|clip'
   return check_call(cmd, shell=True)

def GMailCallBack():
   global label
   label.configure(text='GMAIL was copied to clipboard')
   B1.configure(background='gray')
   B2.configure(background='gray')
   B3.configure(background='green')
   cmd='echo '+"flaviu.nistor@gmail.com"+'|clip'
   return check_call(cmd, shell=True)
   

B1 = tkinter.Button(top, text ="ID", background='gray', height = 1, width = 5, command = IDCallBack)
B2 = tkinter.Button(top, text ="MAIL", background='gray', height = 1, width = 5, command = MailCallBack)
B3 = tkinter.Button(top, text ="GMAIL", background='gray', height = 1, width = 5, command = GMailCallBack)

B1.pack()
canvas1.create_window(150, 80, window=B1)
B2.pack()
canvas1.create_window(150, 120, window=B2)
B3.pack()
canvas1.create_window(150, 160, window=B3)

label = tkinter.Label(top, text= '', fg='green', font=('helvetica', 12, 'bold'))
taglabel = canvas1.create_window(150, 220, window=label)

top.mainloop()
