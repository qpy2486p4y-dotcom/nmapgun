# nmapgun



import socket

target = input("Enter your lab IP: ")

ports = [21, 22, 25, 53, 80, 110, 139, 443, 445, 3389]

print(f"\nScanning {target}...\n")

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"{port:<5} OPEN")
    else:
        print(f"{port:<5} CLOSED")

    sock.close()
