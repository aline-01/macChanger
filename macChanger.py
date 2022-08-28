import os
import re
import time
import random
import string
from subprocess import check_output
from argparse import ArgumentParser
from random import choice

user = check_output("whoami",shell=True)
user = str(user)
user = user[2:-3]
if user != "root":
    print("[!] you not root")
    print("[!] for run this you must be root")
    exit()

def logo():
    print("""                           _____ _
                          /  __ \ |                                 
      _ __ ___   __ _  ___| /  \/ |__   __ _ _ __   __ _  ___ _ __  
     | '_ ` _ \ / _` |/ __| |   | '_ \ / _` | '_ \ / _` |/ _ \ '__| 
     | | | | | | (_| | (__| \__/\ | | | (_| | | | | (_| |  __/ |    
     |_| |_| |_|\__,_|\___|\____/_| |_|\__,_|_| |_|\__, |\___|_|    
                                                   __/ |           
                                                   |___/   
         -i --interface  =  your interface
         -r --random = generate a random MAC address 
         -m --mac  =  enter the custom MAC addres
    """)

logo()


def create_argument():
    parser = ArgumentParser()
    parser.add_argument("-i","--interface",dest="interface",help="[+] give your interface with -i or --interface")
    parser.add_argument("-m","--mac",dest="mac",help="[+] give me a mac address with -m or --mac")
    parser.add_argument("-r","--random",action="store_true",help="[+] for generate random MAC address")
    options = parser.parse_args()
    return options

def create_mac():
    uppercase = ''.join(string.hexdigits.upper())
    mac = ""
    for i in range(6):
    	for j in range(2):
    	   if i == 0:
    	       mac += choice("02468ACE")
    	   else:
    	       mac += choice(uppercase)
    	mac += ":"
    return mac.strip(":")

def current_mac():
    ifconfig = check_output("ifconfig "+interface,shell=True)
    current_mac = re.search("ether (.+)",str(ifconfig)).group().split()[1].strip()
    return current_mac

def change_mac(mac,current_mac,interface):
    
    check_output("sudo ifconfig "+interface+" down",shell=True)
    check_output("sudo ifconfig "+interface+" hw ether "+mac,shell=True)
    check_output("sudo ifconfig "+interface+" up",shell=True)
    print("\t [+] mac is changed ")
    print("\t [+] interface : "+interface)
    print("\t [+] old mac : "+current_mac)
    print("\t [+] new mac : "+mac)
    print("")
    
	
arguments = create_argument()
mac = arguments.mac
interface = arguments.interface
random = arguments.random

if interface == None:
    print("\t [!] give me your interface")
    time.sleep(2)
    exit()

if random == True:
    mac = create_mac()
else:
    if mac == None:
       mac_regex = "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
       print("\t [!] give me a mac address ")
       time.sleep(2)
       exit()
    else:
       true_mac = re.search(mac_regex,mac)
       if true_mac == None:
          print("\t [!] give me true mac address")
          time.sleep(2)
          exit()

current_mac = current_mac()

change_mac(mac,current_mac,interface)



