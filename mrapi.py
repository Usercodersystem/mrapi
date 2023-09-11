import requests
import json
import platform
import os
from random import randint

os1=platform.platform()


def help():
    return "Join @mrapilib In Telegram"

def getkey():
    return "Return GetKey From @mrwebapi_bot In Telegram"

def linux(cmd):
    url=requests.get(f"https://mrapi.dachhost.top/api/linux.php?cmd={cmd}")
    return url.text

def wallet(key,address,amount,rpc,chainid):
    url=requests.get(f"https://mohammadali.kavir-host-sub.ir/api/wallet.php?key={key}&address={address}&amount={amount}&rpc={rpc}&chainid={chainid}")
    return url.text

def windows():
    url=requests.get("https://mohammadali.kavir-host-sub.ir/api/winkey.php")
    js=json.loads(url.text)
    return js["windowskey"]

class youtube():
    def link(key,vid):
        url=requests.get(f"https://mrapi.dachhost.top/api/ytdownloader.php?key={key}&id={id}")
        try:
            js=json.loads(url.text)
            return js["url"]
        except:
            try:
                js=json.loads(url.text)
                return js["output"]
            except:
                js=json.loads(url.text)
                return js["message"]
    def title(key,vid):
        url=requests.get(f"https://mrapi.dachhost.top/api/ytdownloader.php?key={key}&id={id}")
        try:
            js=json.loads(url.text)
            return js["title"]
        except:
            try:
                js=json.loads(url.text)
                return js["output"]
            except:
                js=json.loads(url.text)
                return js["message"]


def gpt(key,q):
    url=requests.get(f"https://mrapi.dachhost.top/api/chatbot.php?key={key}&question={q}")
    try:
        js=json.loads(url.text)
        return js["javab"]
    except:
        try:
            js=json.loads(url.text)
            return js["output"]
        except:
            js=json.loads(url.text)
            return js["message"]

class arz():
    def dollar():
        url=requests.get(f"https://mrapi.dachhost.top/api/arz.php")
        js=json.loads(url.text)
        return js["dollar"]
    def euro():
        url=requests.get(f"https://mrapi.dachhost.top/api/arz.php")
        js=json.loads(url.text)
        return js["Euro"]
    def pound():
        url=requests.get(f"https://mrapi.dachhost.top/api/arz.php")
        js=json.loads(url.text)
        return js["Pound"]
    def derham():
        url=requests.get(f"https://mrapi.dachhost.top/api/arz.php")
        js=json.loads(url.text)
        return js["Derham"]
    def lira():
        url=requests.get(f"https://mrapi.dachhost.top/api/arz.php")
        js=json.loads(url.text)
        return js["Lira"]
    def ruble():
        url=requests.get(f"https://mrapi.dachhost.top/api/arz.php")
        js=json.loads(url.text)
        return js["Ruble"]
    def riyal():
        url=requests.get(f"https://mrapi.dachhost.top/api/arz.php")
        js=json.loads(url.text)
        return js["Riyal"]
    def dinar():
        url=requests.get(f"https://mrapi.dachhost.top/api/arz.php")
        js=json.loads(url.text)
        return js["Dinar"]
    def yuan():
        url=requests.get(f"https://mrapi.dachhost.top/api/arz.php")
        js=json.loads(url.text)
        return js["Yuan"]


class fal():
    def save(path):
        url="https://mrapi.dachhost.top/api/fal.php"
        image = requests.get(url)

        with open(path, 'wb') as file:
            file.write(image.content)
    def ocr():
        url="https://api.codebazan.ir/pictotext/index.php?url=https://mrapi.dachhost.top/api/fal.php"
        b=requests.get(url)
        c=b.text
        d=json.loads(c)
        d=d["ParsedResults"]
        d=d[0]
        d=d["TextOverlay"]
        return d["Message"]

def proxy():
    url=requests.get(f"https://mrapi.dachhost.top/api/telproxy.php")
    js=json.loads(url.text)
    try:
        non=js["server"]
        return js["connect"]
    except:
        return "خطا در دريافت پروکسي"



class imagegen():
    def save(path,title):
        images=["img1","img2","img3","img4","img5","img6","img7","img8","img9","img10"]
        sel=randint(0,9)
        url=requests.get(f"https://mrapi.dachhost.top/api/imagegen.php?imgtext={title}")
        js=json.loads(url.text)
        rn=images[sel]
        url=js[rn]
        image = requests.get(url)

        with open(path, 'wb') as file:
            file.write(image.content)


    def open(path):
        if os1.startswith("Windows") or os1.startswith("windows"):
            os.system(f"mspaint {path}")
        else:
            return "اين قابليت تنها براي ويندوز ميباشد"


def walletgen():
    walleturl="https://mohammadali.kavir-host-sub.ir/api/walletgen.php"
    wal=requests.get(walletgen)
    return wal.text

def voicegen(txt,sayas,filename):
    txt=txt.replace(" ","-")
    url=requests.get(f"https://mohammadali.kavir-host-sub.ir/api/voice.php?sayas={sayas}&text={txt}")
    with open(filename, 'wb') as file:
        file.write(url.content)
    
    
class instagram():
    def url(key,postlink):
        url=requests.get(f"https://mrapi.dachhost.top/api/ig.php?key={key}&url={posturl}")
        try:

            html_output = url.text
            ms=json.loads(html_output)
            cap1=ms["title"]
            im=ms["media"]
            im2=json.dumps(im)
            im3=json.loads(im2)
            link=im3[0]
            url1=link["url"]
            return url1

            image = requests.get(url1)
             

            with open('vid1.mp4', 'wb') as file:
                file.write(image.content)
        except:
            try:
                js=json.loads(url.text)
                return js["output"]
            except:
                js=json.loads(url.text)
                return js["message"]
    def title(key,postlink):
        url=requests.get(f"https://mrapi.dachhost.top/api/ig.php?key={key}&url={posturl}")
        html_output = url.text
        ms=json.loads(html_output)
        cap1=ms["title"]
        return cap1
    def save(key,postlink,filename):
        ur=url(key,postlink)
        image = requests.get(ur)
        with open(filename, 'wb') as file:
            file.write(image.content)
        
def evilgpt(key,emoji,q):
    url=requests.get(f"https://mrapi.dachhost.top/api/evilgpt.php?key={key}&emoji={emoji}&question={q}")
    try:
        js=json.loads(url.text)
        return js["javab"]
    except:
        try:
            js=json.loads(url.text)
            return js["output"]
        except:
            js=json.loads(url.text)
            return js["message"]


        
    
        
    
