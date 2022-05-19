# Tool to detect possible ARP attack on network


# Scapy allows you to read and send packets
from scapy.all import*
import sys
import itertools
import time
ip_mac_map = {}


# processPacket() analyzes the packets sent across the network
# if the source mac does not equal the source ip
# processPacket() attempts to match the old ip on the MAC table
# if the function can not find the old ip you are likely under attack

# print("ARP Attack Detector V 1.0")


# src_ip = IP(dst=sys.argv[1])
# src_mac = ip_mac_map

# while src_ip == IP(dst=sys.argv[1]):
# 	print("Scanning network for ARP attack...")
# 	time.sleep(10)

def processPacket(packet):
	src_ip = packet['ARP'].psrc 
	src_mac = packet['Ether'].src
	

	if src_mac in ip_mac_map != src_ip:
		try:
			old_ip = ip_mac_map
		except:
			old_ip = 'unknown'
		alert_message = ("\nPossible ARP attack detected! \n"
					+ "It is possible that the machine with IP Address: \n"
					+ str(old_ip) + " is pretending to be " + str(src_ip)
					+ "\n")
		return alert_message

	else:
		ip_mac_map[src_mac] = src_ip




		



			


sniff(count= 0, filter="arp", store = 0, prn= processPacket)