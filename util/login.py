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
from selenium import webdriver
from colorama import Fore, Back

from util.plugins.common import get_driver, getheaders

def TokenLogin(token):
    j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
    user = j["username"] + "#" + str(j["discriminator"])
    script = """
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
            location.reload();
        """ % (token)
    type_ = get_driver()

    if type_ == "chromedriver.exe":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)
    # elif type_ == "operadriver.exe":
    #     opts = webdriver.opera.options.ChromeOptions()
    #     opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    #     opts.add_experimental_option("detach", True)
    #     driver = webdriver.Opera(options=opts)
    elif type_ == "msedgedriver.exe":
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=opts)
    else:
        print(f'{Fore.RESET}[{Fore.RED}Erreur{Fore.RESET}] : Impossible de trouver un pilote pour automatiser le processus de connexion à {user}')
        sleep(3)
        print(f"{Fore.YELLOW}Collez ce script dans la console d'un navigateur:{Fore.RESET}\n\n{Back.RED}{script}\n{Back.RESET}")
        print("Entrez n'importe quoi pour continuer... ", end="")
        input()
        Saturne.main()

    print(f"{Fore.GREEN}Connexion sur le compte de {Fore.BLUE}{user}")
    driver.get("https://discordapp.com/login")
    driver.execute_script(script)
    Saturne.main()