from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP


def process_packet(packet):

    if IP in packet:

        src_ip = packet[IP].src
        dst_ip = packet[IP].dst

        protocol = "OTHER"

        if TCP in packet:
            protocol = "TCP"

        elif UDP in packet:
            protocol = "UDP"

        print(
            f"[{protocol}] "
            f"{src_ip} -> {dst_ip} | "
            f"Packet Size: {len(packet)} bytes"
        )


def start_sniffing():
    print("Starting packet capture...")

    sniff(
        prn=process_packet,
        store=False
    )


if __name__ == "__main__":
    start_sniffing()