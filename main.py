from genericpath import isfile
from glob import glob
import os
import time

clear = lambda: os.system('cls')

def main():
    os.system('cls')
    print("               ---------------------------MENU--------------------")
    print("                            -----     [1] Register -----")
    print("                            -----     [2] Login    -----")
    print("                            -----     [3] Exit     -----")
    print("               --------------------------------------------------")
    
    while True:
        print()
        option = str(input("Please enter your choice [1] Register,[2] Login,[3] Exit:"))
        os.system("cls")
        if option in ["1","2","3"]:
            if os.path.isdir("users") == False:
                os.mkdir("users")
            break
    if option == '1':
        register()
    elif option == '2':
        login()
    elif option == '3':
        dquit()

def register():
    clear()
    print("Register")
    print("--------")
    time.sleep(2)
    clear()
    while True:
        global userName
        userName = input("Enter Your Name: ").lower()
        folName = userName.lower()
        os.chdir("users")
        if os.path.isdir(folName) == False:
            os.mkdir(folName)
            os.chdir(f"{folName}")
            infoU = userName.lower() + "info"
            os.mkdir(infoU)
            os.chdir(f"{infoU}")
            if userName != '':
                break
    while True:
        global pssword 
        pssword = input("Enter Your Password: ").lower()
        if pssword != '':
            time.sleep(1)
            tname = folName + "usN" + ".txt"
            pname = folName + "usP" + ".txt"
            os.system('cls')
            cpssword = input("Enter Your Password Again: ").lower()
            if cpssword == pssword:
                global userFile 
                userFile = open(tname, "x")
                userFile.close()
                userFile = open(tname, "r+")
                userFile.write(userName)
                userFile.close() 
                global passFile
                passFile = open(pname, "x")
                passFile.close()
                passFile = open(pname, "r+")
                passFile.write(pssword)
                passFile.close()
                time.sleep(1)
                os.system('cls')
                a = """
                        ╭━┳━╭━╭━╮╮
                        ┃┈┈┈┣▅╋▅┫┃
                        ┃┈┃┈╰━╰━━━━━━╮
                        ╰┳╯┈┈┈┈┈┈┈┈◢▉◣
                        ╲┃┈┈┈┈┈┈┈┈┈▉▉▉
                        ╲┃┈┈┈┈┈┈┈┈┈◥▉◤
                        ╲┃┈┈┈┈╭━┳━━━━╯
                        ╲┣━━━━━━┫                
                        """
                print(a)
                time.sleep(7)
                os.system('cls')
                print ("This program created by; Phantom")
                time.sleep(2)
                os.system('cls')
                break


def login():
    print("Login")
    print("-----")
    time.sleep(2)
    clear()
    while True:
        name = input("Enter Your Name:").lower()
        os.chdir("users")
        os.chdir(f"{name}")
        infoF = name + "info"
        os.chdir(f"{infoF}")
        rname = name + "usP" + ".txt"
        uname = name + "usN" + ".txt"
        frname = open(rname, "r")
        funame = open(uname, "r")
        os.system('cls')
        cuname = funame.read()
        if name == cuname:
            cpass = frname.read()
            ccpass = input("Enter Your Password Again: ").lower()
            if ccpass == cpass:
                print("Account founded")
                time.sleep(0.5)
                os.system('cls') 
                a = """
                        ╭━┳━╭━╭━╮╮
                        ┃┈┈┈┣▅╋▅┫┃
                        ┃┈┃┈╰━╰━━━━━━╮
                        ╰┳╯┈┈┈┈┈┈┈┈◢▉◣
                        ╲┃┈┈┈┈┈┈┈┈┈▉▉▉
                        ╲┃┈┈┈┈┈┈┈┈┈◥▉◤
                        ╲┃┈┈┈┈╭━┳━━━━╯
                        ╲┣━━━━━━┫                
                        """
                print(a)
                time.sleep(7)
                os.system('cls')
                print ("This program created by; Phantom")
                time.sleep(2)
                os.system('cls')
                break
def dquit():
    print("Thanks for usings this program,program will be executed after 6 seconds")
    time.sleep(3)
    clear()
    time.sleep(1)
    a = """
                        ╭━┳━╭━╭━╮╮
                        ┃┈┈┈┣▅╋▅┫┃
                        ┃┈┃┈╰━╰━━━━━━╮
                        ╰┳╯┈┈┈┈┈┈┈┈◢▉◣
                        ╲┃┈┈┈┈┈┈┈┈┈▉▉▉
                        ╲┃┈┈┈┈┈┈┈┈┈◥▉◤
                        ╲┃┈┈┈┈╭━┳━━━━╯
                        ╲┣━━━━━━┫                
                        """
    print(a)
    time.sleep(7)
    os.system('cls')
    print ("This program created by; Phantom")
    time.sleep(2)
    os.system('cls')
    time.sleep(3)
    os.system('taskkill /f /im code.exe')
main()