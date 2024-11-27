#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import time
from PIL import Image, ImageTk
from tkinter import PhotoImage

root = tk.Tk()
start_icon = PhotoImage(file="start.png")
lap_icon = PhotoImage(file="lap.png")
reset_icon = PhotoImage(file="reset.png")
stop_icon = PhotoImage(file="stop.png")
resume_icon = PhotoImage(file="resume.png")

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.root.attributes("-topmost", True)

        self.elapsed_time = 0
        self.running = False
        self.start_time = 0

        self.label = tk.Label(root, text="00:00:00", font=("Helvetica", 32))
        self.label.pack()

        #self.start_button = tk.Button(root, text="Start", command=self.start, font=("Helvetica", 12), fg="brown")
        #self.stop_button = tk.Button(root, text="Stop", command=self.stop, font=("Helvetica", 12), fg="red")
        #self.lap_button = tk.Button(root, text="Lap", command=self.lap, font=("Helvetica", 12), fg="teal")
        #self.reset_button = tk.Button(root, text="Reset", command=self.reset, font=("Helvetica", 12), fg="teal")
        #self.resume_button = tk.Button(root, text="Resume", command=self.start, font=("Helvetica", 12), fg="forestgreen")
        self.start_button = tk.Button(root, image=start_icon, command=self.start)
        self.stop_button = tk.Button(root, image=stop_icon, command=self.stop)
        self.lap_button = tk.Button(root, image=lap_icon, command=self.lap)
        self.reset_button = tk.Button(root, image=reset_icon, command=self.reset)
        self.resume_button = tk.Button(root, image=resume_icon, command=self.start)

        self.start_button.pack()

        self.lap_times = []
        self.lap_display = tk.Label(root, text="")
        self.lap_display.pack()

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update()
            self.start_button.pack_forget()
            self.stop_button.pack()
            self.lap_button.pack()
            self.reset_button.pack()
            self.resume_button.pack_forget()
            self.reset_button.pack_forget()

    def stop(self):
        if self.running:
            self.running = False
            #self.update_buttons()
            self.start_time = time.time()
            self.update()
            self.stop_button.pack_forget()
            self.resume_button.pack()
            self.reset_button.pack()
            self.lap_button.pack_forget()
            
    def lap(self):
        if self.running:
            lap_time = self.elapsed_time
            self.lap_times.append(self.format_time(lap_time))
            self.update_lap_display()
            self.resume_button.pack_forget()
        
    def reset(self):
        self.elapsed_time = 0
        self.start_time = time.time()
        self.lap_times = []
        self.update()
        self.update_lap_display()
        self.stop()
        self.resume_button.pack_forget()  
        self.start_button.pack() 
        self.reset_button.pack_forget()
        self.resume_button.pack_forget()
        
    def update(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.label.config(text=self.format_time(self.elapsed_time))
        self.root.after(10, self.update)

    def format_time(self, elapsed):
        minutes, seconds = divmod(int(elapsed), 60)
        hours, minutes = divmod(minutes, 60)
        milliseconds = int((elapsed - int(elapsed)) * 100)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:02d}"

    def update_lap_display(self):
        self.lap_display.config(text="\n".join(self.lap_times))


stopwatch = Stopwatch(root)
root.mainloop()


# In[ ]:




