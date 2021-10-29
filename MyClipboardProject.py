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
path_to_file = f'{config_file_name}'
# Check if file exists. Return (and save in variable): True or False
path = Path(path_to_file)

saved_config_data = ["myID", "myMAIL", "myGMAIL"]

# Top level window
frame = tkinter.Tk()
frame.title('Copy to clipboard')
frame.geometry('400x400')

canvas = tkinter.Canvas(frame, width=300, height=400)
canvas.pack()

var1 = tkinter.IntVar()
status = [0, 0, 0]

# declare this so they can be used as global in the Save Config Call Back function
input_txt = [tkinter.Text(), tkinter.Text(), tkinter.Text()]
#input_txt1 = tkinter.Text()
#input_txt2 = tkinter.Text()
#input_txt3 = tkinter.Text()
Label_Save = tkinter.Label()


def IDCallBack():
    global label
    if (status[0] == 1):
        label.configure(text='ID was copied to clipboard')
        B[0].configure(background='green')
        B2.configure(background='gray')
        B3.configure(background='gray')
        pyperclip.copy(saved_config_data[0])
    else:
        label.configure(text='ID not configured')
        B[0].configure(background='gray')


def MailCallBack():
    global label
    if (status[1] == 1):
        label.configure(text='MAIL was copied to clipboard')
        B[0].configure(background='gray')
        B2.configure(background='green')
        B3.configure(background='gray')
        pyperclip.copy(saved_config_data[1])
    else:
        label.configure(text='MAIL not configured')
        B2.configure(background='gray')


def GMailCallBack():
    global label
    if (status[2] == 1):
        label.configure(text='GMAIL was copied to clipboard')
        B[0].configure(background='gray')
        B2.configure(background='gray')
        B3.configure(background='green')
        pyperclip.copy(saved_config_data[2])
    else:
        label.configure(text='GMAIL not configured')
        B3.configure(background='gray')


def Refresh():
    global content
    if (var1.get() == 1):
        content.configure(text=pyperclip.paste())
    else:
        content.configure(text='')

    str = pyperclip.paste()
    if (str != saved_config_data[0]):
        B[0].configure(background='gray')
    if (str != saved_config_data[1]):
        B2.configure(background='gray')
    if (str != saved_config_data[2]):
        B3.configure(background='gray')
    Check_Input_Data()
    Set_Status()
    frame.after(500, Refresh)


def Check_sel():
    if (var1.get() == 1):
        content.configure(text=pyperclip.paste())
    else:
        content.configure(text='')


def Configure_Input_Data():
    global input_txt, Label_Save
    # Toplevel object which will be treated as a new window
    configWindow = tkinter.Toplevel(frame)

    # sets the title of the Toplevel widget
    configWindow.title("Configuration Window")

    # sets the geometry of toplevel
    configWindow.geometry("500x200")

    tkinter.Label(configWindow, text="ENTER ID").grid(row=0)
    tkinter.Label(configWindow, text="ENTER MAIL").grid(row=1)
    tkinter.Label(configWindow, text="ENTER GMAIL").grid(row=2)
    input_txt[0] = tkinter.Text(configWindow, height=1, width=45)
    input_txt[1] = tkinter.Text(configWindow, height=1, width=45)
    input_txt[2] = tkinter.Text(configWindow, height=1, width=45)
    input_txt[0].grid(row=0, column=1)
    input_txt[1].grid(row=1, column=1)
    input_txt[2].grid(row=2, column=1)
    tkinter.Button(configWindow, text='Close', command=configWindow.destroy).grid(row=5, column=0, sticky=tkinter.W,
                                                                                  pady=4)
    tkinter.Button(configWindow, text='Save', command=Data_Save_Call_Back).grid(row=5, column=1, sticky=tkinter.W,
                                                                                pady=4)
    Label_Save = tkinter.Label(configWindow, height=1, width=45)
    Label_Save.grid(row=6, column=1)

    if path.is_file():
        print(f'File {path_to_file} found')
        f = open(path_to_file, "r")
        Lines = f.read().splitlines()
        i = 0
        for line in Lines:
            saved_config_data[i] = line[6:]
            print(saved_config_data[i])
            i = i + 1
        f.close()

        input_txt[0].insert('end', saved_config_data[0])
        input_txt[1].insert('end', saved_config_data[1])
        input_txt[2].insert('end', saved_config_data[2])

    else:
        f = open(path_to_file, "w")
        print(f'File {path_to_file} created')
        f.close()


def Data_Save_Call_Back():
    global input_txt1, Label_Save
    f = open(path_to_file, "w")
    f.write("Line1:" + input_txt[0].get('1.0', 'end-1c') + "\n")
    f.write("Line2:" + input_txt[1].get('1.0', 'end-1c') + "\n")
    f.write("Line3:" + input_txt[2].get('1.0', 'end-1c'))
    f.close()
    Label_Save.configure(text="Configuration Saved. Close the Configuration Window")


def Check_Input_Data():
    if path.is_file():
        print(f'File {path_to_file} found')
        f = open(path_to_file, "r")
        Lines = f.read().splitlines()
        i = 0
        for line in Lines:
            saved_config_data[i] = line[6:]
            print(saved_config_data[i])
            i = i + 1
        f.close()
    if saved_config_data[0] != "default" and saved_config_data[0] != "":
        status[0] = 1
    else:
        status[0] = 0
    if saved_config_data[1] != "default" and saved_config_data[1] != "":
        status[1] = 1
    else:
        status[1] = 0
    if saved_config_data[2] != "default" and saved_config_data[2] != "":
        status[2] = 1
    else:
        status[2] = 0


def Set_Status():
    if (status[0] == 0):
        canvas.itemconfig(S1, fill="red")  # Fill the circle with RED
    else:
        canvas.itemconfig(S1, fill="green")  # Fill the circle with GREEN

    if (status[1] == 0):
        canvas.itemconfig(S2, fill="red")  # Fill the circle with RED
    else:
        canvas.itemconfig(S2, fill="green")  # Fill the circle with GREEN
    if (status[2] == 0):
        canvas.itemconfig(S3, fill="red")  # Fill the circle with RED
    else:
        canvas.itemconfig(S3, fill="green")  # Fill the circle with GREEN


B = [tkinter.Button(), tkinter.Button(), tkinter.Button()]
B[0] = tkinter.Button(frame, text="ID", background='gray', height=1, width=5, command=IDCallBack)
B[0].pack()
canvas.create_window(150, 80, window=B[0])

#B[0] = tkinter.Button(frame, text="ID", background='gray', height=1, width=5, command=IDCallBack)
B2 = tkinter.Button(frame, text="MAIL", background='gray', height=1, width=5, command=MailCallBack)
B3 = tkinter.Button(frame, text="GMAIL", background='gray', height=1, width=5, command=GMailCallBack)

Check_Input_Data()

S1 = canvas.create_oval(70, 75, 80, 85)
S2 = canvas.create_oval(70, 110, 80, 120)
S3 = canvas.create_oval(70, 145, 80, 155)

Set_Status()

Config_button = tkinter.Button(frame, text="CONFIGURE", background='green', height=1, width=10,
                               command=Configure_Input_Data)

CB = tkinter.Checkbutton(text='See current clipboard', font=('helvetica', 10), variable=var1, onvalue=1, offvalue=0,
                         command=Check_sel)

Config_button.pack()
canvas.create_window(20, 20, window=Config_button)

#B[0].pack()
#canvas.create_window(150, 80, window=B[0])
B2.pack()
canvas.create_window(150, 120, window=B2)
B3.pack()
canvas.create_window(150, 160, window=B3)

label = tkinter.Label(frame, text='', fg='green', font=('helvetica', 12, 'bold'))
taglabel = canvas.create_window(150, 220, window=label)

status_label = tkinter.Label(frame, text='Status', fg='black', font=('helvetica', 12, 'bold'))
tagstatus_label = canvas.create_window(75, 55, window=status_label)

CB.pack
canvas.create_window(150, 280, window=CB)

content = tkinter.Label(frame, text='', fg='black', font=('helvetica', 12, 'bold'))
tagcontent = canvas.create_window(150, 300, window=content)
frame.after(1000, Refresh)
frame.mainloop()
