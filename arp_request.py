#! /usr/bin/env python

from tabulate import tabulate
from scapy.all import srp, Ether, ARP, conf
import argparse # optparse deapreciated
import sys


def getInput():
    parser = argparse.ArgumentParser(description="IP adresini configler")
    parser.add_argument("-i", "--ip", dest="ipadress",
                        help="Arkadasim tek opsiyon var zaten -i yaz ip  yaz. Hic olmadi direk calistir default yine akar.")
    args = parser.parse_args()
    if not args.ipadress:
        print("Parametre girmedin. Alayina gidiyorum.")  # Komik olmayan komiklikler
        args.ipadress = "192.168.0.1/24"  # GOP Cocugu is online. Alayina sorgu.
    return args.ipadress


def getTable(ip="192.168.0.1/24"):
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip),
                     timeout=2)
    return ans


conf.verb = 0
df = []

for snd, rcv in getTable(getInput()):
    df.append({rcv.sprintf(r"%Ether.src%"),
               rcv.sprintf(r"%ARP.psrc%")
               })

print(tabulate(df, tablefmt="grid", headers=["SENDER", "RECIEVER"]))
