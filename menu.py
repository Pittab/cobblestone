#Cobblestone, a Pittab project based on:
#Harmony code editor dev build 4
#Copyright EyeScary Development
#Uses some code from Stronge by EyeScary Development

import editor
import os
import settings
def main():
    print("Welcome to Cobblestone, the new notetaking app from Pittab, would you like to:\n(e)dit a note\ngo to (s)ettings\nor (q)uit?")
    selection=input("| ")
    if selection=="e":
        os.system("cls" if os.name == "nt" else "clear")
        editor.main()
    elif selection=="s":
        os.system("cls" if os.name == "nt" else "clear")
        settings.main()
    else:
        quit()

if __name__ == "__main__":
    main()
