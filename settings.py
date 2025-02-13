import menu
import os

#where all temp setting data is stored
settings=[]

#loads the setting data into the list
def loadsettings():
    global settings
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'settings.escnf')
    with open(file_path, 'r') as file:
        for line in file:
            settings.append(line.strip())

#checks the value of a setting
def checksetting(setting):
    global settings
    loadsettings()
    if settings[setting] == "1":
        return True
    else:
        return False

#the home menu for settings
def main():
    loadsettings()
    print("Welcome to Settings, would you like to:\n(e)dit a setting\nread (a)bout your Harmony installation\nor go to (m)enu?")
    selection=input("| ")
    if selection=="s":
        editsetting()
    elif selection=="a":
        about()
    elif selection=="e":
        editsetting()
    else:
        menu.main()
        
if __name__ == "__main__":
    main()

#writes settings to the config file
def writesettings():
    global settings
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'settings.escnf')
    with open(file_path, 'w') as file:
        file.seek(0)
        for item in settings:
            file.write(item+'\n')

#edits the value of a setting
def editsetting():
    global settings
    toedit = int(input('what setting would you like to edit? (1 - syntax highlighting, 2 - show files in current directory when opening editor (more coming soon)): '))
    toedit -= 1
    setto = input("what would you like to set that to? (1 - on, 0 - off): ")
    settings.pop(toedit)
    settings.insert(toedit, setto)
    writesettings()
    main()

#displays info about the build of Harmony
def about():
    print("Harmony code editor (stronge-harmony) version 0.3\nCopyright EyeScary Development Studios 2024")
    main()
