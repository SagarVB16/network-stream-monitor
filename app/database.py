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