from pyautogui import click,typewrite
from time import sleep
print("welcome to virtual-auto, the one stop shop for your vbox starter kit!")
sleep(2)
print("a few rules... make sure your desktop search bar is open!, windows only...")
sleep(3)
print("type 'help' to see our options")

command = input("->  ").lower()
sleep(2)
vbox_downloaded = False
kali_install = False
while True:
    command = input("-->").lower()
    if command == "vbox":
        print("sweet")
        sleep(3)
        print("let me take control for a sec, hands off the keyboard")
        sleep(5)
        click(371, 1047)
        typewrite("chrome")
        typewrite(["enter"])
        sleep(4)
        click(1055, 60)
        sleep(1)
        typewrite("https://download.virtualbox.org/virtualbox/6.0.14/VirtualBox-6.0.14-133895-Win.exe")
        typewrite(["enter"])
        sleep(3)
        print("virtualbox is downloaded")
        vbox_downloaded = True
    elif command == "kali":
        print("let me take control for a sec, hands off the keyboard")
        sleep(2)
        click(371, 1047)
        typewrite("chrome")
        typewrite(["enter"])
        sleep(4)
        click(1055, 60)
        sleep(1)
        typewrite("https://images.offensive-security.com/virtual-images/kali-linux-2019.3-vmware-amd64.7z")
        typewrite(["enter"])
        sleep(3)
        print("kali is downloaded!")
    elif command == "ubuntu":
        print("let me take control for a sec, hands off the keyboard")
        sleep(2)
        click(371, 1047)
        typewrite("chrome")
        typewrite(["enter"])
        sleep(4)
        click(1055, 60)
        sleep(1)
        typewrite("http://releases.ubuntu.com/18.04.3/ubuntu-18.04.3-desktop-amd64.iso?_ga=2.66190636.347584942.1572806073-741636547.1570071645")
        typewrite(["enter"])
        sleep(3)
        print("ubuntu is downloaded!")
    elif command == "parrot":
        print("let me take control for a sec, hands off the keyboard")
        sleep(2)
        click(371, 1047)
        typewrite("chrome")
        typewrite(["enter"])
        sleep(4)
        click(1055, 60)
        sleep(1)
        typewrite("https://download.parrot.sh/parrot/iso/4.7/Parrot-security-4.7_virtual.ova")
        typewrite(["enter"])
        sleep(3)
        print("ubuntu is downloaded!")
    elif command == "android":
        print("let me take control for a sec, hands off the keyboard")
        sleep(4)
        click(371, 1047)
        typewrite("chrome")
        typewrite(["enter"])
        sleep(4)
        click(1055, 60)
        sleep(1)
        typewrite("https://sourceforge.net/projects/osboxes/files/v/vb/1-A-d/8.1-R2/Ax86-8.1-R2-VB-64bit.7z/download")
        typewrite(["enter"])
        sleep(3)
        print("android is downloaded!")
    elif command == "everything":
        print("sweet")
        sleep(3)
        print("let me take control for a sec, hands off the keyboard")
        sleep(5)
        click(371, 1047)
        typewrite("chrome")
        typewrite(["enter"])
        sleep(4)
        click(1055, 60)
        sleep(1)
        typewrite("https://download.virtualbox.org/virtualbox/6.0.14/VirtualBox-6.0.14-133895-Win.exe")
        typewrite(["enter"])
        sleep(3)
        print("vbox is downloaded")
        click(1055, 60)
        sleep(1)
        typewrite("https://images.offensive-security.com/virtual-images/kali-linux-2019.3-vmware-amd64.7z")
        typewrite(["enter"])
        sleep(3)
        print("kali is downloaded!")
        click(1055, 60)
        sleep(1)
        typewrite("http://releases.ubuntu.com/18.04.3/ubuntu-18.04.3-desktop-amd64.iso?_ga=2.66190636.347584942.1572806073-741636547.1570071645")
        typewrite(["enter"])
        sleep(3)
        print("ubuntu is downloaded!")
        click(1055, 60)
        sleep(1)
        typewrite("https://download.parrot.sh/parrot/iso/4.7/Parrot-security-4.7_virtual.ova")
        typewrite(["enter"])
        sleep(3)
        print("parrot is downloaded!")
        click(1055, 60)
        sleep(1)
        typewrite("https://sourceforge.net/projects/osboxes/files/v/vb/1-A-d/8.1-R2/Ax86-8.1-R2-VB-64bit.7z/download")
        typewrite(["enter"])
        sleep(3)
        print("android is downloaded!")
        print("Everything is downloaded!")



    elif command == "quit":
        print("until we meet again")
        sleep(3)
        break
    elif command =="help":
        print("""
        vbox - downloads virtualbox
        kali - downloads a kali vbox ova 
        ubuntu - downloads linux ubuntu
        parrot - downloads parrot security os
        win10 - downloads windows 10 iso
        everything - NICE! downloads every option
        
        """)
    else:
        print("i didnt catch that, type 'help' for options")



