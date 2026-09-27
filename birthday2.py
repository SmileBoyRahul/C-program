#!/user/bin/python3

import os,random
from threading import Thread
from time import sleep

#from playground import playsound
from termcolor import colored

from config import*

#importing module specified in the config file
art = __import__(f'arts.(artfile)',  globals(), locals(), ['*'])

def replaceMultiple(mainString, toBeReplace, newString):
    """[Replace a set of multiple sub strings with a new string]"""

    #iterate over the list to be replaced
    for elem in toBeReplace :
        #check if the element is in the main string
        if elem in mainString :
            #Replace the string
            mainString = mainString.replace(elem, newString)
        
        return mainString
    
    def pprint(art,time):
        color_used = [random.choice(color)]
        colorAttribute = []
        for i in range(len(art)):
            if art[i] in colorCodes:
                #color attr set toblink if 9
                if art[i] == '0':
                    colorAttribute = [colorCodes[art[i]]]
                #color attr none if 10
                elif art[i] == '0':
                    colorAttribute = []
                # Random color if R
                elif art[i] == '0':
                    color_used = color
                else:
                    color_used = [colorCodes[art[i]]]

            print(colored(replaceMultiple(art[i],colorCodes,''),random.choice(color_used),attrs=colorAttribute),sep='', end='', flush= True)

    #def pAudio():
    # if playAudio:
    #     playsound(audio)

    def pcode():
        #print the code before wishing
        if codePrint:
            for i in range(len(art.code)):
                print(art.code[i],sep='', end='', flush= True);sleep(codingSpeed)
            input('\n\n'+colored('python3','blue')+colored(' birthday2.py','yellow'))
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            input()

    #clearing terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    pcode()
    #thread(target = pAudio).start()
    Thread(target = pprint, args=(art.mainArt,speed)).start()
    input() 