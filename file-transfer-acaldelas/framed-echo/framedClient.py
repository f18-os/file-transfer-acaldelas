#! /usr/bin/env python3

# Echo client program
import socket, sys, re
"""Socket provides access to the BSD socket interface.
When socket() is called it returns a socket object which contains different calls
like read and write, buffer allocaiton on receive opations is automatic and buffer length
is imclicit on send ops"""
"""SYS -Things that talk to the interpreter and funcitons and is always available"""
"""re - Regular expression operations"""


#.path is a list of strings that specifies the search path for modules
#.append is a string apprending
sys.path.append("../lib")       # for params
#Library that is under the lib folder
import params

#From the python file in the same directory we are using the following
from framedSock import framedSend, framedReceive

#Default options to use
switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )
print(type(switchesVarDefaults))
print(switchesVarDefaults)
progname = "framedClient"
#Function call to params for parsing the parameters
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug  = paramMap["server"], paramMap["usage"], paramMap["debug"]

if usage:
    params.usage()


try:
    serverHost, serverPort = re.split(":", server)
    serverPort = int(serverPort)
except:
    print("Can't parse server:port from '%s'" % server)
    sys.exit(1)

s = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socktype, proto, canonname, sa = res
    try:
        print("creating sock: af=%d, type=%d, proto=%d" % (af, socktype, proto))
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        s = None
        continue
    try:
        print(" attempting to connect to %s" % repr(sa))
        s.connect(sa)
    except socket.error as msg:
        print(" error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)


print("sending hello world")
framedSend(s, b"hello world", debug)
print("received:", framedReceive(s, debug))

print("sending hello world")
framedSend(s, b"hello world", debug)
print("received:", framedReceive(s, debug))

