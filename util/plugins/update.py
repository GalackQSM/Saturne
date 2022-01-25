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
import os
import shutil
import re
import sys

from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.common import *

def search_for_updates():
    clear()
    setTitle("Saturne Vérification des mises à jour. . .")
    r = requests.get("https://github.com/GalackQSM/Saturne/releases/latest")

    soup = str(BeautifulSoup(r.text, 'html.parser'))
    s1 = re.search('<title>', soup)
    s2 = re.search('·', soup)
    result_string = soup[s1.end():s2.start()]

    if THIS_VERSION not in result_string:
        soup = BeautifulSoup(requests.get("https://github.com/GalackQSM/Saturne/releases").text, 'html.parser')
        for link in soup.find_all('a'):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        new_version = requests.get(update_url)
        setTitle("Saturne - Nouvelle mise à jour trouvée!")
        print(f'''{Fore.YELLOW}
               ███╗   ██╗ ██████╗ ██╗   ██╗██╗   ██╗███████╗██╗     ██╗     ███████╗    ███╗   ███╗ █████╗      ██╗
               ████╗  ██║██╔═══██╗██║   ██║██║   ██║██╔════╝██║     ██║     ██╔════╝    ████╗ ████║██╔══██╗     ██║
               ██╔██╗ ██║██║   ██║██║   ██║██║   ██║█████╗  ██║     ██║     █████╗      ██╔████╔██║███████║     ██║
               ██║╚██╗██║██║   ██║██║   ██║╚██╗ ██╔╝██╔══╝  ██║     ██║     ██╔══╝      ██║╚██╔╝██║██╔══██║██   ██║
               ██║ ╚████║╚██████╔╝╚██████╔╝ ╚████╔╝ ███████╗███████╗███████╗███████╗    ██║ ╚═╝ ██║██║  ██║╚█████╔╝
               ╚═╝  ╚═══╝ ╚═════╝  ╚═════╝   ╚═══╝  ╚══════╝╚══════╝╚══════╝╚══════╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚════╝ 
                              {Fore.RED}La version de Saturne {THIS_VERSION} est obsolète '''.replace('█', f'{Fore.WHITE}█{Fore.RED}'), end="\n\n")
        choice = str(input(
            f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Vous souhaitez mettre à jour vers la dernière version ? (O pour mettre à jour): {Fore.RED}'))

        if choice.upper() == 'O':
            print(f"{Fore.WHITE}\nMise à jour en cours...")
            setTitle(f'Mise à jour de Saturne...')
            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("Saturne.zip", 'wb')as zipfile:
                    zipfile.write(new_version.content)
                with ZipFile("Saturne.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Saturne.zip")
                try:
                    cwd = os.getcwd()+'\\Saturne\\'
                    shutil.copyfile(cwd+'Changelog.md', 'Changelog.md')
                    shutil.copyfile(cwd+os.path.basename(sys.argv[0]), 'Saturne.exe')
                    shutil.copyfile(cwd+'README.md', 'README.md')                   
                    shutil.rmtree('Saturne')
                    setTitle('Saturne Mise à jour terminée!')
                    print(f"{Fore.GREEN}Mise à jour terminée avec succès!")
                    sleep(1)
                    os.startfile("Saturne.exe")
                    sys.exit()
                except PermissionError as err:
                    clear()
                    print(f"{Fore.RED}\nSaturne-{THIS_VERSION} n'a pas assez d'autorisation pour mettre à jour\nessayez de relancer en tant qu'administrateur ou désactivez l'anti-virus sinon essayez de le télécharger manuellement ici {update_url}\n\n\"{err}\"")
                    sleep(10)

            else:
                new_version_soure = requests.get("https://github.com/GalackQSM/Saturne/archive/refs/heads/main.zip")
                with open("Saturne-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_soure.content)
                with ZipFile("Saturne-main.zip", 'r') as filezip:
                    filezip.extractall()
                os.remove("Saturne-main.zip")
                try:
                    cwd = os.getcwd()+'\\Saturne-main'
                    shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                    shutil.rmtree(cwd)
                    setTitle('Mise à jour de Saturne terminée!')
                    print(f"{Fore.GREEN}Mise à jour terminée avec succès!")
                    sleep(1)
                    os.startfile("run.bat")
                    sys.exit()
                except PermissionError as err:
                    clear()
                    print(f"{Fore.RED}\nSaturne-{THIS_VERSION} n'a pas les autorisations suffisantes pour mettre à jour\nessayez de relancer en tant qu'administrateur ou désactivez l'antivirus, sinon essayez de le télécharger manuellement ici {update_url}\n\n\"{err}\"")
                    sleep(10)

        else:
            input
            return