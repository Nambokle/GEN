import requests, sys
from capmonster_python import HCaptchaTask
import threading, json
from threading import Thread, Barrier
import random
import tls_client
from colorama import Fore
from concurrent.futures import ThreadPoolExecutor
import time
import random, string
import httpx, sys, ctypes
from colr import color
from datetime import datetime
import os
from json import dumps,loads
from base64 import b64encode
import websocket
import base64
with open('config.json') as config_file:config = json.load(config_file)
solved = 0; genned = 0; errors = 0; genStartTime = time.time()

def TitleWorkerr():
    global genned, solved, errors
    if sys.platform == "linux" or sys.platform == "darwin":
        pass
    else:
        ctypes.windll.kernel32.SetConsoleTitleW(f'Team-Ai | G+ : {genned} | Code : {invite} | E! : {errors} | S+ : {solved} | Speed : {round(genned / ((time.time() - genStartTime) / 60))}/m')

      
class Logger:
    def CenterText(var:str, space:int=None): # From Pycenter
        if not space:
            space = (os.get_terminal_size().columns - len(var.splitlines()[int(len(var.splitlines())/2)])) / 2
        return "\n".join((' ' * int(space)) + var for var in var.splitlines())
    
    def Success(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}]{Fore.LIGHTGREEN_EX} [Success] ({Fore.GREEN}/{Fore.WHITE}) {text}{Fore.LIGHTBLUE_EX})----[Connected To Websocket]--[Javier]')
        lock.release()
    
    def Error(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}]{Fore.RED} [Error..] ({Fore.RED}-{Fore.WHITE}) {text}')
        lock.release()
    
    def Question(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}] ({Fore.YELLOW}?{Fore.WHITE}) {text}')
        lock.release()
    
    def Debug(text):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        lock = threading.Lock()
        lock.acquire()
        print(f'[{current_time}] {Fore.LIGHTMAGENTA_EX} [DEBUGING..] ({Fore.LIGHTBLUE_EX}!{Fore.LIGHTRED_EX}) {text}')
        lock.release()



print(Fore.LIGHTMAGENTA_EX ,f"""

 ______ __    __  ______   ______          ______   ______  __    __ _______   ______  ________ 
|      \  \  /  \/      \ /      \        /      \ /      \|  \  |  \       \ /      \|        \
 \▓▓▓▓▓▓ ▓▓ /  ▓▓  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\      |  ▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓  | ▓▓ ▓▓▓▓▓▓▓\  ▓▓▓▓▓▓\ ▓▓▓▓▓▓▓▓
  | ▓▓ | ▓▓/  ▓▓| ▓▓ __\▓▓ ▓▓__| ▓▓______| ▓▓___\▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓__| ▓▓ ▓▓   \▓▓ ▓▓__    
  | ▓▓ | ▓▓  ▓▓ | ▓▓|    \ ▓▓    ▓▓      \\▓▓    \| ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓    ▓▓ ▓▓     | ▓▓  \   
  | ▓▓ | ▓▓▓▓▓\ | ▓▓ \▓▓▓▓ ▓▓▓▓▓▓▓▓\▓▓▓▓▓▓_\▓▓▓▓▓▓\ ▓▓  | ▓▓ ▓▓  | ▓▓ ▓▓▓▓▓▓▓\ ▓▓   __| ▓▓▓▓▓   
 _| ▓▓_| ▓▓ \▓▓\| ▓▓__| ▓▓ ▓▓  | ▓▓      |  \__| ▓▓ ▓▓__/ ▓▓ ▓▓__/ ▓▓ ▓▓  | ▓▓ ▓▓__/  \ ▓▓_____ 
|   ▓▓ \ ▓▓  \▓▓\\▓▓    ▓▓ ▓▓  | ▓▓       \▓▓    ▓▓\▓▓    ▓▓\▓▓    ▓▓ ▓▓  | ▓▓\▓▓    ▓▓ ▓▓     \
 \▓▓▓▓▓▓\▓▓   \▓▓ \▓▓▓▓▓▓ \▓▓   \▓▓        \▓▓▓▓▓▓  \▓▓▓▓▓▓  \▓▓▓▓▓▓ \▓▓   \▓▓ \▓▓▓▓▓▓ \▓▓▓▓▓▓▓▓
                                                                                                
                                                                                                DISCORD : discord.gg/ikgas
                                                                                                
      
""")
print("https://discord.gg/ikgas")


