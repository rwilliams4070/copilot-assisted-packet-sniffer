from scapy.all import *
from redaction import mask_ip, redact_sensitive_data
import argparse
log_file = open("sample_output/capture_log.txt", "a")

def packet_callback(packet):

    print("\n========== PACKET ==========")

    if IP in packet:
        src_ip = mask_ip(packet[IP].src)
        dst_ip = mask_ip(packet[IP].dst)

        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")

    if TCP in packet:
        print("Protocol: TCP")
        print(f"Source Port: {packet[TCP].sport}")
        print(f"Destination Port: {packet[TCP].dport}")

    elif UDP in packet:
        print("Protocol: UDP")
        print(f"Source Port: {packet[UDP].sport}")
        print(f"Destination Port: {packet[UDP].dport}")

    if DNS in packet and packet[DNS].qd:
        query = packet[DNS].qd.qname.decode()

        print(f"DNS Query: {query}")

    if Raw in packet:
        try:
            payload = packet[Raw].load.decode(errors="ignore")

            payload = redact_sensitive_data(payload)

            print("Payload:")
            print(payload[:500])
            log_file.write(payload[:500] + "\n\n")
            log_file.flush()

        except:
            pass

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--iface", default="lo")
    parser.add_argument("--count", type=int, default=25)
    parser.add_argument("--filter", default="")

    args = parser.parse_args()

    allowed_interfaces = ["lo", "eth0"]

    if args.iface not in allowed_interfaces:
        print("Interface not allowed")
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
