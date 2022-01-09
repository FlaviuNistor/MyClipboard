# used to create the GUI
from tkinter import *
# used to interact with the clipboard
import pyperclip

# used to lunch an command to the OS
from subprocess import check_call
# used to check if file exists
from pathlib import Path

# use dictionary to convert suggestive color name to hex
# I used : https://htmlcolorcodes.com/
color_convertor = {
    "mygray": "#C8D6D8",
    "myred": "#F78383",
    "mygreen": "#33753F"
    }

# Expected configuration file name for storing the input information
config_file_name = 'config.txt'
# Path expected
path_to_file = f'{config_file_name}'
# Check if file exists. Return (and save in variable): True or False
path = Path(path_to_file)

# used to stored the saved configuration. Take this default values
saved_config_data = ["myID", "myMAIL", "myGMAIL"]

# Top level window (main window). Set title and size
root = Tk()
root.title('Copy to clipboard')

# variable used to store the value of the checked box (True or False)
var1 = IntVar()
# list to store the state of the status indicator
status = [0, 0, 0]

# declare this list so they can be used as global in the Save Config Call Back function
input_txt = [Text(), Text(), Text()]
# declare a label to be able to print out a message when configuration is saved
save_message = Label()

# CallBack function for pressing the ID button
def IDCallBack():
    global main_win_message
    # Change the color of the buttons to reflect the current selection
    if status[0] == 1:
        main_win_message.configure(text='ID was copied to clipboard', fg=color_convertor["mygreen"])
        B[0].configure(background=color_convertor["mygreen"])
        B[1].configure(background=color_convertor["mygray"])
        B[2].configure(background=color_convertor["mygray"])
        pyperclip.copy(saved_config_data[0])
    else:
        main_win_message.configure(text='ID not configured', fg=color_convertor["myred"])
        B[0].configure(background=color_convertor["mygray"])


# CallBack function for pressing the MAIL button
def MailCallBack():
    global main_win_message
    # Change the color of the buttons to reflect the current selection
    if status[1] == 1:
        main_win_message.configure(text='MAIL was copied to clipboard', fg=color_convertor["mygreen"])
        B[0].configure(background=color_convertor["mygray"])
        B[1].configure(background=color_convertor["mygreen"])
        B[2].configure(background=color_convertor["mygray"])
        pyperclip.copy(saved_config_data[1])
    else:
        main_win_message.configure(text='MAIL not configured', fg=color_convertor["myred"])
        B[1].configure(background=color_convertor["mygray"])


# CallBack function for pressing the GMAIL button
def GMailCallBack():
    global main_win_message
    # Change the color of the buttons to reflect the current selection
    if status[2] == 1:
        main_win_message.configure(text='GMAIL was copied to clipboard', fg=color_convertor["mygreen"])
        B[0].configure(background=color_convertor["mygray"])
        B[1].configure(background=color_convertor["mygray"])
        B[2].configure(background=color_convertor["mygreen"])
        pyperclip.copy(saved_config_data[2])
    else:
        main_win_message.configure(text='GMAIL not configured', fg=color_convertor["myred"])
        B[2].configure(background=color_convertor["mygray"])


# Function to refresh the GUI
def Refresh():
    global content
    Check_sel()
    str = pyperclip.paste()
    i = 0
    while i <= 2:
        if str != saved_config_data[i]:
            B[i].configure(background=color_convertor["mygray"])
        i += 1
    Check_Input_Data()
    Set_Status()
    root.after(500, Refresh)


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
        content.configure(text=(paperclip_content[:50]), bd=2, relief=SUNKEN)
    else:
        content.configure(text='', bd=2, relief=FLAT)


# Function used to configure the input data
def Configure_Input_Data():
    global input_txt, save_message
    # Toplevel object which will be treated as a new window
    configWindow = Toplevel(root)

    # sets the title of the Toplevel widget
    configWindow.title("Configuration Window")

    # sets the geometry of toplevel
    configWindow.geometry("500x200")

    Label(configWindow, text="ENTER ID").grid(row=0)
    Label(configWindow, text="ENTER MAIL").grid(row=1)
    Label(configWindow, text="ENTER GMAIL").grid(row=2)
    # use a while to set the objects and index row based on var i
    i = 0
    while i <= 2:
        input_txt[i] = Text(configWindow, height=1, width=45)
        input_txt[i].grid(row=i, column=1)
        i += 1
    Button(configWindow, text='Close', command=configWindow.destroy).grid(row=5, column=0, sticky=W,
                                                                                pady=4)
    Button(configWindow, text='Save', command=Data_Save_Call_Back).grid(row=5, column=1, sticky=W,
                                                                                pady=4)
    save_message = Label(configWindow, height=1, width=45)
    save_message.grid(row=6, column=1)

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
    global input_txt, save_message
    valid_data = 0  # use variable to signal is email addresses are valid
    at_index = [0, 0]   # list with index position for ""@"
    # check if string is empty. If it is that ios considered valid
    # if not empty should respect the rule in order to be valid
    # rule: must contain '@'  and a '.' after
    if input_txt[1].get('1.0', 'end-1c') != "":
        at_index[0] = input_txt[1].get('1.0', 'end-1c').find("@")
        if "@" in input_txt[1].get('1.0', 'end-1c') and "." in input_txt[1].get('1.0', 'end-1c')[at_index[0]:]:
            valid_data += 1
    else:
        valid_data += 1

    # check if string is empty. If it is that ios considered valid
    # if not empty should respect the rule in order to be valid
    # rule: must contain '@'  and a '.' after
    if input_txt[2].get('1.0', 'end-1c') != "":
        at_index[1] = input_txt[2].get('1.0', 'end-1c').find("@")
        if "@" in input_txt[2].get('1.0', 'end-1c') and "." in input_txt[2].get('1.0', 'end-1c')[at_index[1]:]:
            valid_data += 2
    else:
        valid_data += 2

    # check both addresses are valid, and if so update the config file
    if valid_data == 3:
        f = open(path_to_file, "w")
        f.write("Line1:" + input_txt[0].get('1.0', 'end-1c') + "\n")
        f.write("Line2:" + input_txt[1].get('1.0', 'end-1c') + "\n")
        f.write("Line3:" + input_txt[2].get('1.0', 'end-1c'))
        f.close()
        save_message.configure(text="Configuration Saved. Close the Configuration Window")
    # both addresses are not valid
    elif valid_data == 0:
        save_message.configure(text="Both GMAIL and MAIL are not valid")
    # first address is not valid
    elif valid_data == 2:
        save_message.configure(text="MAIL is not valid")
    # second address is not valid
    elif valid_data == 1:
        save_message.configure(text="GMAIL is not valid")

# Function to check if the configured input data is valid
def Check_Input_Data():
    if path.is_file():
        #print(f'File {path_to_file} found')
        f = open(path_to_file, "r")
        Lines = f.read().splitlines()
        i = 0
        for line in Lines:
            saved_config_data[i] = line[6:]
            #print(saved_config_data[i])
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
        canvas1.itemconfig(Status_Indicator[0], fill=color_convertor["myred"])  # Fill the circle with RED
    else:
        canvas1.itemconfig(Status_Indicator[0], fill=color_convertor["mygreen"])  # Fill the circle with GREEN

    if status[1] == 0:
        canvas2.itemconfig(Status_Indicator[1], fill=color_convertor["myred"])  # Fill the circle with RED
    else:
        canvas2.itemconfig(Status_Indicator[1], fill=color_convertor["mygreen"])  # Fill the circle with GREEN
        
    if status[2] == 0:
        canvas3.itemconfig(Status_Indicator[2], fill=color_convertor["myred"])  # Fill the circle with RED
    else:
        canvas3.itemconfig(Status_Indicator[2], fill=color_convertor["mygreen"])  # Fill the circle with GREEN


# Declare list of buttons that will be used the in main window for ID, MAIL and GMAIL
B = [Button(), Button(), Button()]
B[0] = Button(root, text="ID", background=color_convertor["mygray"], height=1, width=5, command=IDCallBack)
B[0].grid(row=2, column=2, padx=10, pady=10, sticky=NW)

B[1] = Button(root, text="MAIL", background=color_convertor["mygray"], height=1, width=5, command=MailCallBack)
B[1].grid(row=3, column=2, padx=10, pady=10, sticky=NW)

B[2] = Button(root, text="GMAIL", background=color_convertor["mygray"], height=1, width=5, command=GMailCallBack)
B[2].grid(row=4, column=2, padx=10, pady=20, sticky=NW)

Check_Input_Data()

canvas1 = Canvas(root, height=20, width=20)
canvas1.grid(row=2, column=1)
canvas2 = Canvas(root, height=20, width=20)
canvas2.grid(row=3, column=1)
canvas3 = Canvas(root, height=20, width=20)
canvas3.grid(row=4, column=1)

# List of status indicators
Status_Indicator = [canvas1.create_oval(2, 7, 10, 15), canvas2.create_oval(2, 7, 10, 15), canvas3.create_oval(2, 7, 10, 15)]

Set_Status()

Config_button = Button(root, text="CONFIGURE", background=color_convertor["mygreen"], height=1, width=10,
                               command=Configure_Input_Data)
Config_button.grid(row=0, column=0)

CB = Checkbutton(root, text='See current clipboard', font=('helvetica', 10), variable=var1, onvalue=1, offvalue=0,
                         command=Check_sel)
CB.grid(row=7, column=1, columnspan=3, pady=10)

main_win_message = Label(root, text='', fg=color_convertor["mygreen"], font=('helvetica', 12, 'bold'), width=10)
main_win_message.grid(row=6, column=0, columnspan=3, ipadx=160, ipady=10, padx=5, pady=10)

status_label = Label(root, text='Status', fg='black', font=('helvetica', 12, 'bold'))
status_label.grid(row=1, column=1, padx=20)

content = Label(root, text='', fg='black', font=('helvetica', 12, 'bold'), width=10)
content.grid(row=8, column=0, columnspan=3, ipadx=160, ipady=10, padx=5, pady=20)

# trigger the Refresh function after 500ms. After this the Refresh function will keep calling itself
root.after(1000, Refresh)
# use this to signal to other people this is an executable
if __name__ == "__main__":
    root.mainloop()
