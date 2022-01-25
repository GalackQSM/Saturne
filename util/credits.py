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
from datetime import datetime
from colorama import Fore
from util.plugins.common import getheaders

def Credits(token):
        
    print(f'''

    {Fore.RESET}{Fore.GREEN}Saturne a été crée par GalackQSM{Fore.RESET}
    {Fore.RED}Source de base: Hazard{Fore.RESET}   
    {Fore.BLUE}Source refaite et totalement traduite par GalackQSM{Fore.RESET}    
    {Fore.YELLOW}Github: https://github.com/GalackQSM/Saturne{Fore.RESET}    
    {Fore.RED}Discord: https://discord.com/invite/Saturnetools{Fore.RESET}    

                ''')

    input(f'{Fore.GREEN}[{Fore.YELLOW}>{Fore.GREEN}] {Fore.RESET}Entrez n\'importe quoi pour continuer...  {Fore.RED}')
    Saturne.main()