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
import threading

from colorama import Fore

def MassReport(token, guild_id1, channel_id1, message_id1, reason1):
    for i in range(500, 1000):
        while True:
            threading.Thread(target=Report, args=(token, guild_id1, channel_id1, message_id1, reason1)).start()

def Report(token, guild_id1, channel_id1, message_id1, reason1):
    Responses = {
            '401: Unauthorized': f'{Fore.RED}Token Discord invalide.',
            'Missing Access': f'{Fore.RED}Accès manquant au salon ou au serveur.',
            'Vous devez vérifier votre compte pour effectuer cette action.': f'{Fore.RED} Non vérifié.'
    }

    report = requests.post(
        'https://discordapp.com/api/v8/report', json={
            'channel_id': channel_id1,
            'message_id': message_id1,
            'guild_id': guild_id1,
            'reason': reason1
        }, headers={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'sv-SE',
            'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
            'Content-Type': 'application/json',
            'Authorization': token
        }
    )
    
    if (status := report.status_code) == 201:
        print(f"{Fore.GREEN}Rapport envoyé avec succès!\n")
    elif status in (401, 403):
        print(Responses[report.json()['message']]+"\n")
    else:
        print(f"{Fore.RED}Erreur: {report.text} | Code d'état: {status}\n")