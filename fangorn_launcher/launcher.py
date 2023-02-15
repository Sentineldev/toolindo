import subprocess
import os
import json
from threading import Thread


    
def OpenApp(wamp_directory):
    subprocess.call([wamp_directory])


def runCmd(command):
    os.system(command)

def load_json():
    try:
        f = open('instructions.json')
        instructions = json.load(f)
        f.close()
        return instructions
    except:
        print("File not found!")
def execute_instructions(wamp_directory,command):
    try:
        Thread(target=OpenApp,args=(wamp_directory,)).start()
        Thread(target=runCmd,args=(command,)).start()  
    except Exception as e:
        print(e)
        print("There has been an error.")
def main():


    instructions = load_json()
    command = instructions['command']
    wamp_directory = instructions['app_directory']

    execute_instructions(wamp_directory, command)

if __name__ == "__main__":
    main()