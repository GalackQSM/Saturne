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
import Saturne

from time import sleep
from colorama import Fore

from util.plugins.common import print_slow, proxy

def WebhookSpammer(WebHook, Message):
    print_slow("\"ctrl + c\" à tout moment pour arrêter\n")
    sleep(1.5)
    while True:
        response = requests.post(
            WebHook,
            proxies={"http": f'{proxy()}'},
            json = {"content" : Message},
            params = {'wait' : True}
        )
        try:
            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.GREEN}Message envoyé{Fore.RESET}")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Tarif limité ({response.json()['retry_after']}ms){Fore.RESET}")
                sleep(response.json()["retry_after"] / 1000)
            else:
                print(f"{Fore.RED}Erreur : {response.status_code}{Fore.RESET}")

            sleep(.01)
        except KeyboardInterrupt:
            break

    print_slow(f'{Fore.RED}Webhook spammé avec succès!{Fore.RESET} ')
    print("Entrez n'importe quoi pour continuer... ", end="")
    input()
    Saturne.main()