import urllib.request
from time import time
from threading import Thread


def get_info(name):
    page = urllib.request.urlopen(name)


web = ['https://www.google.ru/', 'https://www.youtube.com/', 'https://www.twitch.tv/', 'https://www.codeforces.com/', 'https://www.figma.com/', 'https://www.ubuntu.ru/',
       'https://www.kali.org/', 'https://www.manjaro.org/', 'https://getfedora.org', 'https://www.debian.org/']

start = time()
one = [Thread(target=get_info, args=(web[i],)) for i in range(10)]
for o in one:
    o.start()
print(f"with threading, time: {time() - start}")

start = time()
page = urllib.request.urlopen('https://www.google.ru/')
page = urllib.request.urlopen('https://www.youtube.com/')
page = urllib.request.urlopen('https://www.twitch.tv/')
page = urllib.request.urlopen('https://www.codeforces.com/')
page = urllib.request.urlopen('https://www.figma.com/')
page = urllib.request.urlopen('https://www.ubuntu.ru/')
page = urllib.request.urlopen('https://www.kali.org/')
page = urllib.request.urlopen('https://www.manjaro.org/')
page = urllib.request.urlopen('https://getfedora.org')
page = urllib.request.urlopen('https://www.debian.org/')
print(f"without threading, time {time()- start}")