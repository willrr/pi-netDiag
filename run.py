import tkinter, socket, fcntl, shlex, struct
from tkinter import messagebox
from subprocess import Popen, PIPE, STDOUT
#import sys

#import all the requirements for the program
#tkinter gives the user interface, socket, fcntl & struct is required for ip, default Gateway and subnet mask
#shlex is required for accessing the command line (to use ping)
#subprocess imports are required for command line

root = tkinter.Tk() #set root throughout the program
#root.geometry('480x320')
root.attributes('-fullscreen', False) #set to fullscreen
root.title("Network Tester") #set title for program
ifname='wlp2s0' #set ifname to the interface name eg. 'eth0' is the ethernet port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #a command used a lot throughout the code so this is used to reduce the repetition

def internalIP():
  o = socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack(b'256s', bytes(ifname[:15], 'utf-8')))[20:24]) #set o to internal ip on the interface defined as ifname
  messagebox.showinfo("Internal ip", o) #messagebox the user with the IP

iIp = tkinter.Button(root, text ="Internal IP", command = internalIP) #define button that runs internalIP

def defaultGateway():
  with open("/proc/net/route") as fh: #open file /proc/net/route
    for line in fh: #read each line in file
      fields = line.strip().split() #create an array of all lines in file
      if fields[1] != '00000000' or not int(fields[3], 16) & 2: #find the line that isn't '00000000' (this will be the gateway code)
        continue
      o = socket.inet_ntoa(struct.pack("<L", int(fields[2], 16))) #convert gateway code to default gateway and set to o
  messagebox.showinfo("Default Gateway:", o) #send a messagebox with the default gateway

dG = tkinter.Button(root, text ="Default Gateway", command = defaultGateway) #define the default gateway button

def subnetCheck():
  o = socket.inet_ntoa(fcntl.ioctl(s, 35099, struct.pack(b'256s', bytes(ifname, 'utf-8')))[20:24]) #get the subnet mask
  messagebox.showinfo("Subnet Mask:", o) #tell the user the subnet mask

sNM = tkinter.Button(root, text ="Subnet Mask", command = subnetCheck) #define the subnet mask button

def get_simple_cmd_output(cmd, stderr=STDOUT):
  #Execute a simple external command and get its output.
  args = shlex.split(cmd)
  return Popen(args, stdout=PIPE, stderr=stderr).communicate()[0]

def get_ping_time(host):
  host = host.split(':')[0] #split ping address into an array
  cmd = "fping {host} -C 3 -q".format(host=host) #run command fping for host array fping is used to simplify the output down to just ping times -C is the amount of times and -q simplifies the output
  res = [float(x) for x in get_simple_cmd_output(cmd).strip().split(b':')[-1].split() if x != b'-'] #get the output and store it (each ping stored in the array)
  print(res)
  if len(res) > 0:
    return sum(res) / len(res) #divide the sum of the output and divide by the amount in the string
  else:
    return 999999

def ping8():
    messagebox.showinfo("Pinging 8.8.8.8", get_ping_time('8.8.8.8'))

p8 = tkinter.Button(root, text ="Ping 8.8.8.8", command = ping8) #width = 320

def ping4():
    messagebox.showinfo("Ping 4.2.2.2", get_ping_time('4.2.2.2'))

p4 = tkinter.Button(root, text ="Ping 4.2.2.2", command = ping4)

def pingG():
    messagebox.showinfo("Pinging google.com", get_ping_time('google.com'))

pG = tkinter.Button(root, text ="Ping Google.com", command = pingG)

def pingB():
    messagebox.showinfo("Pinging bbc.co.uk", get_ping_time('bbc.co.uk'))

pB = tkinter.Button(root, text ="Ping bbc.co.uk", command = pingB)

iIp.pack()
dG.pack()
sNM.pack()
p8.pack()
p4.pack()
pG.pack()
pB.pack()
root.mainloop()
