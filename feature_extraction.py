from scapy.all import rdpcap, IP, TCP, UDP
import pandas as pd

def extract_features(pcap_file):
    packets = rdpcap(pcap_file)
    data = []

    for pkt in packets:
        if IP in pkt:
            data.append({
                "src_ip": pkt[IP].src,
                "dst_ip": pkt[IP].dst,
                "protocol": pkt[IP].proto,
                "packet_size": len(pkt),
                "tcp": int(TCP in pkt),
                "udp": int(UDP in pkt)
            })

    df = pd.DataFrame(data)
    df.to_csv("data/processed/dataset.csv", index=False)

if __name__ == "__main__":
    extract_features("data/raw/traffic.pcap")
