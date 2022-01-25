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
import random
import Saturne

from time import sleep
from colorama import Fore

from util.plugins.common import print_slow, setTitle, getheaders, proxy

def selector(token, users):
    while True:
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.RED}Chat de groupe créé")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Tarif limité ({response.json()['retry_after']}ms){Fore.RESET}")
            else:
                print(f"{Fore.RED}Erreur: {response.status_code}{Fore.RESET}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    Saturne.main()

def randomizer(token, ID):
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.RED}Chat de groupe créé")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Tarif limité ({response.json()['retry_after']}ms){Fore.RESET}")
            else:
                print(f"{Fore.RED}Erreur: {response.status_code}{Fore.RESET}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    Saturne.main()


def GcSpammer(token):
    print(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Voulez-vous choisir vous-même le ou les utilisateurs pour grouper les spams de chat ou voulez-vous sélectionner des utilisateurs aléatoires?')
    sleep(1)
    print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] choisissez vous-même les utilisateurs
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Utilisateurs aléatoires
                        ''')
    secondchoice = int(input(
        f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Deuxième choix: {Fore.RED}'))

    if secondchoice not in [1, 2]:
        print(f'{Fore.RESET}[{Fore.RED}Erreur{Fore.RESET}] : Deuxième choix invalide')
        sleep(1)
        Saturne.main()

    if secondchoice == 1:
        setTitle(f"Créer des discussions de groupe")
        recipients = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Entrez les utilisateurs avec lesquels vous souhaitez créer un groupe de discussion (séparez par , id,id2,id3): {Fore.RED}')
        user = recipients.split(',')
        if "," not in recipients:
            print(f"\n{Fore.RED}Vous n'aviez pas de virgule (,) le format est id,id2,id3")
            sleep(3)
            Saturne.main()
        print_slow("\"ctrl + c\" à tout moment pour arrêter\n")
        sleep(1.5)
        selector(token, user)

    elif secondchoice == 2:
        setTitle(f"Créer des discussions de groupe")
        IDs = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'http://{proxy()}'}, headers=getheaders(token)).json()
        for friend in friendIds:
            IDs.append(friend['id'])
        print_slow("\"ctrl + c\" à tout moment pour arrêter\n")
        sleep(1.5)
        randomizer(token, IDs)