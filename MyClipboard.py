import tkinter
import pyperclip

# used to lunch an command to the OS
from subprocess import check_call
# used to check if file exists
from pathlib import Path

# Expected configuration file information
# File name intended to be used
config_file_name = 'config.txt'
# Path expected. The folder is hiden
path_to_file = f'.temp/{config_file_name}'
# Check if file exists. Return and save: True or False
path = Path(path_to_file)

# Top level window
frame = tkinter.Tk()
frame.title('Copy to clipboard')
frame.geometry('400x400')

canvas1 = tkinter.Canvas(frame, width=300, height=400)
canvas1.pack()

var1 = tkinter.IntVar()
status1: int = 0
status2: int = 0
status3: int = 0

def IDCallBack():
    global label
    label.configure(text='ID was copied to clipboard')
    B1.configure(background='green')
    B2.configure(background='gray')
    B3.configure(background='gray')
    pyperclip.copy('myID')
    # cmd='echo '+"90127067"+'|clip'
    # return check_call(cmd, shell=True)

def MailCallBack():
    global label
    label.configure(text='MAIL was copied to clipboard')
    B1.configure(background='gray')
    B2.configure(background='green')
    B3.configure(background='gray')
    pyperclip.copy('mymail1')
    # cmd='echo '+"flaviu.nistor@continental-corporation.com"+'|clip'
    # return check_call(cmd, shell=True)

def GMailCallBack():
    global label
    label.configure(text='GMAIL was copied to clipboard')
    B1.configure(background='gray')
    B2.configure(background='gray')
    B3.configure(background='green')
    pyperclip.copy('mymail2')
    # cmd='echo '+"flaviu.nistor@gmail.com"+'|clip'
    # return check_call(cmd, shell=True)

def Refresh():
    global content
    if (var1.get() == 1):
        content.configure(text=pyperclip.paste())
    else:
        content.configure(text='')

    str = pyperclip.paste()
    if (str != 'myID'):
        B1.configure(background='gray')
    if (str != 'mymail1'):
        B2.configure(background='gray')
    if (str != 'mymail2'):
        B3.configure(background='gray')
    frame.after(500, Refresh)

def Check_sel():
    if (var1.get() == 1):
        content.configure(text=pyperclip.paste())
    else:
        content.configure(text='')

def Configure_Input_Data():
    # Toplevel object which will be treated as a new window
    configWindow = tkinter.Toplevel(frame)

    # sets the title of the Toplevel widget
    configWindow.title("Configuration Window")

    # sets the geometry of toplevel
    configWindow.geometry("500x200")

    tkinter.Label(configWindow, text="ENTER ID").grid(row=0)
    tkinter.Label(configWindow, text="ENTER MAIL").grid(row=1)
    tkinter.Label(configWindow, text="ENTER GMAIL").grid(row=2)
    inputtxt1 = tkinter.Text(configWindow, height=1, width=45)
    inputtxt2 = tkinter.Text(configWindow, height=1, width=45)
    inputtxt3 = tkinter.Text(configWindow, height=1, width=45)
    inputtxt1.grid(row=0, column=1)
    inputtxt2.grid(row=1, column=1)
    inputtxt3.grid(row=2, column=1)
    tkinter.Button(configWindow, text='Cancel', command=configWindow.destroy).grid(row=5, column=0, sticky=tkinter.W, pady=4)
    tkinter.Button(configWindow, text='Save').grid(row=5, column=1, sticky=tkinter.W, pady=4)


def Check_Input_Data():
    global status1, status2, status3
    print('Checking if input data is present!')
    if path.is_file():
        status1 = 1
        status2 = 1
        status3 = 1
        print(f'File {path_to_file} exists')
    else:
        status1 = 0
        status2 = 0
        status3 = 0
        print(f'File {path_to_file} does not exist')


def Set_Status():
    if (status1 == 0):
        canvas1.itemconfig(S1, fill="red")  # Fill the circle with RED
    else:
        canvas1.itemconfig(S1, fill="green")  # Fill the circle with GREEN

    if (status2 == 0):
        canvas1.itemconfig(S2, fill="red")  # Fill the circle with RED
    else:
        canvas1.itemconfig(S2, fill="green")  # Fill the circle with GREEN
    if (status3 == 0):
        canvas1.itemconfig(S3, fill="red")  # Fill the circle with RED
    else:
        canvas1.itemconfig(S3, fill="green")  # Fill the circle with GREEN


B1 = tkinter.Button(frame, text="ID", background='gray', height=1, width=5, command=IDCallBack)
B2 = tkinter.Button(frame, text="MAIL", background='gray', height=1, width=5, command=MailCallBack)
B3 = tkinter.Button(frame, text="GMAIL", background='gray', height=1, width=5, command=GMailCallBack)

Check_Input_Data()

S1 = canvas1.create_oval(70, 75, 80, 85)
S2 = canvas1.create_oval(70, 110, 80, 120)
S3 = canvas1.create_oval(70, 145, 80, 155)

Set_Status()

Config_button = tkinter.Button(frame, text="CONFIGURE", background='green', height=1, width=10,
                               command=Configure_Input_Data)

CB = tkinter.Checkbutton(text='See current clipboard', font=('helvetica', 10), variable=var1, onvalue=1, offvalue=0,
                         command=Check_sel)

Config_button.pack()
canvas1.create_window(20, 20, window=Config_button)

B1.pack()
canvas1.create_window(150, 80, window=B1)
B2.pack()
canvas1.create_window(150, 120, window=B2)
B3.pack()
canvas1.create_window(150, 160, window=B3)

label = tkinter.Label(frame, text='', fg='green', font=('helvetica', 12, 'bold'))
taglabel = canvas1.create_window(150, 220, window=label)

status_label = tkinter.Label(frame, text='Status', fg='black', font=('helvetica', 12, 'bold'))
tagstatus_label = canvas1.create_window(75, 55, window=status_label)

CB.pack
canvas1.create_window(150, 280, window=CB)

content = tkinter.Label(frame, text='', fg='black', font=('helvetica', 12, 'bold'))
tagcontent = canvas1.create_window(150, 300, window=content)
frame.after(1000, Refresh)
frame.mainloop()
