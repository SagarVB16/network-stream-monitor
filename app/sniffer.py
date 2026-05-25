from scapy.all import sniff
from parser import parse_packet


def process_packet(packet):

    parsed_data = parse_packet(packet)

    if parsed_data:

        print("\n==============================")
        print(f"Timestamp      : {parsed_data['timestamp']}")
        print(f"Protocol       : {parsed_data['protocol']}")
        print(f"Source IP      : {parsed_data['src_ip']}")
        print(f"Destination IP : {parsed_data['dst_ip']}")
        print(f"Source Port    : {parsed_data['src_port']}")
        print(f"Destination Port: {parsed_data['dst_port']}")
        print(f"Packet Size    : {parsed_data['packet_size']} bytes")

        if parsed_data["tcp_flags"]:
            print(f"TCP Flags      : {parsed_data['tcp_flags']}")


def start_sniffing():

    print("Starting advanced packet monitoring...")

    sniff(
        prn=process_packet,
        store=False
    )


if __name__ == "__main__":
    start_sniffing()