import psutil
import time
import csv
from datetime import datetime

def bytes_to_mb(bytes_value):
    return round(bytes_value / (1024 * 1024), 2)  # Convert to MB

print("Tracking network usage... Press CTRL+C to stop.\n")

# Initial values
net_io = psutil.net_io_counters()
start_sent = net_io.bytes_sent
start_recv = net_io.bytes_recv

try:
    while True:
        # Get current date to decide filename
        today = datetime.now().strftime("%Y-%m-%d")
        filename = f"network_usage_{today}.csv"

        # Create CSV file with headers if it doesn't exist yet
        try:
            with open(filename, "x", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Sent_MB", "Received_MB", "Total_MB"])
        except FileExistsError:
            pass  # file already exists, just append

        # Get current usage since script start
        net_io = psutil.net_io_counters()
        used_sent = bytes_to_mb(net_io.bytes_sent - start_sent)
        used_recv = bytes_to_mb(net_io.bytes_recv - start_recv)
        total = used_sent + used_recv

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Append new row to today's log file
        with open(filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, used_sent, used_recv, total])

        print(f"{timestamp} | Sent: {used_sent} MB | Received: {used_recv} MB | Total: {total} MB", end="\r")

        time.sleep(60)  # log every 1 minute (change if needed)

except KeyboardInterrupt:
    print("\nStopped tracking.")
