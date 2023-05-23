import requests 
# session = requests.Session()
from time import sleep as t

def getProxy():
    for i in range(50):
        try:
            res = requests.get("https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true", timeout = 5)
            pr  = res.text
            # http://5.78.102.66:8080
            proxy = pr.split("//")[1]
        except:
             pass
        

    
        try:
            response = requests.get('https://httpbin.org/ip', proxies={'http': proxy, 'https': proxy}, timeout=5)
            if response.status_code == 200 and 'origin' in response.json():
                # print(proxy)
                d= {
                    "ip":proxy
                }
                print("prox=========",proxy)
                # r = response = session.post("https://amharic-pushdown.000webhostapp.com/omar.php",data=d)
                # print(r.json())
                # print()
                # with open('pa.txt', "+a", errors="ignore") as fin:
                #     fin.write(proxy+"\n")
                #     print("Dnss............ ",proxy)
            else:
                print("False ")
        except:
                    print("False EEEE")


getProxy()