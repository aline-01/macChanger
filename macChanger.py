import os
import re
import time
from subprocess import check_output
from argparse import ArgumentParser

user = check_output("whoami",shell=True)
user = str(user)
user = user[2:-3]
if user != "root":
    print("[!] you not root")
    print("[!] for run this you must be root")
    exit()

def logo():
    print("""              _____ _
                          /  __ \ |                                 
      _ __ ___   __ _  ___| /  \/ |__   __ _ _ __   __ _  ___ _ __  
     | '_ ` _ \ / _` |/ __| |   | '_ \ / _` | '_ \ / _` |/ _ \ '__| 
     | | | | | | (_| | (__| \__/\ | | | (_| | | | | (_| |  __/ |    
     |_| |_| |_|\__,_|\___|\____/_| |_|\__,_|_| |_|\__, |\___|_|    
                                                   __/ |           
                                                   |___/   
         -i --interface  =  your interface
         -m --mac  =  your new mac address
    """)

logo()

def change_mac(mac,interface):
    os.system("sudo ifconfig " + interface + " down")
    os.system("sudo ifconfig " + interface + " hw ether " + mac)
    os.system("sudo ifconfig " + interface + " up")
    print("\t [+] mac is change")
    print("\t [+] interface: "+interface)
    print("\t [+] new mac: "+mac)

def create_argument():
    parser = ArgumentParser()
    parser.add_argument("-i","--interface",dest="interface",help="[+] give your interface with -i or --interface")
    parser.add_argument("-m","--mac",dest="mac",help="[+] give me a mac address with -m or --mac")
    options = parser.parse_args()
    return options

arguments = create_argument()
mac = arguments.mac
interface = arguments.interface

if interface == None:
    print("\t [!] give me your interface")
    time.sleep(2)
    exit()

mac_regex = "^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$"
if mac == None:
    print("\t [!] give me a mac address ")
    time.sleep(2)
    exit()
else:
    true_mac = re.search(mac_regex,mac)
    if true_mac == None:
        print("\t [!] give me true mac address")
        time.sleep(2)
        exit()

change_mac(mac,interface)

print("it's must be update")

