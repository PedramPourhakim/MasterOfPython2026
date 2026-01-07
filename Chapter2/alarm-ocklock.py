#imports and global variables
import tkinter as tk
window = tk.Tk()
window.title("Alarm O'clock App")
window.resizable(width=False, height=False)
window.geometry("600x500")

#function for getting current time



# function set alarm timer
def set_alarm():
    print("Alarm has been set",hour_alarm_entry.get(),minute_alarm_entry.get())


#function for comparing time with alarm


#ui design


# text time

time_label = tk.Label(window,text="12:30:30",font=("Tahoma",32))
time_label.pack()


# text input hour

# input entry
tk.Label(window,text="Hour").pack()
hour_alarm_entry = tk.Entry(window)
hour_alarm_entry.pack()

# text input minute

# input entry
tk.Label(window,text="Minute").pack()
minute_alarm_entry = tk.Entry(window)
minute_alarm_entry.pack()

# button set alarm
tk.Button(window,text="Set Alarm",command=set_alarm).pack()

# showing last alarm
latest_alram_label =  tk.Label(window,text="12:31")
latest_alram_label.pack()
#running application
window.mainloop()