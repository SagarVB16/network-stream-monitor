import asyncio

from scapy.all import sniff

from parser import parse_packet

from database import (
    initialize_database,
    insert_packet
)

from detector import detect_anomalies

from websocket_manager import broadcast_message

from metrics import (
    update_metrics,
    increment_alert_count
)


def process_packet(packet):

    parsed_data = parse_packet(packet)

    if parsed_data:

        # Store packet
        insert_packet(parsed_data)
        update_metrics(parsed_data)

        # Detect anomalies
        alerts = detect_anomalies(parsed_data)

        # Send alerts
        for alert in alerts:

            alert_message = (
                f"[ALERT] {alert}"
            )

            print(alert_message)

            increment_alert_count()

            try:

                asyncio.run(
                    broadcast_message(alert_message)
                )

            except Exception as error:

                print(
                    f"WebSocket Error: {error}"
                )

        # Print packet details
        print("\n==============================")
        print(f"Timestamp        : {parsed_data['timestamp']}")
        print(f"Protocol         : {parsed_data['protocol']}")
        print(f"Source IP        : {parsed_data['src_ip']}")
        print(f"Destination IP   : {parsed_data['dst_ip']}")
        print(f"Source Port      : {parsed_data['src_port']}")
        print(f"Destination Port : {parsed_data['dst_port']}")
        print(f"Packet Size      : {parsed_data['packet_size']} bytes")
        print(f"Jitter           : {parsed_data['jitter']} sec")

        if parsed_data["tcp_flags"]:

            print(
                f"TCP Flags        : "
                f"{parsed_data['tcp_flags']}"
            )


def start_sniffing():

    print(
        "Starting packet monitoring system..."
    )

    initialize_database()

    sniff(
        prn=process_packet,
        store=False
    )


if __name__ == "__main__":

    start_sniffing()