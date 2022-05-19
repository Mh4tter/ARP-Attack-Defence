from scapy.all import*
import sys
import time
import itertools







def arp_spoof(dest_ip, dest_mac, source_ip):
	pass

def arp_restore(dest_ip, dest_mac, source_mac):
	packet = ARP(op="is at", hwsrc=source_mac,
					prsc= source_ip, hwdst= dest_mac, pdst= dest_ip)

	send(packet, verbose=False)

def main():
	victim_ip= input("Enter target IP: ")				#passed to the program via CLI
	router_ip= input("Enter router IP: ")				#passed to the program via CLI
	victim_mac= getmacbyip(victim_ip)
	router_mac= getmacbyip(router_ip)

	try:
		print("Sending spoofed ARP packets...")
		while True:
			packet_amount = 100
			for _ in itertools.repeat(None, packet_amount):
				arp_spoof(victim_ip, victim_mac, router_ip)
				arp_spoof(router_ip, router_mac, victim_ip)
				
			

	except KeyboardInterrupt:
		print('\n Restoring ARP tables...')
		arp_restore(router_ip, router_mac, victim_ip, victim_mac)
		arp_restore(victim_ip, victim_mac, router_ip, router_mac)
		quit()


main()
