#import netifaces as nii
#import socket
#import struct
#ni.ifaddresses('wlp2s0')
#ip = ni.ifaddresses('wlp2s0')[ni.AF_INET][0]['addr']
#print(ip)
import socket
import fcntl
import struct
import shlex
from subprocess import Popen, PIPE, STDOUT

ifname = 'wlp2s0'

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def get_ip_address():
#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  return socket.inet_ntoa(fcntl.ioctl(s.fileno(),0x8915,struct.pack(b'256s', bytes(ifname[:15], 'utf-8')))[20:24])
#get_ip_address(iface)

print("IP:", get_ip_address())

def get_subnet_mask():
 return socket.inet_ntoa(fcntl.ioctl(socket.socket(socket.AF_INET, socket.SOCK_DGRAM), 35099, struct.pack(b'256s', bytes(ifname, 'utf-8')))[20:24])

print("Subnet Mask:",get_subnet_mask())

def get_default_gateway():
  #Read the default gateway directly from /proc.
  with open("/proc/net/route") as fh:
    for line in fh:
      fields = line.strip().split()
      if fields[1] != '00000000' or not int(fields[3], 16) & 2:
        continue
      return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))

print("Default Gateway:", get_default_gateway())

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

print("8.8.8.8 Avg Ping Time:", get_ping_time('8.8.8.8'))
print("4.2.2.2 Avg Ping Time:", get_ping_time('4.2.2.2'))
print("Google.com Avg Ping Time:", get_ping_time('google.com'))
print("bbc.co.uk Avg Ping Time:", get_ping_time('bbc.co.uk'))
