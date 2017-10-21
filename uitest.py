import sys
import tkinter
from tkinter import messagebox
import os
root = tkinter.Tk()
root.geometry('480x320')
root.title("Network Tester")
def internalIP():
    messagebox.showinfo("Internal ip","Goes Here")
iIp = tkinter.Button(root, text ="Internal IP", command = internalIP, width = 320)
def ping8():
    messagebox.showinfo("Pinging 8.8.8.8","yes")    
p8 = tkinter.Button(root, text ="Ping 8.8.8.8", command = ping8, width = 320)
def pingURL():
    messagebox.showinfo("Internal ip","Goes Here")
pU = tkinter.Button(root, text ="ping URL", command = pingURL, width = 320)
def subnetCheck():
    messagebox.showinfo("Internal ip","Goes Here")
cS = tkinter.Button(root, text ="Check subnet", command = subnetCheck, width = 320)

iIp.pack()
p8.pack()
pU.pack()
cS.pack()
root.mainloop()
