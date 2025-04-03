#Harmony editor component dev build 4
#Copyright EyeScary Development
#Uses some code from Stronge by EyeScary Development
#Modified by Pittab first on 13.2.25 to make Cobblestone, an notes app

#Imports
import os
import sys
import lead_md as lead
import menu
from typing import (List, Any)
import readline
from settings import checksetting
from consts import PLATFORM

#variables
lines=[]
filename=...
extension=...

#functions

#opens the file
def openfile(filename):
    global lines
    with open(filename, "r") as file:
        lines=file.readlines()

#prints out the file and judges wether syntax highlighing is needed
def printfile(extension, tofind=...):
   global settings
   global filename
   global lines
   try:
        openfile(filename)
        cleaned=[line.strip() for line in lines]
   except FileNotFoundError:
       print(end="")
   else:
      linenum=1
      lead.render(cleaned)

#deletes a line
def removeLine(linenum):
    global lines
    linenum=int(linenum)-1
    lines.pop(linenum)

#replaces a line
def replaceLine(linenum):
    global lines
    linenum-=1
    readline.set_startup_hook(lambda: readline.insert_text(lines[linenum].strip("\n")))
    try:
        user_input = input("make edits to this line: ")
    finally:
        readline.set_startup_hook()
    lines[linenum]=user_input+'\n'

#inserts a line
def insertLine(linenum, input_list: List[Any]):
    global lines
    linenum-=1
    input_list.pop(0)
    lines.insert(linenum, ' '.join(input_list)+'\n')

#replace function
def replace(input_list: List[Any]):
    global lines
    torep=input_list[0]
    input_list.pop(0)
    for i, item in enumerate(lines):
        words = item.split()
        for j, word in enumerate(words):
            if word == torep:
                words[j] = ' '.join(input_list)
        lines[i] = ' '.join(words)+'\n'

#handles commands
def commands(userInput: str):
    global lines
    global filename
    command = userInput.split()[0]
    try:
        match command:
            case ":sf":
                write(lines, filename)
                name = input("change to what file name? | ")
                if name.startswith("."):
                    filename=name
                    extension="except"
                elif "." in name:
                    extension = "." + name.split(".")[1]
                    filename = name
                else:
                    extension = input("what extension? |  ")
                    if not extension.startswith("."):
                        extension = "." + extension
                        filename = name + extension
                openfile(filename)
            case ":q" | ":x" | ":exit":
                os.system("cls" if os.name == "nt" else "clear")
                return True
            case ":dl":
                removeLine(userInput.split()[1])
            case ":edln":
                listtoinput=userInput.split()
                listtoinput.pop(0)
                replaceLine(int(listtoinput[0]))
            case ':rp':
                listtoinput=userInput.split()
                listtoinput.pop(0)
                replace(listtoinput)
            case ":in":
                listtoinput=userInput.split()
                listtoinput.pop(0)
                insertLine(int(listtoinput[0]), listtoinput)
            case ":rn":
                coderun(extension)
            case ":fnd":
                os.system("cls" if os.name == "nt" else "clear")
                printfile(extension, userInput.split()[1])
                input('press enter to continue: ')
    except IndexError:
        print("invalid command")
        input("press enter to continue: ")

#writes to the file
def write(filename):
    global lines
    with open(filename, "w") as file:
            for item in lines:
                file.write(item)

#editor function
def editor():
    global filename, extension, lines
    os.system("cls" if os.name == "nt" else "clear")
    printfile(extension)
    userInput=input("|")
    if userInput.startswith(":"):
        if commands(userInput.strip()):
            return True
    else:
        lines.append(userInput+'\n')
    write(filename)

#main function
def main():
    global filename, extension
    if checksetting(1):
        print("here is a list of notes in the current directory:")
        if PLATFORM == "Windows":
            os.system("dir *.md")
        else:
            os.system('ls *.md')
    name=input("what is the name of the note you wish to edit?: ")
    extension=".md"
    filename=name+extension
    try:
        openfile(filename)
    except FileNotFoundError:
        lines=[]
    while True:
        if editor():
            break
    menu.main()

if __name__ == "__main__":
    main()
