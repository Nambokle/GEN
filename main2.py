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

print(Fore.LIGHTYELLOW_EX ,f"""Invite-Code
""")
              

invite = input(Fore.LIGHTCYAN_EX  + 'Invite -> ')

def GetUsername():
    type = config['username']
    
    if type == "real":
        usernames = open("usernames.txt", encoding="utf-8").read().splitlines()
        return random.choice(usernames)
    
    
    
class Utils(object):
    @staticmethod
    def GenerateBornDate():
        year=str(random.randint(1997,2001));month=str(random.randint(1,12));day=str(random.randint(1,28))
        if len(month)==1:month='0'+month
        if len(day)==1:day='0'+day
        return year+'-'+month+'-'+day

websiteKey = "4c672d35-0701-42b2-88c3-78380b0db560"
websiteUrl = "https://discord.com/"
useragent = "Mozilla/5.0 (Windows NT 6.0; rv:40.0) Gecko/20100101 Firefox/40.0"




def init(proxy):
        global solved
        started_on = time.time()
        captcha_key = Solvers.hCaptcha('4c672d35-0701-42b2-88c3-78380b0db560', 'https://discord.com/', None)
        if "P1_" in captcha_key:
            solved += 1
            TitleWorkerr()
            Logger.Debug(f"Solved hCaptcha : {captcha_key[:32]}... ({round(time.time() - started_on)} s)")
            return captcha_key
        else:
            return False
class Solvers:
    @staticmethod
    def hCaptcha(websiteKey, websiteUrl, UserAgent):
           solvedCaptcha = None
           taskId = ""
           captchaKey = config["captchaKey"]

           taskId = httpx.post(f"https://api.capmonster.cloud/createTask", json={"clientKey": captchaKey, "task": { "type": "HCaptchaTaskProxyless",  "websiteURL": websiteUrl, "websiteKey": websiteKey }}, timeout=30).json()
           if taskId.get("errorId") > 0:
                print(f"{Fore.RED}[-] Error While Creating Task - {taskId.get('errorDescription')}!")

           taskId = taskId.get("taskId")
            
           while not solvedCaptcha:
                    captchaData = httpx.post(f"https://api.capmonster.cloud/getTaskResult", json={"clientKey": captchaKey, "taskId": taskId}, timeout=30).json()
                    if captchaData.get("status") == "ready":
                        solvedCaptcha = captchaData.get("solution").get("gRecaptchaResponse")
                        return solvedCaptcha



def joiner():
    session = tls_client.Session(client_identifier='chrome_112')
    request_url = "https://discord.com/api/v9/experiments"
    r = session.get(request_url)
    fingerprint = "1071861684764938290.LF9Okx-1071881013329932308.016nW7dhymgXw5CWh41HSkoDMH8"
    proxy = random.choice(open('proxies.txt','r').readlines())
    proxy = str(proxy).strip('\n').replace(' ','')
    key = init(proxy)
    name = GetUsername()
    email = "{}@gmail.com".format(''.join(random.choice(string.ascii_lowercase) for _ in range(8)))
    global genned, solved, errors
    try:
        r = session.post('https://discord.com/api/v9/auth/register',json={  
            'fingerprint': fingerprint,
            'email': email,
            'username': str(name),
            'password': "Tunable123$$$", 
            'invite': invite,
            'consent': True,
            'date_of_birth': Utils.GenerateBornDate(),
            'bio': ".gg/97op", 
            'gift_code_sku_id': None,
            "captcha_key": str(key), 
            "promotional_email_opt_in": True

        },headers = {
                'Host': 'discord.com',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
                'Accept': '*/*',
                'Accept-Language': 'en-US,en;q=0.5',
                'Accept-Encoding': 'gzip, deflate, br',
                'Content-Type': 'application/json',
                'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwOC4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwOC4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA4LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTY1NDg1LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
                'X-Fingerprint': fingerprint,
                'X-Discord-Locale': 'en-US',
                'X-Debug-Options': 'bugReporterEnabled',
                'Origin': 'https://discord.com',
                'Alt-Used': 'discord.com',
                'Connection': 'keep-alive',
                'Referer': f'https://discord.com/invite{invite}',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'dnt': '1',
                'TE': 'trailers'
        }, proxy=f'http://{proxy}'
        )
        if r.status_code == 201:
            token = r.json()['token']
            Logger.Success(f"{Fore.LIGHTCYAN_EX}Created : {token[:32]+'*************'}")
            genned = genned + 1
            file = open(f'output/{invite}.txt', 'a')
            file.write(f'{token}\n')
            TitleWorkerr()

        else:
            TitleWorkerr()
            if 'captcha' in r.text:
                errors = errors + 1
                Logger.Error('Submit Was Rejected')
            else:
                errors = errors + 1
                Logger.Error(r.json())
    except Exception as e:
        TitleWorkerr()
        errors = errors + 1
        Logger.Error(e)

def start_thread():
    while True:
            joiner()

for i in range(100):
    threading.Thread(target=start_thread).start()
