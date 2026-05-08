# Copilot-Assisted Packet Sniffer: Seeing the Network Ethically

## Project Overview
This project is a lab-safe packet sniffer built with Python and Scapy. It captures authorized local traffic, decodes basic TCP, UDP, DNS, and HTTP information, and redacts sensitive data before displaying or logging output.

## Ethics Statement
This tool is for educational use only. It may only be used on my own machine, loopback interface, or an instructor-approved lab network. It must not be used to capture other people’s traffic.

## Features
- Captures loopback traffic using Scapy
- Supports BPF filters such as `tcp port 8000` and `udp port 53`
- Decodes IP, TCP, UDP, DNS, and HTTP payloads
- Masks IP addresses
- Redacts emails, passwords, and tokens
- Saves redacted output to `sample_output/capture_log.txt`
- Includes unit tests for redaction

## Setup
```bash
sudo apt update
sudo apt install python3 python3-pip git wireshark tshark -y
pip install scapy pytest

## Run Examples

HTTP capture:

```bash
sudo python3 ./sniffer.py --iface lo --count 25 --filter "tcp port 8000"
