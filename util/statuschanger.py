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
from colorama import Fore

from util.plugins.common import print_slow, getheaders, proxy

def StatusChanger(token, Status):
    CustomStatus = {"custom_status": {"text": Status}} #{"text": Status, "emoji_name": "☢"} if you want to add an emoji to the status
    try:
        requests.patch("https://discord.com/api/v9/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=CustomStatus)
        print_slow(f"\n{Fore.GREEN}Statut changer avec succès en {Fore.WHITE}{Status}{Fore.GREEN} ")
    except Exception as e:
        print(f"{Fore.RED}Erreur:\n{e}\nS'est produit lors de la tentative de modification de l'état :/")
    print("Entrez n'importe quoi pour continuer. . . ", end="")
    input()
    Saturne.main()