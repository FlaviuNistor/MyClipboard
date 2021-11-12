# used to create the GUI
import tkinter
# used to interact with the clipboard
import pyperclip

# used to lunch an command to the OS
from subprocess import check_call
# used to check if file exists
from pathlib import Path

# Expected configuration file name for storing the input information
config_file_name = 'config.txt'
# Path expected
path_to_file = f'{config_file_name}'
# Check if file exists. Return (and save in variable): True or False
path = Path(path_to_file)

# used to stored the saved configuration. Take this default values
saved_config_data = ["myID", "myMAIL", "myGMAIL"]

# Top level window (main window). Set title and size
frame = tkinter.Tk()
frame.title('Copy to clipboard')
frame.geometry('400x400')

# Create a canvas on the main window
canvas = tkinter.Canvas(frame, width=300, height=400)
canvas.pack()

# variable used to store the value of the checked box (True or False)
var1 = tkinter.IntVar()
# list to store the state of the status indicator
status = [0, 0, 0]

# declare this list so they can be used as global in the Save Config Call Back function
input_txt = [tkinter.Text(), tkinter.Text(), tkinter.Text()]
# declare a label to be able to print out a message when configuration is saved
Save_Message = tkinter.Label()

# CallBack function for pressing the ID button
def IDCallBack():
    global label
    if status[0] == 1:
        label.configure(text='ID was copied to clipboard')
        B[0].configure(background='green')
        B[1].configure(background='gray')
        B[2].configure(background='gray')
        pyperclip.copy(saved_config_data[0])
    else:
        label.configure(text='ID not configured')
        B[0].configure(background='gray')


# CallBack function for pressing the MAIL button
def MailCallBack():
    global label
    if status[1] == 1:
        label.configure(text='MAIL was copied to clipboard')
        B[0].configure(background='gray')
        B[1].configure(background='green')
        B[2].configure(background='gray')
        pyperclip.copy(saved_config_data[1])
    else:
        label.configure(text='MAIL not configured')
        B[1].configure(background='gray')


# CallBack function for pressing the GMAIL button
def GMailCallBack():
    global label
    if status[2] == 1:
        label.configure(text='GMAIL was copied to clipboard')
        B[0].configure(background='gray')
        B[1].configure(background='gray')
        B[2].configure(background='green')
        pyperclip.copy(saved_config_data[2])
    else:
        label.configure(text='GMAIL not configured')
        B[2].configure(background='gray')


# Function to refresh the GUI
def Refresh():
    global content
    Check_sel()
    str = pyperclip.paste()
    i = 0
    while i <= 2:
        if str != saved_config_data[i]:
            B[i].configure(background='gray')
        i += 1
    Check_Input_Data()
    Set_Status()
    frame.after(500, Refresh)


# Function to check if the user wants to see the current content of clipboard by
# checking/unchecking the check-box
def Check_sel():
    if var1.get() == 1:
        # get clipboard content as string
        temp_string = pyperclip.paste()
        # make sure to get only the first line in case of large text in the clipboard
        # not to flood the content area with to much text. Use new line as separator
        paperclip_content = temp_string.split('\n')[0]
        # display max 50 characters from the first line of the clipboard content
        content.configure(text=(paperclip_content[:50]))
    else:
        content.configure(text='')


# Function used to configure the input data
def Configure_Input_Data():
    global input_txt, Save_Message
    # Toplevel object which will be treated as a new window
    configWindow = tkinter.Toplevel(frame)

    # sets the title of the Toplevel widget
    configWindow.title("Configuration Window")

    # sets the geometry of toplevel
    configWindow.geometry("500x200")

    tkinter.Label(configWindow, text="ENTER ID").grid(row=0)
    tkinter.Label(configWindow, text="ENTER MAIL").grid(row=1)
    tkinter.Label(configWindow, text="ENTER GMAIL").grid(row=2)
    # use a while to set the objects and index row based on var i
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
    Save_Message = tkinter.Label(configWindow, height=1, width=45)
    Save_Message.grid(row=6, column=1)

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


# CallBack function for pressing the SAVE button
def Data_Save_Call_Back():
    global input_txt, Save_Message
    f = open(path_to_file, "w")
    f.write("Line1:" + input_txt[0].get('1.0', 'end-1c') + "\n")
    f.write("Line2:" + input_txt[1].get('1.0', 'end-1c') + "\n")
    f.write("Line3:" + input_txt[2].get('1.0', 'end-1c'))
    f.close()
    Save_Message.configure(text="Configuration Saved. Close the Configuration Window")


# Function to check if the configured input data is valid
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


# Function used to set the status indicator for each of the possible configured data
def Set_Status():
    if status[0] == 0:
        canvas.itemconfig(Status_Indicator[0], fill="red")  # Fill the circle with RED
    else:
        canvas.itemconfig(Status_Indicator[0], fill="green")  # Fill the circle with GREEN

    if status[1] == 0:
        canvas.itemconfig(Status_Indicator[1], fill="red")  # Fill the circle with RED
    else:
        canvas.itemconfig(Status_Indicator[1], fill="green")  # Fill the circle with GREEN
        
    if status[2] == 0:
        canvas.itemconfig(Status_Indicator[2], fill="red")  # Fill the circle with RED
    else:
        canvas.itemconfig(Status_Indicator[2], fill="green")  # Fill the circle with GREEN


# Declare list of buttons that will be used the in main window for ID, MAIL and GMAIL
B = [tkinter.Button(), tkinter.Button(), tkinter.Button()]
B[0] = tkinter.Button(frame, text="ID", background='gray', height=1, width=5, command=IDCallBack)
B[0].pack()
canvas.create_window(150, 80, window=B[0])

B[1] = tkinter.Button(frame, text="MAIL", background='gray', height=1, width=5, command=MailCallBack)
B[1].pack()
canvas.create_window(150, 120, window=B[1])

B[2] = tkinter.Button(frame, text="GMAIL", background='gray', height=1, width=5, command=GMailCallBack)
B[2].pack()
canvas.create_window(150, 160, window=B[2])

Check_Input_Data()

# List of status indicators
Status_Indicator = [canvas.create_oval(70, 75, 80, 85), canvas.create_oval(70, 110, 80, 120), canvas.create_oval(70, 145, 80, 155)]

Set_Status()

Config_button = tkinter.Button(frame, text="CONFIGURE", background='green', height=1, width=10,
                               command=Configure_Input_Data)
Config_button.pack()
canvas.create_window(20, 20, window=Config_button)

CB = tkinter.Checkbutton(text='See current clipboard', font=('helvetica', 10), variable=var1, onvalue=1, offvalue=0,
                         command=Check_sel)
CB.pack
canvas.create_window(150, 280, window=CB)

label = tkinter.Label(frame, text='', fg='green', font=('helvetica', 12, 'bold'))
canvas.create_window(150, 220, window=label)

status_label = tkinter.Label(frame, text='Status', fg='black', font=('helvetica', 12, 'bold'))
canvas.create_window(75, 55, window=status_label)

content = tkinter.Label(frame, text='', fg='black', font=('helvetica', 12, 'bold'))
canvas.create_window(150, 300, window=content)

# trigger the Refresh function after 500ms. After this the Refresh function will keep calling itself
frame.after(1000, Refresh)
# use this to signal to other people this is an executable
if __name__ == "__main__":
    frame.mainloop()
