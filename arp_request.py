#! /usr/bin/env python

import scapy.all as scapy # Mevzuda adamlari ipe dizecek olan arkadas
import optparse # Input girmeleri icin bir arac

def get_input_from_bebe():
	parse_object = optparse.OptionParser() 
	parse_object.add_option("-i", "--ip", dest="ipadress", help="Arkadasim tek opsiyon var zaten -i yaz ip  yaz. Hic olmadi direk calistir default yine akar.")

	(user_input,arguments)=parse_object.parse_args()
	
	if not user_input.ipadress:
		print("Parametre girmedin. Alayina gidiyorum.")  #Komik olmayan komiklikler
		user_input.ipadress = "192.168.0.1/24" #GOP Cocugu is online. Alayina sorgu.
	return user_input

def network_search(ip = "192.168.0.1/24"):
	arp_request_packet = scapy.ARP(pdst = ip) #ARP sorgusu soracagimiz abiler
	broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #Modeme sen hayirdir cekme
	combined_packet = broadcast_packet/arp_request_packet #Paketlerimizi harmanliyoruz
	(answered, offline) = scapy.srp(combined_packet, timeout=1) #A sorguladigimiz ve bize donen elemanlar, B offline olup cevap vermeyenler.
	answered.summary() #Insan gibi okunacak sekilde output aliyoruz.

user_ipadress = get_input_from_bebe()
network_search(user_ipadress.ipadress)
