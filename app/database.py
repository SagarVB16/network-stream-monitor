import sqlite3


DATABASE_NAME = "network_monitor.db"


def initialize_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS packet_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        protocol TEXT,
        src_ip TEXT,
        dst_ip TEXT,
        src_port INTEGER,
        dst_port INTEGER,
        packet_size INTEGER,
        tcp_flags TEXT
    )
    """)

    connection.commit()
    connection.close()


def insert_packet(packet_data):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    INSERT INTO packet_logs (
        timestamp,
        protocol,
        src_ip,
        dst_ip,
        src_port,
        dst_port,
        packet_size,
        tcp_flags
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        packet_data["timestamp"],
        packet_data["protocol"],
        packet_data["src_ip"],
        packet_data["dst_ip"],
        packet_data["src_port"],
        packet_data["dst_port"],
        packet_data["packet_size"],
        packet_data["tcp_flags"]
    ))

    connection.commit()
    connection.close()


def get_metrics_data():
    metrics = {
    "total_packets": 0,
    "tcp_packets": 0,
    "udp_packets": 0,
    "alerts": 0,
    "current_jitter": 0,
    "current_latency": 0
}

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    metrics = {
        "total_packets": 0,
        "tcp_packets": 0,
        "udp_packets": 0
    }

    cursor.execute(
        "SELECT COUNT(*) FROM packet_logs"
    )

    metrics["total_packets"] = (
        cursor.fetchone()[0]
    )

    cursor.execute(
        "SELECT COUNT(*) FROM packet_logs "
        "WHERE protocol='TCP'"
    )

    metrics["tcp_packets"] = (
        cursor.fetchone()[0]
    )

    cursor.execute(
        "SELECT COUNT(*) FROM packet_logs "
        "WHERE protocol='UDP'"
    )

    metrics["udp_packets"] = (
        cursor.fetchone()[0]
    )
    metrics["alerts"] = 0

    metrics["current_jitter"] = round(
        metrics["udp_packets"] / 1000,
        4
    )

    metrics["current_latency"] = round(
        metrics["tcp_packets"] / 1000,
        4
    )

    connection.close()

    return metrics

def get_top_ips():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
    SELECT src_ip, COUNT(*) as packet_count
    FROM packet_logs
    GROUP BY src_ip
    ORDER BY packet_count DESC
    LIMIT 5
    """)

    results = cursor.fetchall()

    connection.close()

    return results