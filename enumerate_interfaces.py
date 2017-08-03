# -*- coding: utf-8 -*-
# Use those functions to enumerate all interfaces available on the system using Python.
# found on <http://code.activestate.com/recipes/439093/#c1>

import socket
import fcntl
import struct
import array


def format_ip(addr):
    return '{0}.{1}.{2}.{3}'.format(str(addr[0]), str(addr[1]), str(addr[2]), str(addr[3]))

def all_interfaces():
    max_possible = 128  # arbitrary. raise if needed.
    bytes = max_possible * 32
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    names = array.array('B', B'\0' * bytes)
    outbytes = struct.unpack('iL', fcntl.ioctl(
        s.fileno(),
        0x8912,  # SIOCGIFCONF
        struct.pack('iL', bytes, names.buffer_info()[0])
    ))[0]
    namestr = names.tostring()
    d = {}
    for i in range(0, outbytes, 40):
        name = namestr[i:i+16].split(B'\0', 1)[0].decode()
        ip   = namestr[i+20:i+24]
        d[name] = format_ip(ip)
    return d



ifs = all_interfaces()
for name,ip in ifs.items():
    print(name,ip)
