# Network Usage Tracker

## Description
This project is a simple Python script that tracks and logs network usage (data sent and received) on your system. It continuously monitors network I/O counters, calculates the total bytes sent and received since the script started, and logs this data to a daily CSV file. The script also prints real-time updates to the console every minute.

The logged data includes:
- Timestamp
- Sent data in MB
- Received data in MB
- Total data in MB

## How It Works
1. The script uses the `psutil` library to access network I/O counters.
2. It calculates the difference in bytes sent and received from the initial values when the script started.
3. Every 60 seconds, it logs the current usage to a CSV file named `network_usage_YYYY-MM-DD.csv` (one file per day).
4. It prints the current usage to the console in real-time.
5. The script runs indefinitely until interrupted with CTRL+C.

## Requirements
- Python 3.6 or higher (due to f-string usage)
- Windows, macOS, or Linux operating system
- Administrative privileges may be required on some systems to access network counters

## Dependencies
- `psutil`: A cross-platform library for retrieving information on running processes and system utilization.

## Installation
1. Ensure Python 3.6+ is installed on your system.
2. Install the required dependency using pip:
   ```
   pip install psutil
   ```
3. Download or clone the project files (`app.py` and this README).

## Usage
1. Run the script:
   ```
   python app.py
   ```
2. The script will start tracking network usage and display updates in the console.
3. Press CTRL+C to stop tracking and exit the script.
4. Check the generated CSV files in the same directory for historical data.

## Output
- **Console Output**: Real-time display of sent, received, and total MB used since script start.
- **CSV Files**: Daily logs with timestamps and usage data. Files are named `network_usage_YYYY-MM-DD.csv`.

## Notes
- The script tracks cumulative usage since it was started, not per session.
- Network counters are system-wide, not per application.
- Ensure you have sufficient disk space for log files.
- The logging interval is set to 60 seconds but can be modified in the code.

## Troubleshooting
- If you encounter permission errors, try running the script with administrative privileges.
- Ensure `psutil` is installed correctly by running `pip list` and checking for it.
