from socket import gethostbyaddr
from concurrent.futures import ThreadPoolExecutor
import os
os.system("clear")
print("               script name :mass iprange")
print("")
print("                coded by :i-Xploit")
print("")
print("                language  : python")
print("")
print("                team : there is not any")
print("")
print("                date : 2022-3-5")
print("")
print("               location : Indonesia , surakarta ")
print("")
class IpRange:

    def __init__(self) -> None:
        self.result = "result.txt"
        self.thread = 30
        self.ips = []

    def check(self, ip: str):
        try:
            return ip if gethostbyaddr(ip) else False
        except:
            return False

    def ip_replace(self, ip: str) -> str:
        return ".".join(ip.split(".")[:-1])

    def iprange(self, start: int=1, end: int=255) -> None:
        try:
            for x in self.ips:
                for y in range(start, end+1):
                    ip = f"{self.ip_replace(x)}.{y}"
                    if (res := self.check(ip)):
                        print("\x1b[1;32m[*] %s" % res)
                        open(self.result, "a+").write(res+"\n")
                    else:
                        print("\x1b[1;31m[^] %s" % ip)
        except Exception as e:
            print(e)

    def start(self):
        self.ips = list(dict.fromkeys(open(input("[+] IP List : ")).read().splitlines()))
        self.thread = int(input("[+] Thread : "))
        self.result = input("[+] Result : ")
        with ThreadPoolExecutor(max_workers=self.thread) as tot:
            tot.submit(self.iprange)

if __name__ == "__main__":
    IpRange().start()
