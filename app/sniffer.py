from scapy.all import sniff

from parser import parse_packet

from database import (
    initialize_database,
    insert_packet
)

from detector import detect_anomalies


def process_packet(packet):

    parsed_data = parse_packet(packet)

    if parsed_data:

        # Store packet in database
        insert_packet(parsed_data)

        # Run anomaly detection
        alerts = detect_anomalies(parsed_data)

        # Print alerts
        for alert in alerts:
            print(f"\n[ALERT] {alert}")

        # Print packet details
        print("\n==============================")
        print(f"Timestamp        : {parsed_data['timestamp']}")
        print(f"Protocol         : {parsed_data['protocol']}")
        print(f"Source IP        : {parsed_data['src_ip']}")
        print(f"Destination IP   : {parsed_data['dst_ip']}")
        print(f"Source Port      : {parsed_data['src_port']}")
        print(f"Destination Port : {parsed_data['dst_port']}")
        print(f"Packet Size      : {parsed_data['packet_size']} bytes")

        if parsed_data["tcp_flags"]:
            print(f"TCP Flags        : {parsed_data['tcp_flags']}")


def start_sniffing():

    print("Starting packet monitoring system...")

    # Create database and tables
    initialize_database()

    # Start live packet capture
    sniff(
        prn=process_packet,
        store=False
    )


if __name__ == "__main__":
    start_sniffing()