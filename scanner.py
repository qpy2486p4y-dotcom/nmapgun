#!/usr/bin/env python3

import socket
import argparse

COMMON_SERVICES = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3389: "RDP",
}


def scan_port(target, port, timeout=0.5):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)

    try:
        result = sock.connect_ex((target, port))
        return result == 0

    except socket.gaierror:
        print("[-] Could not resolve target.")
        return False

    except KeyboardInterrupt:
        print("\n[!] Scan stopped.")
        raise SystemExit

    finally:
        sock.close()


def main():
    parser = argparse.ArgumentParser(
        description="Simple TCP port scanner for authorized labs."
    )

    parser.add_argument(
        "target",
        help="IP address or hostname to scan"
    )

    parser.add_argument(
        "-p",
        "--ports",
        default="1-1000",
        help="Port range, e.g. 1-1000 or 22,80,443"
    )

    args = parser.parse_args()

    target = args.target

    print("=" * 50)
    print("        Python TCP Port Scanner")
    print("=" * 50)
    print(f"Target: {target}")
    print(f"Ports:  {args.ports}")
    print()

    # Convert the port argument into a list
    if "-" in args.ports:
        start, end = map(int, args.ports.split("-"))
        ports = range(start, end + 1)

    else:
        ports = [int(port) for port in args.ports.split(",")]

    open_ports = []

    for port in ports:
        if scan_port(target, port):
            service = COMMON_SERVICES.get(port, "Unknown")
            print(f"[+] {port:<5} OPEN   {service}")
            open_ports.append(port)

    print()
    print("=" * 50)
    print(f"Scan complete. {len(open_ports)} open port(s) found.")
    print("=" * 50)


if __name__ == "__main__":
    main()
