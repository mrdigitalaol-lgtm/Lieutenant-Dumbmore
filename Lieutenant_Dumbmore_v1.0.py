#Lieutenant Dumbmore v1.0
#By Thom
#An AI Assistant that's false advertising because it actually uses no AI and doesn't assist you in anything.

#imports#
import random
import os
import time
import sys
import datetime
from datetime import datetime
import getpass
#global variables#
quitfunc = ("q")
returntolaunch = ("r")
openclock = ("tell me the time", "what's the time", "whats the time", "open clock")
opencale = ("tell me the date", "what's the date", "whats the date", "open calendar")
opencalc = ("i have a math problem", "open calculator")
opendice = ("roll a die", "roll a dice", "open dice")
openfortune = ("tell me my fortune", "open fortune teller")
openabout = ("who are you", "credits", "open about")
openhelp = ("h")
secretget = ("do what i tell you to")
#global functions#
def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def Quit():
    ClearScreen()
    print ("The program will close in 3 seconds.")
    time.sleep(3)
    sys.exit(0)

def ErrorCode01():
    print ("")
    print ("ERROR 01: USER INPUT NOT VALID")
    print ("")

def ErrorCode02():
    print ("")
    print ("ERROR 02: DIVIDE BY ZERO")
    print ("")
    
def UserInput():
    while True:
        print ("")
        #while True:
        xu = input().lower()
        print ("")
        if xu == quitfunc:
            Quit()
        elif xu in openclock:
            clock()
        elif xu in opencale:
            calendar()
        elif xu in opencalc:
            calculator()
        elif xu in opendice:
            dice()
        elif xu in openfortune:
            fortune_teller()
        elif xu in openabout:
            about()
        elif xu == secretget:
            secret()
        elif xu == openhelp:
            help()
        else:
            ErrorCode01()

def launch():
    ClearScreen()
    print ("HELLO. I AM LIEUTENANT DUMBMORE.")
    UserInput()

def EnterInput():
    print ("")
    xe = getpass.getpass("CLick Enter to return...")
    launch()
     
def start():
    print ("Welcome to Lieutenant Dumbmore,\nthe first assistant product since ~2016 that uses no AI at all.")
    print ("")
    print ("Input 'help' to view the list of all possible commands.")
    xs = getpass.getpass("Click Enter to launch Lieutenant Dumbmore...")
    launch()

def about():
    ClearScreen()
    print ("Lieutenant Dumbmore v1.0")
    print ("Created and developed by Thom Addeo.")
    print ("Coded in Python.")
    print ("2026")
    EnterInput()

def help():
    ClearScreen()
    print ("I CAN DO MANY THINGS!")
    print ("\033[3m(Please note that all actions and program names must have\nthe Enter key used after in order for the command to be read.)\033[3m")
    print ("")
    print ("*Actions*")
    print ("'Q' - quits Commander Dumbmore")
    print ("'R' - returns to launch screen")
    print ("*Applications*")
    print ("'Tell me the time', 'What's the time', 'Open Clock' - opens Clock")
    print ("'Tell me the date', 'What's the date', 'Open Calendar' - opens Calendar")
    print ("'I have a math problem', 'Open Calculator' - opens Calculator")
    print ("'Roll a die', 'Open Dice' - opens Dice")
    print ("'Tell me my fortune', 'Open Fortune Teller' - opens Fortune Teller")
    print ("'Who are you', 'Credits', 'Open About' - opens About")
    EnterInput()

def clock():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print ("THE TIME IS ", current_time)
    EnterInput()

def calendar():
    date = datetime.today().strftime("%d-%m-%y")
    print ("THE DATE IS " + date)
    EnterInput()

def calculator():
    ClearScreen()
    add = ("addition", "add", "plus", "+")
    minu = ("subtraction", "subtract", "minus", "-")
    mul = ("multiplication", "times", "multiply", "*")
    div = ("division", "divide", "divided by", "/")
    while True:
        print ("")
        print ("WHAT IS YOUR DESIRED OPERATION?")
        print ("(Addition, Subtraction, Multiplication, Division)")
        print ("")
        xc = input().lower()
        print ("")      
        if xc in add:
            print ("WHAT IS YOUR FIRST INTEGER?")
            print ("")
            yc = int(input())
            print ("")
            print ("WHAT IS YOUR SECOND INTEGER?")
            print ("")
            zc = int(input())
            addresult = yc + zc
            print ("")
            print ("{yc} + {zc} = ", + addresult)
        elif xc in minu:
            print ("WHAT IS YOUR FIRST INTEGER?")
            print ("")
            wc = int(input())
            print ("")
            print ("WHAT IS YOUR SECOND INTEGER?")
            print ("")
            vc = int(input())
            minuresult = wc - vc
            print ("")
            print ("{yc} - {zc} = ", + minuresult)
        elif xc in mul:
            print ("WHAT IS YOUR FIRST INTEGER?")
            print ("")
            uc = int(input())
            print ("")
            print ("WHAT IS YOUR SECOND INTEGER?")
            print ("")
            tc = int(input())
            mulresult = uc * tc
            print ("")
            print ("{uc} * {tc} = ", + mulresult)
        elif xc in div:
            print ("WHAT IS YOUR FIRST INTEGER?")
            print ("")
            sc = int(input())
            print ("")
            print ("WHAT IS YOUR SECOND INTEGER?")
            print ("")
            rc = int(input())
            try:
                divresult = sc / rc
            except ZeroDivisionError:
                divresult = ErrorCode02()
            print ("{sc} / {rc} = ", divresult)
        elif xc == quitfunc:
            Quit()
        elif xc == returntolaunch:
            launch()
        else:
            ErrorCode01()

def dice():
    ClearScreen()
    d6 = ("d6")
    d10 = ("d10")
    d20 = ("d20")
    d6n = [1,2,3,4,5,6]
    d10n = [1,2,3,4,5,6,7,8,9,10]
    d20n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    while True:
        d6r = random.choice(d6n)
        d10r = random.choice(d10n)
        d20r = random.choice(d20n)
        print ("SELECT AN OPTION")
        print ("- d6")
        print ("- d10")
        print ("- d20")
        print ("")
        xd = input().lower()
        print ("")
        if xd == d6:
            print ("YOU ROLLED A ", d6r)
            print ("")
        elif xd == d10:
            print ("YOU ROLLED A ", d10r)
            print ("")
        elif xd == d20:
            print ("YOU ROLLED A ", d20r)
            print ("")
        elif xd == quitfunc:
            Quit()
        elif xd == returntolaunch:
            launch()
        else:
            ErrorCode01()

def fortune_teller():
    ClearScreen()
    fc = ("fortune cookie", "Fortune cookie", "Fortune Cookie", "fortune Cookie")
    start1 = ["GRAND ", "MINUT ", "NO "]
    middle1 = ["LUCK ", "CURSES ", "HAPPINESS "]
    end1 = ["WILL COME SOON.", "WILL NOT COME SOON."]
    start1select = random.choice(start1)
    middle1select = random.choice(middle1)
    end1select = random.choice(end1)
    set1 = [start1select + middle1select + end1select]
    m8 = ("magic 8 ball", "Magic 8 ball", "magic 8 Ball", "Magic 8 Ball")
    responses = [
        "IT IS CERTAIN", "IT IS DECIDEDLY SO", "WITHOUT A DOUBT",
        "YES, DEFINITELY", "YOU MAY RELY ON IT", "AS I SEE IT, YES",
        "MOST LIKELY", "OUTLOOK GOOD", "YES",
        "SIGNS POINT TO YES", "REPLY HAZY, TRY AGAIN", "ASK AGAIN LATER",
        "BETTER NOT TELL YOU NOW", "CANNOT PREDICT NOW", "CONCENTRATE AND TRY AGAIN",
        "DON'T COUNT ON IT", "MY REPLY IS NO", "OUTLOOK NOT SO GOOD",
        "VERY DOUBTFUL", "NO", "NOT LIKELY",
        "SIGNS POINT TO NO", "NO, DEFINITELY NOT", "MY SOURCES SAY NO",
        "I DON'T THINK I CAN TELL YOU", "AS I SEE IT, NO"
        ]
    respond = random.choice(responses)
    while True:
        start1select = random.choice(start1)
        middle1select = random.choice(middle1)
        end1select = random.choice(end1)
        set1 = [start1select + middle1select + end1select]
        respond = random.choice(responses)
        print ("SELECT AN OPTION.")
        print ("- Fortune Cookie")
        print ("")
        print ("- Magic 8 Ball")
        print ("")
        xf = input().lower()
        print ("")
        if xf in fc:
            print (set1)
            print ("")
        elif xf in m8:
            print ("")
            print ("WHAT IS YOUR QUESTION?")
            print ("")
            yf = input().lower()
            print ("")
            print (respond)
            print ("")
        elif xf or yf == quitfunc:
            Quit()
        elif xf or yf == returntolaunch:
            launch()   
        else:
            ErrorCode01()

def secret():
    print ("")
    print ("I'M SORRY, DAVE. I'M AFRAID I CAN'T DO THAT.")
    print ("")
    UserInput()
    
#setup#
start()

