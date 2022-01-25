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

def Info(token):
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
    cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}
    badges = ""

    Discord_Employee = 1
    Partnered_Server_Owner = 2
    HypeSquad_Events = 4
    Bug_Hunter_Level_1 = 8
    House_Bravery = 64
    House_Brilliance = 128
    House_Balance = 256
    Early_Supporter = 512
    Bug_Hunter_Level_2 = 16384
    Early_Verified_Bot_Developer = 131072

    flags = r.json()['flags']
    if (flags == Discord_Employee):
        badges += "Staff, "
    if (flags == Partnered_Server_Owner):
        badges += "Partenaire, "
    if (flags == HypeSquad_Events):
        badges += "Événement Hypesquad, "
    if (flags == Bug_Hunter_Level_1):
        badges += "Bughunter Vert, "
    if (flags == House_Bravery):
        badges += "Hypesquad Bravery, "
    if (flags == House_Brilliance):
        badges += "HypeSquad Brillance, "
    if (flags == House_Balance):
        badges += "HypeSquad Balance, "
    if (flags == Early_Supporter):
        badges += "Early Supporter, "
    if (flags == Bug_Hunter_Level_2):
        badges += "BugHunter Or, "
    if (flags == Early_Verified_Bot_Developer):
        badges += "Développeur de bots vérifié, "
    if (badges == ""):
        badges = "Aucun"

    userName = r.json()['username'] + '#' + r.json()['discriminator']
    userID = r.json()['id']
    phone = r.json()['phone']
    email = r.json()['email']
    language = r.json()['locale']
    mfa = r.json()['mfa_enabled']
    avatar_id = r.json()['avatar']
    has_nitro = False
    res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=getheaders(token))
    nitro_data = res.json()
    has_nitro = bool(len(nitro_data) > 0)
    avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp'
    creation_date = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

    if has_nitro:
        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        days_left = abs((d2 - d1).days)

    billing_info = []
    for x in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=getheaders(token)).json():
        y = x['billing_address']
        name = y['name']
        address_1 = y['line_1']
        address_2 = y['line_2']
        city = y['city']
        postal_code = y['postal_code']
        state = y['state']
        country = y['country']
        if x['type'] == 1:
            cc_brand = x['brand']
            cc_first = cc_digits.get(cc_brand)
            cc_last = x['last_4']
            cc_month = str(x['expires_month'])
            cc_year = str(x['expires_year'])
            data = {
                'Payment Type': 'Carte de crédit',
                'Valide': not x['invalid'],
                'Titulaire': name,
                'Marque CC': cc_brand.title(),
                'Numéro CC': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                'Expiration': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                'Addresse 1': address_1,
                'Addresse 2': address_2 if address_2 else '',
                'Ville': city,
                'Code Postal': postal_code,
                'État': state if state else '',
                'Pays': country,
                'Paiement par défaut': x['default']
            }
        elif x['type'] == 2:
            data = {
                'Payment Type': 'PayPal',
                'Valide': not x['invalid'],
                'Nom PayPal': name,
                'Email Paypal': x['email'],
                'Addresse 1': address_1,
                'Addresse 2': address_2 if address_2 else '',
                'Ville': city,
                'Code Postal': postal_code,
                'État': state if state else '',
                'Pays': country,
                'Paiement par défaut': x['default']
            }
        billing_info.append(data)
        
    print(f'''
    {Fore.RESET}{Fore.GREEN}<<────────────{userName}────────────>>{Fore.RESET}
    [{Fore.RED}ID du membre{Fore.RESET}]    {userID}
    [{Fore.RED}Créé le{Fore.RESET}     ]    {creation_date}
    [{Fore.RED}Langue{Fore.RESET}      ]    {language}
    [{Fore.RED}Badges{Fore.RESET}      ]    {badges}
    [{Fore.RED}Avatar{Fore.RESET}      ]    {avatar_url if avatar_id else "Pas d'avatar"}
    [{Fore.RED}Token{Fore.RESET}       ]    {token}
    {Fore.RESET}{Fore.GREEN}<<───────────Infos de sécurité──────────>>{Fore.RESET}
    [{Fore.RED}2 Facteur{Fore.RESET}   ]    {mfa}
    [{Fore.RED}Email{Fore.RESET}       ]    {email}
    [{Fore.RED}Téléphone{Fore.RESET}   ]    {phone if phone else "Pas de téléphone"}
    {Fore.RESET}{Fore.GREEN}<<────────────Infos nitro───────────────>>{Fore.RESET}
    [{Fore.RED}Satut nitro{Fore.RESET} ]    {has_nitro}
    [{Fore.RED}Expire dans{Fore.RESET} ]    {days_left if has_nitro else "0"} jour(s)
                ''')
    if len(billing_info) > 0:
        print(f"\t\t{Fore.RESET}{Fore.GREEN}<────────────Infos de facturation────────────>{Fore.RESET}")
        if len(billing_info) == 1:
            for x in billing_info:
                for key, val in x.items():
                    if not val:
                        continue
                    print(f"[{Fore.RED}"+'{:<23}{:<10}{}'.format(key+Fore.RED+Fore.RESET+"]", Fore.RESET, val))
        else:
            for i, x in enumerate(billing_info):
                title = f'Mode de paiment #{i + 1} ({x["Payment Type"]})'
                print('' + title)
                print('' + ('=' * len(title)))
                for j, (key, val) in enumerate(x.items()):
                    if not val or j == 0:
                        continue
                    print(f"[{Fore.RED}"+'{:<23}{:<10}{}'.format(key+Fore.RED+Fore.RESET+"]", Fore.RESET, val))
                if i < len(billing_info) - 1:
                    print(f'{Fore.RESET}\n')
        print(f'{Fore.RESET}')
    input(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Entrez n\'importe quoi pour continuer...  {Fore.RED}')
    Saturne.main()