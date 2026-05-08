# Copilot-Assisted Packet Sniffer: Seeing the Network Ethically

## Introduction

The purpose of this project was to build a packet sniffer capable of safely capturing and decoding authorized network traffic in a controlled lab environment. The project focused on understanding packet capture concepts such as TCP, UDP, DNS, and HTTP traffic while implementing ethical safeguards to reduce the exposure of sensitive information. The project was developed using Python and the Scapy library inside a Kali Linux virtual machine.

The packet sniffer was designed to capture only local loopback traffic or instructor-approved lab traffic. Ethical restrictions were enforced throughout development to ensure the tool could not be used for unauthorized monitoring.

## Lab Environment and Tools

The project environment included:
- Kali Linux Virtual Machine
- Python 3.11
- Scapy
- GitHub
- GitHub Copilot
- Wireshark/TShark
- pytest

The loopback interface (`lo`) was used to safely generate and capture traffic locally on the virtual machine. HTTP traffic was generated using Python’s built-in HTTP server and the `curl` command. DNS traffic was generated using the `dig` command.

## Packet Capture and Decoding

The packet sniffer successfully captured and decoded:
- IP packets
- TCP traffic
- UDP traffic
- DNS queries
- HTTP request payloads

The project implemented BPF filtering to limit captures to specific traffic types such as:
- `tcp port 8000`
- `udp port 53`

Captured packets displayed source and destination IP addresses, ports, protocol information, and HTTP payloads.

## Ethical Redaction Features

One of the primary goals of the project was implementing ethical safeguards. Before packet data was displayed or written to log files, the program automatically redacted sensitive information.

The following information was masked:
- email addresses
- passwords
- authentication tokens
- portions of IP addresses

Examples included:
- `[REDACTED_EMAIL]`
- `password=[REDACTED]`
- `token=[REDACTED]`

This helped reduce the risk of exposing sensitive data during packet analysis.

## Logging and Testing

The sniffer also logged redacted payloads into a file located at:

```text
sample_output/capture_log.txt
