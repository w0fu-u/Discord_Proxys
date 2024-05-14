import requests
import random
import threading
import colorama
import webbrowser
from colorama import Fore as O

colorama.init()

print(O.LIGHTMAGENTA_EX+"""
                @                     
                @                     
                @                     
                @                     
                @                     
                @                     
                @                     
                @                     
                @                     
                @                     
                @                     
                @                     
                @                     
                @                     
               @@@                    
              @ @ @                   
             @  @  @                  
            @   @   @                 
           @    @    @                
          @     @     @               
         @      @      @              
        @       @       @             
       @        @        @            
       @@@@@    @    @@@@@            
        @   @@@ @ @@@   @             
         @     @@@     @              
          @     @     @               ██████╗ ███████╗███╗   ██╗████████╗ █████╗ 
           @    @    @                ██╔══██╗██╔════╝████╗  ██║╚══██╔══╝██╔══██╗
            @   @   @                 ██████╔╝█████╗  ██╔██╗ ██║   ██║   ███████║
             @  @  @                  ██╔═══╝ ██╔══╝  ██║╚██╗██║   ██║   ██╔══██║
              @ @ @                   ██║     ███████╗██║ ╚████║   ██║   ██║  ██║
               @@@                    ╚═╝     ╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝
                @                     by #wofu_u
      
                                    
""")



def make_request_with_proxy(batch):
    for ip in batch:
        proxy = f"{ip}:80"
        try:

            headers = {
                    'Accept': '*/*',
                    'Accept-Language': 'en-US,en;q=0.9',
                    'Connection': 'keep-alive',
                    'Referer': 'http://discord.com/',
                    'Sec-Fetch-Dest': 'empty',
                    'Sec-Fetch-Mode': 'cors',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-GPC': '1',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.51',
                    'X-Track': 'eyJvcyI6IklPUyIsImJyb3dzZXIiOiJTYWZlIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKElQaG9uZTsgQ1BVIEludGVybmFsIFByb2R1Y3RzIFN0b3JlLCBhcHBsaWNhdGlvbi8yMDUuMS4xNSAoS0hUTUwpIFZlcnNpb24vMTUuMCBNb2JpbGUvMTVFMjQ4IFNhZmFyaS82MDQuMSIsImJyb3dzZXJfdmVyc2lvbiI6IjE1LjAiLCJvc192IjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfZG9tYWluX2Nvb2tpZSI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOiJzdGFibGUiLCJjbGllbnRfZXZlbnRfc291cmNlIjoic3RhYmxlIn0',
            }

            response = requests.get('http://discord.com/api/v9/experiments', headers=headers,proxies={'http': proxy}, timeout=4)
            if response.status_code == 200:
                if "fingerprint" in response.json():
                    print(O.GREEN+f"Valid Proxy Found "+(O.LIGHTGREEN_EX+f"{ip}"))
                    with open(file_name, "a") as datei:
                        datei.write(proxy + "\n")
            else:
                pass
        except requests.exceptions.RequestException as e:
            pass
    return
    
    
def generate_random_ips(batch_size):
    return [f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}" for _ in range(batch_size)]


def check_proxy(proxy, file_name):

    headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'http://discord.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.51',
            'X-Track': 'eyJvcyI6IklPUyIsImJyb3dzZXIiOiJTYWZlIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKElQaG9uZTsgQ1BVIEludGVybmFsIFByb2R1Y3RzIFN0b3JlLCBhcHBsaWNhdGlvbi8yMDUuMS4xNSAoS0hUTUwpIFZlcnNpb24vMTUuMCBNb2JpbGUvMTVFMjQ4IFNhZmFyaS82MDQuMSIsImJyb3dzZXJfdmVyc2lvbiI6IjE1LjAiLCJvc192IjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfZG9tYWluX2Nvb2tpZSI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOiJzdGFibGUiLCJjbGllbnRfZXZlbnRfc291cmNlIjoic3RhYmxlIn0',
    }
    try:
        response = requests.get('http://discord.com/api/v9/experiments', headers=headers,proxies={'http': proxy}, timeout=4)
        if response.status_code == 200:
            if "fingerprint" in response.json():
                print(O.GREEN+f"Proxy works fine "+(O.LIGHTGREEN_EX+f"{proxy}"))
                with open(file_name, 'a') as valid_file:
                    valid_file.write(f'{proxy}\n')
        else:
            print(O.RED+f"Proxy doesn't work "+(O.LIGHTRED_EX+f"{proxy}"))
    except Exception as e:
        print(O.RED+f"Proxy doesn't awnser "+(O.LIGHTRED_EX+f"{proxy}"))

def check_proxy_https(proxy, file_name):

    headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Referer': 'http://discord.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-GPC': '1',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36 Edg/114.0.1823.51',
            'X-Track': 'eyJvcyI6IklPUyIsImJyb3dzZXIiOiJTYWZlIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKElQaG9uZTsgQ1BVIEludGVybmFsIFByb2R1Y3RzIFN0b3JlLCBhcHBsaWNhdGlvbi8yMDUuMS4xNSAoS0hUTUwpIFZlcnNpb24vMTUuMCBNb2JpbGUvMTVFMjQ4IFNhZmFyaS82MDQuMSIsImJyb3dzZXJfdmVyc2lvbiI6IjE1LjAiLCJvc192IjoiIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfZG9tYWluX2Nvb2tpZSI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjk5OTksImNsaWVudF9ldmVudF9zb3VyY2UiOiJzdGFibGUiLCJjbGllbnRfZXZlbnRfc291cmNlIjoic3RhYmxlIn0',
    }
    try:
        response = requests.get('http://discord.com/api/v9/experiments', headers=headers,proxies={'http': proxy, 'https': proxy}, timeout=4)
        if response.status_code == 200:
            if "fingerprint" in response.json():
                print(O.GREEN+f"Proxy works fine "+(O.LIGHTGREEN_EX+f"{proxy}"))
                with open(file_name, 'a') as valid_file:
                    valid_file.write(f'{proxy}\n')
        else:
            print(O.RED+f"Proxy doesn't work "+(O.LIGHTRED_EX+f"{proxy}"))
    except Exception as e:
        print(O.RED+f"Proxy doesn't awnser "+(O.LIGHTRED_EX+f"{proxy}"))

def check_proxys(proxys, file_name):
    threads = []
    for proxy in proxys:
        thread = threading.Thread(target=check_proxy, args=(proxy, file_name))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def check_proxys_https(proxys, file_name):
    threads = []
    for proxy in proxys:
        thread = threading.Thread(target=check_proxy_https, args=(proxy, file_name))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()


choice = input("[1] Scann (http)    [2] Get-Free     [3] Check: ")
print("")





if choice == "1":
    file_name = input("Filename: ")
    if ".txt" not in file_name:
        file_name = file_name+".txt"
    while True:
        batch_size = 5
        ips_batches = [generate_random_ips(batch_size) for _ in range(10000)]
        threads = []
        for batch in ips_batches:
            thread = threading.Thread(target=make_request_with_proxy, args=(batch,))
            threads.append(thread)
            thread.start()
        for thread in threads:
            thread.join()


elif choice == "2":
    url = 'https://proxyscrape.com/free-proxy-list'
    webbrowser.open(url)


elif choice == "3":
    choice = input("[1] Basic  [2] Discord : ")
    print("")
    file_name_read = input("Filename (proxys to check): ")
    if ".txt" not in file_name_read:
        file_name_read = file_name_read+".txt"

    file_name_write = input("Filename (write valid proxys): ")
    if ".txt" not in file_name_write:
        file_name_write = file_name_write+".txt"
    with open(file_name_read, 'r') as f:
        proxies_list = f.read().splitlines()
    if choice == "2":
        check_proxys_https(proxies_list, file_name_write)
    else:
        check_proxys(proxies_list, file_name_write)