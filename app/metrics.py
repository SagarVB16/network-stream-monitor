metrics = {
    "total_packets": 0,
    "tcp_packets": 0,
    "udp_packets": 0,
    "alerts": 0,
    "current_jitter": 0,
    "current_latency": 0
}


def update_metrics(packet_data):

    metrics["total_packets"] += 1

    if packet_data["protocol"] == "TCP":
        metrics["tcp_packets"] += 1

    elif packet_data["protocol"] == "UDP":
        metrics["udp_packets"] += 1

    metrics["current_jitter"] = (
        packet_data.get("jitter", 0)
    )

    metrics["current_latency"] = (
        packet_data.get("latency", 0)
    )

    print("UPDATED METRICS:", metrics)


def increment_alert_count():

    metrics["alerts"] += 1


def get_metrics():

    return metrics