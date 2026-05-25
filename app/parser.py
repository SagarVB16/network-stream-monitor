from scapy.layers.inet import IP, TCP, UDP
from datetime import datetime


def parse_packet(packet):

    if IP not in packet:
        return None

    packet_data = {
        "timestamp": datetime.now().strftime("%H:%M:%S"),
        "src_ip": packet[IP].src,
        "dst_ip": packet[IP].dst,
        "packet_size": len(packet),
        "protocol": "OTHER",
        "src_port": None,
        "dst_port": None,
        "tcp_flags": None
    }

    if TCP in packet:

        packet_data["protocol"] = "TCP"
        packet_data["src_port"] = packet[TCP].sport
        packet_data["dst_port"] = packet[TCP].dport
        packet_data["tcp_flags"] = str(packet[TCP].flags)

    elif UDP in packet:

        packet_data["protocol"] = "UDP"
        packet_data["src_port"] = packet[UDP].sport
        packet_data["dst_port"] = packet[UDP].dport

    return packet_data