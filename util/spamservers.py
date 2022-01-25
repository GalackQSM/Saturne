###############################################################
# ███████╗ █████╗ ████████╗██╗   ██╗██████╗ ███╗   ██╗███████╗
# ██╔════╝██╔══██╗╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██╔════╝
# ███████╗███████║   ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗  
# ╚════██║██╔══██║   ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝  
# ███████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗
# ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
###############################################################
# Crée par GalackQSM
# Github: https://github.com/GalackQSM/Saturne
# Discord: https://discord.gg/saturnetools|XvjJpw4D3m
# © 2022 Saturne
###############################################################

import requests

from colorama import Fore

from util.plugins.common import getheaders, proxy, random_chinese

def SpamServers(token, icon, name=None):
    if name:
        for i in range(4):
            try:
                payload = {'name': f'{name}', 'region': 'europe', 'icon': icon, 'channels': None}
                requests.post('https://discord.com/api/v7/guilds', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=payload)
                print(f"{Fore.BLUE}Serveur crée {name}.{Fore.RESET}")
            except Exception as e:
                print(f"L'exception suivante a été rencontrée et est ignorée: {e}")
    for i in range(4):
        server_name = random_chinese(5,12)
        try:
            payload = {'name': f'{server_name}', 'region': 'europe', 'icon': icon , 'channels': None}
            requests.post('https://discord.com/api/v7/guilds', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=payload)
            print(f"{Fore.BLUE}Serveur crée {server_name}.{Fore.RESET}")
        except Exception as e:
            print(f"L'exception suivante a été rencontrée et est ignorée: {e}")