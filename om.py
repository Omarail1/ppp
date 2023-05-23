import requests 
# session = requests.Session()
from time import sleep as t

def getProxy():
    for i in range(50):
        try:
       
        except:
             pass
        

    
        try:
            response = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=5)
            if response.status_code == 200 and 'origin' in response.json():
                # print(proxy)
                d= {
                    "ip":proxy
                }
 
            else:
                print("False ")
        except:
                    print("False EEEE")


getProxy()
