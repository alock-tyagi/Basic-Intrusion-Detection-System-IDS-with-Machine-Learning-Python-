from scapy.all import sniff, wrpcap

def capture_packets(interface="eth0", count=1000):
    packets = sniff(iface=interface, count=count)
    wrpcap("data/raw/traffic.pcap", packets)

if __name__ == "__main__":
    capture_packets()
