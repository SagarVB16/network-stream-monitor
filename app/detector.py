from collections import deque
from datetime import datetime


packet_times = deque(maxlen=100)

PACKET_RATE_THRESHOLD = 30
PACKET_SIZE_THRESHOLD = 1500


def detect_anomalies(packet_data):

    alerts = []

    current_time = datetime.now()

    packet_times.append(current_time)

    # Packet burst detection
    if len(packet_times) >= PACKET_RATE_THRESHOLD:

        time_difference = (
            packet_times[-1] - packet_times[0]
        ).total_seconds()

        if time_difference < 1:
            alerts.append(
                "High packet burst detected"
            )

    # Large packet detection
    if packet_data["packet_size"] > PACKET_SIZE_THRESHOLD:

        alerts.append(
            f"Large packet detected: "
            f"{packet_data['packet_size']} bytes"
        )

    return alerts