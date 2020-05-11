#signing

import os, sys

def start():
    print('[!] set password as "toor"')
    os.system("openssl req -x509 -newkey rsa:4096 -keyout output/key.pem -out output/ignorecert.pem -days 365")
    os.system('osslsigncode sign -certs "output/cert.pem" -key "output/key.pem" -pass "toor" -n "Microsoft" -i "https://www.Microsoft.com" -t "http://timestamp.comodoca.com/authenticode" -in "output/evil.exe" -out "output/signed.exe"')
