import sys
import tkinter
from tkinter import messagebox
import os
import socket
import fcntl
import struct
import shlex
from subprocess import Popen, PIPE, STDOUT
root = tkinter.Tk()
root.geometry('480x320')
root.title("Network Tester")
ifname='enp1s0'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def internalIP():
  o = socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack(b'256s', bytes(ifname[:15], 'utf-8')))[20:24])
  messagebox.showinfo("Internal ip", o)
iIp = tkinter.Button(root, text ="Internal IP", command = internalIP, width = 320)
def defaultGateway():
  with open("/proc/net/route") as fh:
    for line in fh:
      fields = line.strip().split()
      if fields[1] != '00000000' or not int(fields[3], 16) & 2:
        continue
      o = socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))
  messagebox.showinfo("Default Gateway:", o)
dG = tkinter.Button(root, text ="Default Gateway", command = defaultGateway, width = 320)
def subnetCheck():
  o = socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack(b'256s', bytes(ifname, 'utf-8')))[20:24])
  messagebox.showinfo("Subnet Mask:", o)
S = tkinter.Button(root, text ="Subnet Mask", command = subnetCheck, width = 320)
def get_simple_cmd_output(cmd, stderr=STDOUT):
  #Execute a simple external command and get its output.
  args = shlex.split(cmd)
  return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]
def get_ping_time(host):
  host = host.split(':')[0]
  cmd = "fping {host} -C 3 -q".format(host=host)
  res = [float(x) for x in get_simple_cmd_output(cmd).strip().split(b':')[-1].split() if x != b'-']
  if len(res) > 0:
    return sum(res) / len(res)
  else:
    return 999999
def ping8():
  messagebox.showinfo("Pinging 8.8.8.8", get_ping_time('8.8.8.8'))
p8 = tkinter.Button(root, text ="Ping 8.8.8.8", command = ping8, width = 320)
def ping4():
    messagebox.showinfo("Ping 4.2.2.2", get_ping_time('4.2.2.2'))
p4 = tkinter.Button(root, text ="Ping 4.2.2.2", command = ping4, width = 320)
def pingG():
    messagebox.showinfo("Pinging google.com", get_ping_time('google.com'))
pG = tkinter.Button(root, text ="Ping Google.com", command = pingG, width = 320)
def pingB():
    messagebox.showinfo("Pinging bbc.co.uk", get_ping_time('bbc.co.uk'))
pB = tkinter.Button(root, text ="Ping bbc.co.uk", command = pingB, width = 320)

iIp.pack()
dG.pack()
S.pack()
p8.pack()
p4.pack()
pG.pack()
pB.pack()
root.mainloop()
