import requests
from scapy.all import *


def arp_display(pkt):
    if pkt[ARP].op == 1: #who-has (request)
        if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
            if pkt[ARP].hwsrc == "f0:27:2d:0b:8e:b9":
                requests.get("http://localhost:3000/buttonPress")
            else:
                print "ARP Probe from: " + pkt[ARP].hwsrc


print sniff(prn=arp_display, filter="arp", store=0, count=0)
