from scapy.all import sniff
import argparse

def packet_callback(packet):
    print(packet.summary())

def main():
    parser = argparse.ArgumentParser(description="Ethical packet sniffer for lab traffic only")
    parser.add_argument("--iface", default="lo", help="Interface to sniff on")
    parser.add_argument("--count", type=int, default=25, help="Number of packets to capture")
    parser.add_argument("--filter", default="", help="BPF filter, example: udp port 53")

    args = parser.parse_args()

    allowed_interfaces = ["lo", "eth0"]

    if args.iface not in allowed_interfaces:
        print(f"[!] Interface {args.iface} is not allowed.")
        print(f"[!] Allowed interfaces: {allowed_interfaces}")
        return

    print(f"[*] Starting capture on interface: {args.iface}")
    print(f"[*] Packet count: {args.count}")
    print(f"[*] Filter: {args.filter}")

    sniff(
        iface=args.iface,
        count=args.count,
        filter=args.filter,
        prn=packet_callback,
        store=False
    )

if __name__ == "__main__":
    main()
