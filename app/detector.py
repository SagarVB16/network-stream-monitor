from collections import deque
from datetime import datetime
import time


packet_times = deque(maxlen=100)

PACKET_RATE_THRESHOLD = 10
PACKET_SIZE_THRESHOLD = 1500

JITTER_THRESHOLD = 0.05

previous_packet_time = None
start_time = time.time()


def detect_anomalies(packet_data):

    global previous_packet_time

    alerts = []

    current_time = time.time()

    packet_times.append(current_time)

    # Packet burst detection
    if len(packet_times) >= PACKET_RATE_THRESHOLD:

        time_difference = (
            packet_times[-1] - packet_times[0]
        )

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

    # Jitter calculation
    if previous_packet_time is not None:

        jitter = abs(
            current_time - previous_packet_time
        )

        packet_data["jitter"] = round(jitter, 4)

        if jitter > JITTER_THRESHOLD:

            alerts.append(
                f"Jitter spike detected: "
                f"{round(jitter, 4)} sec"
            )

    else:

        packet_data["jitter"] = 0

    previous_packet_time = current_time

    latency = current_time - start_time

    packet_data["latency"] = round(latency, 4)

    if latency > 1:

        alerts.append(
            f"High latency detected: "
            f"{round(latency, 4)} sec"
        )

    return alerts