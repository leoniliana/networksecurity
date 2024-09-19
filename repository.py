import socket
import argparse
from datetime import datetime

def perform_port_scan(target, start, end):
    """
    Scans a range of ports on a specified target.

    Args:
        target (str): The IP address or domain to scan.
        start (int): The starting port number.
        end (int): The ending port number.
    """
    print(f"\nInitiating port scan on {target}")
    print(f"Scanning ports from {start} to {end}")
    print(f"Scan began at: {datetime.now()}\n")
    
    try:
        ip_address = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Unable to resolve hostname: {target}. Exiting...")
        return
    
    for port in range(start, end + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.settimeout(1)
            try:
                status = connection.connect_ex((ip_address, port))
                if status == 0:
                    print(f"Port {port} is OPEN")
                else:
                    print(f"Port {port} is CLOSED")
            except socket.error as e:
                print(f"Connection error on port {port}: {e}")

    print(f"\nScan finished at: {datetime.now()}")

def main():
    parser = argparse.ArgumentParser(description="A customizable Python port scanning tool")
    parser.add_argument("target", help="IP address or domain to scan")
    parser.add_argument("-s", "--start", type=int, default=1, help="Port to start scanning from (default is 1)")
    parser.add_argument("-e", "--end", type=int, default=1024, help="Port to end scanning at (default is 1024)")
    
    args = parser.parse_args()
    
    if args.start < 1 or args.end > 65535:
        print("Port range is invalid. Ports must be within 1 and 65535.")
        return
    
    perform_port_scan(args.target, args.start, args.end)

if __name__ == "__main__":
    main()
