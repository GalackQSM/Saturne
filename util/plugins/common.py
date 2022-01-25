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

import os
import re
import io
import sys
import time
import json
import ctypes
import random
import zipfile
import requests
import pkg_resources
import subprocess
import threading

from distutils.version import LooseVersion
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from colorama import Fore
from time import sleep

THIS_VERSION = "1.0.1"
TARGET_VERSION = 0

class Chrome_Installer(object):
    installed = False
    target_version = None
    DL_BASE = "https://chromedriver.storage.googleapis.com/"

    def __init__(self, executable_path=None, target_version=None, *args, **kwargs):
        self.platform = sys.platform

        if TARGET_VERSION:
            self.target_version = TARGET_VERSION

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]

        self._base = base_ = "chromedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = base_.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            self.fetch_chromedriver()
            if not self.__class__.installed:
                if self.patch_binary():
                    self.__class__.installed = True

    @staticmethod
    def random_cdc():
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open(self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect


    def get_release_version_number(self):
        path = (
            "LATEST_RELEASE"
            if not self.target_version
            else f"LATEST_RELEASE_{self.target_version}"
        )
        return LooseVersion(urlopen(self.__class__.DL_BASE + path).read().decode())

    def fetch_chromedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        urlretrieve(
            f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
            filename=zip_name,
        )
        with zipfile.ZipFile(zip_name) as zf:
            zf.extract(self._exe_name)
        os.remove(zip_name)
        if sys.platform != "win32":
            os.chmod(self._exe_name, 0o755)
        return self._exe_name

class Edge_Installer(object):
    installed = False
    target_version = None
    DL_BASE = "https://msedgedriver.azureedge.net/"

    def __init__(self, executable_path=None, target_version=None, *args, **kwargs):
        self.platform = sys.platform

        if TARGET_VERSION:
            self.target_version = TARGET_VERSION

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]

        self._base = base_ = "edgedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = base_.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            self.fetch_edgedriver()
            if not self.__class__.installed:
                if self.patch_binary():
                    self.__class__.installed = True

    @staticmethod
    def random_cdc():
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open("ms"+self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect


    def get_release_version_number(self):
        path = (
            "LATEST_STABLE"
            if not self.target_version
            else f"LATEST_RELEASE_{str(self.target_version).split('.', 1)[0]}"
        )
        urlretrieve(
            f"{self.__class__.DL_BASE}{path}",
            filename=f"{os.getenv('temp')}\\{path}",
        )
        with open(f"{os.getenv('temp')}\\{path}", "r+") as f:
            _file = f.read().strip("\n")
            content = ""
            for char in [x for x in _file]:
                for num in ("0","1","2","3","4","5","6","7","8","9","."):
                    if char == num:
                        content += char
        return LooseVersion(content)

    def fetch_edgedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        print(f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip")
        urlretrieve(
            f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
            filename=zip_name,
        )
        with zipfile.ZipFile(zip_name) as zf:
            zf.extract("ms"+self._exe_name)
        os.remove(zip_name)
        if sys.platform != "win32":
            os.chmod(self._exe_name, 0o755)
        return self._exe_name

class Opera_Installer(object):
    _os_bit = 64
    def __init__(self, *args, **kwargs):
        if os.environ.get('PROCESSOR_ARCHITECTURE').lower() == 'x86' and os.environ.get('PROCESSOR_ARCHITEW6432') is None: 
            self.__class__._os_bit = 32
            
        r = requests.get("https://github.com/operasoftware/operachromiumdriver/releases")
        soup = str(BeautifulSoup(r.text, 'html.parser'))
        print(soup.get_text())

def get_driver():
    drivers = ["chromedriver.exe", "msedgedriver.exe"] 

    print(f"\n{Fore.BLUE}Vérification du pilote...")
    sleep(0.5)

    for driver in drivers:
        if os.path.exists(os.getcwd() + os.sep + driver):
            print(f"{Fore.GREEN}{driver} existe déjà, patienter...{Fore.RESET}")
            sleep(0.5)
            return driver
    else:
        print(f"{Fore.RED}Pilote introuvable! je l'installe pour vous")
        if os.path.exists(os.getenv('localappdata') + '\\Google'):
            Chrome_Installer()
            print(f"{Fore.GREEN}chromedriver.exe installé!{Fore.RESET}")
            return "chromedriver.exe"
        # elif os.path.exists(os.getenv('appdata') + '\\Opera Software\\Opera Stable'):
            # Opera_Installer()
            #print(f"{Fore.GREEN}operadriver.exe Installed!{Fore.RESET}")
            # return "operadriver.exe"
        elif os.path.exists(os.getenv('localappdata') + '\\Microsoft\\Edge'):
            Edge_Installer()
            print(f"{Fore.GREEN}msedgedriver.exe installé!{Fore.RESET}")
            return "msedgedriver.exe"
        else:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Aucun pilote compatible trouvé... Continuer avec chromedriver')
            Chrome_Installer()
            print(f"{Fore.GREEN}essayer d'installer chromedriver.exe{Fore.RESET}")
            return "chromedriver.exe"

def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def setTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | Crée par GalackQSM")
    elif system == 'posix':
        os.system(f"\033]0;{_str} | Crée par GalackQSM\a", end='', flush=True)
    else:
        pass

def random_chinese(amount, second_amount):
    name = u''
    for i in range(random.randint(amount, second_amount)):
        name = name + chr(random.randint(0x4E00,0x8000))
    return name

def print_slow(_str):
    for letter in _str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.04)

def install_lib(dependencies):
    installed_packages = sorted([i.key for i in pkg_resources.working_set])
    for lib in dependencies:
        if lib not in installed_packages:
            print(f"{Fore.BLUE}{lib}{Fore.RED} pas trouvé! je l'install pour vous...{Fore.RESET}")
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
            except Exception as e:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : {e}')
                sleep(0.5)
                pass

def validateToken(token):
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
    if r.status_code == 200:
        pass
    else:
        print(f"\n{Fore.RED}Token invalide.{Fore.RESET}")
        sleep(1)
        __import__("Saturne").main()

def validateWebhook(hook):
    try:
        responce = requests.get(hook)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
        print(f"\n{Fore.RED}Webhook non valide.{Fore.RESET}")
        sleep(1)
        __import__("Saturne").main()
    try:
        j = responce.json()["name"]
    except (KeyError, json.decoder.JSONDecodeError):
        print(f"\n{Fore.RED}Invalid Webhook.{Fore.RESET}")
        sleep(1)
        __import__("Saturne").main()
    print(f"{Fore.GREEN}Webhook valide! ({j})")

def proxy_scrape(): 
    proxieslog = []
    setTitle("Recherche de proxies")
    startTime = time.time()
    temp = os.getenv("temp")+"\\saturne_proxies"
    print(f"{Fore.YELLOW}Veuillez patienter pendant que Saturne supprime les proxys pour vous!{Fore.RESET}")

    def fetchProxies(url, custom_regex):
        global proxylist
        try:
            proxylist = requests.get(url, timeout=5).text
        except Exception:
            pass
        finally:
            proxylist = proxylist.replace('null', '')
        custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
        custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
        for proxy in re.findall(re.compile(custom_regex), proxylist):
            proxieslog.append(f"{proxy[0]}:{proxy[1]}")

    proxysources = [
        ["http://spys.me/proxy.txt","%ip%:%port% "],
        ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
        ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
        ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
        ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
        ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt", '%ip%", "type": "http", "port": %port%'],
        ["https://www.us-proxy.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://free-proxy-list.net/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://www.sslproxies.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
        ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
        ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
        ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",']
    ]
    threads = [] 
    for url in proxysources:
        t = threading.Thread(target=fetchProxies, args=(url[0], url[1]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    proxies = list(set(proxieslog))
    with open(temp, "w") as f:
        for proxy in proxies:
            for i in range(random.randint(7, 10)):
                f.write(f"{proxy}\n")
    execution_time = (time.time() - startTime)
    print(f"{Fore.GREEN}Nous avons trouvé{Fore.MAGENTA}{len(proxies): >5}{Fore.GREEN} proxies totales => {Fore.RED}{temp}{Fore.RESET} | {execution_time}ms")
    setTitle(f"Saturne {THIS_VERSION}")

def proxy():
    temp = os.getenv("temp")+"\\saturne_proxies"
    if os.stat(temp).st_size == 0:
        proxy_scrape()
    proxies = open(temp).read().split('\n')
    proxy = proxies[0]

    with open(temp, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])
    return proxy

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

def blackwhite(text):
    os.system(""); faded = ""
    red = 0; green = 0; blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 20; green += 20; blue += 20
            if red > 255 and green > 255 and blue > 255:
                red = 255; green = 255; blue = 255
    return faded

def purplepink(text):
    os.system(""); faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

def greenblue(text):
    os.system(""); faded = ""
    blue = 100
    for line in text.splitlines():
        faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
        if not blue == 255:
            blue += 15
            if blue > 255:
                blue = 255
    return faded

def pinkred(text):
    os.system(""); faded = ""
    blue = 255
    for line in text.splitlines():
        faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m\n")
        if not blue == 0:
            blue -= 20
            if blue < 0:
                blue = 0
    return faded

def purpleblue(text):
    os.system(""); faded = ""
    red = 110
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;255m{line}\033[0m\n")
        if not red == 0:
            red -= 15
            if red < 0:
                red = 0
    return faded

def water(text):
    os.system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded

def fire(text):
    os.system(""); faded = ""
    green = 250
    for line in text.splitlines():
        faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return faded

def getTheme():
    themes = ["saturne", "dark", "fire", "water", "neon"]
    with open(os.getenv("temp")+"\\saturne_theme", 'r') as f:
        text = f.read()
        if not any(s in text for s in themes):
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid theme was given, Switching to default. . .')
            setTheme('saturne')
            sleep(2.5)
            __import__("Saturne").main()
        return text

def setTheme(new: str):
    with open(os.getenv("temp")+"\\saturne_theme", 'w'): pass
    with open(os.getenv("temp")+"\\saturne_theme", 'w') as f:
        f.write(new)

def banner(theme=None):
    if theme == "dark":
        print(bannerTheme(blackwhite, blackwhite))
    elif theme == "fire":
        print(bannerTheme(fire, fire))
    elif theme == "water":
        print(bannerTheme(water, greenblue))
    elif theme == "neon":
        print(bannerTheme(pinkred, purpleblue))
    else:
        print(f'''{Fore.GREEN}
                                      ███████╗ █████╗ ████████╗██╗   ██╗██████╗ ███╗   ██╗███████╗
                                      ██╔════╝██╔══██╗╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██╔════╝
                                      ███████╗███████║   ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗  
                                      ╚════██║██╔══██║   ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝  
                                      ███████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗
                                      ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
                                      Crée par GalackQSM                      Github.com/GalackQSM
'''.replace('█', f'{Fore.WHITE}█{Fore.GREEN}') + f'''   
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.RESET}[{Fore.GREEN}1{Fore.RESET}]{Fore.LIGHTBLACK_EX} Détruire un compte                                             {Fore.RESET}[{Fore.GREEN}10{Fore.RESET}]{Fore.LIGHTBLACK_EX} Bloquer les amis
{Fore.RESET}[{Fore.GREEN}2{Fore.RESET}]{Fore.LIGHTBLACK_EX} Supprimer tout les amis                                        {Fore.RESET}[{Fore.GREEN}11{Fore.RESET}]{Fore.LIGHTBLACK_EX} Changeur de profil
{Fore.RESET}[{Fore.GREEN}3{Fore.RESET}]{Fore.LIGHTBLACK_EX} Supprimer et quitter tous les serveurs                         {Fore.RESET}[{Fore.GREEN}12{Fore.RESET}]{Fore.LIGHTBLACK_EX} Cloturer un compte 
{Fore.RESET}[{Fore.GREEN}4{Fore.RESET}]{Fore.LIGHTBLACK_EX} Spam créer de nouveaux serveurs                                {Fore.RESET}[{Fore.GREEN}13{Fore.RESET}]{Fore.LIGHTBLACK_EX} Créer un Grabber 
{Fore.RESET}[{Fore.GREEN}5{Fore.RESET}]{Fore.LIGHTBLACK_EX} Supprimer les DMs                                              {Fore.RESET}[{Fore.GREEN}14{Fore.RESET}]{Fore.LIGHTBLACK_EX} Grabber QR Code
{Fore.RESET}[{Fore.GREEN}6{Fore.RESET}]{Fore.LIGHTBLACK_EX} Mass Dm                                                        {Fore.RESET}[{Fore.GREEN}15{Fore.RESET}]{Fore.LIGHTBLACK_EX} Rapport en masse
{Fore.RESET}[{Fore.GREEN}7{Fore.RESET}]{Fore.LIGHTBLACK_EX} Activer le mode de saisie                                      {Fore.RESET}[{Fore.GREEN}16{Fore.RESET}]{Fore.LIGHTBLACK_EX} Spammeur de groupe
{Fore.RESET}[{Fore.GREEN}8{Fore.RESET}]{Fore.LIGHTBLACK_EX} Obtenir des informations d'un compte                           {Fore.RESET}[{Fore.GREEN}17{Fore.RESET}]{Fore.LIGHTBLACK_EX} Supprimer un webhook
{Fore.RESET}[{Fore.GREEN}9{Fore.RESET}]{Fore.LIGHTBLACK_EX} Connectez-vous à un compte                                     {Fore.RESET}[{Fore.GREEN}18{Fore.RESET}]{Fore.RED} Paramètres
                                                                                                                           {Fore.RESET}[{Fore.GREEN}19{Fore.RESET}]{Fore.RED} Crédits
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')

def bannerTheme(type1, type2):
    return type1(f'''
                                      ███████╗ █████╗ ████████╗██╗   ██╗██████╗ ███╗   ██╗███████╗
                                      ██╔════╝██╔══██╗╚══██╔══╝██║   ██║██╔══██╗████╗  ██║██╔════╝
                                      ███████╗███████║   ██║   ██║   ██║██████╔╝██╔██╗ ██║█████╗  
                                      ╚════██║██╔══██║   ██║   ██║   ██║██╔══██╗██║╚██╗██║██╔══╝  
                                      ███████║██║  ██║   ██║   ╚██████╔╝██║  ██║██║ ╚████║███████╗
                                      ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
                                      Crée par GalackQSM                      Github.com/GalackQSM
''')+type2('''  
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[1] Détruire un compte                                                            [10] Bloquer les amis
[2] Supprimer tout les amis                                                       [11] Changeur de profil
[3] Supprimer et quitter tous les serveurs                                        [12] Cloturer un compte
[4] Spam créer de nouveaux serveurs                                               [13] Créer un Grabber 
[5] Supprimer les DMs                                                             [14] Grabber QR Code
[6] Mass Dm                                                                       [15] Rapport en masse
[7] Activer le mode de saisie                                                     [16] Spammeur de groupe
[8] Obtenir des informations d'un compte                                          [17] Supprimer un webhook
[9] Connectez-vous à un compte                                                    [18] Paramètres
                                                                                  [19] Crédits
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')
