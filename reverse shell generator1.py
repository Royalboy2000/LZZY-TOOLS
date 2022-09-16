
import sys,time,os

def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1) 

message ="welcome to reverse shell generator\n"

for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)

print("")

def startlistener():
    os.system("bash android.sh")

def startlistener2():
    os.system("bash android2.sh")

def startlistener3():
    os.system("bash android3.sh")

def startlistener4():
    os.system("bash android4.sh")


android1 =print('1:Android REVERSE TCP \n ')

android2 =print ('2:Android meterpreter Embeded reverse TCP \n ')
windows =print ('3:windows powershell \n ')
install = print('4:install requirements needed \n')

options = input('please choose options: ')


if options == "1":
    print("")
 
typingPrint("starting the listener in 3...\n")
time.sleep(1)
typingPrint("2...\n")
time.sleep(1)
typingPrint("1...\n")
time.sleep(1)
startlistener()

if options == "2":
     print("")
 
typingPrint("starting the listener in 3...\n")
time.sleep(1)
typingPrint("2...\n")
time.sleep(1)
typingPrint("1...\n")
time.sleep(1)
startlistener2()

if options == "3":

     print("")
typingPrint("starting the listener in 3...\n")
time.sleep(1)
typingPrint("2...\n")
time.sleep(1)
typingPrint("1...\n")
time.sleep(1)
startlistener3()

    


if options == "4":
    typingPrint("starting the listener in 3...\n")
time.sleep(1)
typingPrint("2...\n")
time.sleep(1)
typingPrint("1...\n")
time.sleep(1)
startlistener4()

