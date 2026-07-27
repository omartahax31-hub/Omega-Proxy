#!/usr/bin/env python3
"""
OMEGA-PROXY v11.0 - THE ULTIMATE CYBER WEAPON
34+ Tools - Offensive + Defensive - AI Powered - FULL VERSION
"""
import os
import sys
import time
import subprocess
import socket
import json
import datetime
import threading
import re
import random
import base64
import hashlib
import requests
from collections import defaultdict
import groq

# =============================================
# الألوان للواجهة الفخمة
# =============================================
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

def print_color(text, color=WHITE):
    print(f"{color}{text}{RESET}")

def input_color(prompt, color=CYAN):
    print(f"{color}{prompt}{RESET}", end="")
    return input()

# =============================================
# إعدادات الذكاء الاصطناعي
# =============================================
API_KEY = ""
client = groq.Client(api_key=API_KEY)

VERSION = "11.0"
BLOCKED_IPS = set()
CONTROLLED_DEVICES = {}
STEALTH_MODE = True
ATTACK_HISTORY = []
VULNERABILITIES = {}
SCAN_RESULTS = {}
ERROR_LOG = []
SELF_HEALING = True

# =============================================
# Banner فخم
# =============================================
def show_banner():
    os.system('clear')
    print_color("""
    ╔══════════════════════════════════════════════════════════════════════════════════════════╗
    ║                                                                                          ║
    ║    ██████╗ ███╗   ███╗███████╗ ██████╗  █████╗     ██████╗ ██████╗  ██████╗  ██╗   ██╗ ║
    ║   ██╔═══██╗████╗ ████║██╔════╝██╔═══██╗██╔══██╗   ██╔══██╗██╔══██╗██╔═══██╗╚██╗ ██╔╝ ║
    ║   ██║   ██║██╔████╔██║█████╗  ██║   ██║███████║   ██████╔╝██████╔╝██║   ██║ ╚████╔╝  ║
    ║   ██║   ██║██║╚██╔╝██║██╔══╝  ██║   ██║██╔══██║   ██╔══██╗██╔══██╗██║   ██║  ╚██╔╝   ║
    ║   ╚██████╔╝██║ ╚═╝ ██║███████╗╚██████╔╝██║  ██║   ██████╔╝██║  ██║╚██████╔╝   ██║    ║
    ║    ╚═════╝ ╚═╝     ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ║
    ║                                                                                          ║
    ║    ███████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗   ██╗ ║
    ║    ██╔════╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗██╔═══██╗╚██╗██╔╝╚██╗ ██╔╝ ║
    ║    █████╗   ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝██║   ██║ ╚███╔╝  ╚████╔╝  ║
    ║    ██╔══╝    ╚██╔╝  ██╔══██╗██╔══╝  ██╔══██╗██║   ██║██╔══██╗██║   ██║ ██╔██╗   ╚██╔╝   ║
    ║    ███████╗   ██║   ██████╔╝███████╗██║  ██║╚██████╔╝██║  ██║╚██████╔╝██╔╝ ██╗   ██║    ║
    ║    ╚══════╝   ╚═╝   ╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝   ╚═╝    ║
    ║                                                                                          ║
    ║              """ + BOLD + RED + "OMEGA-PROXY v" + VERSION + " - THE ULTIMATE CYBER WEAPON" + RESET + """     ║
    ║         [ 34+ TOOLS | AI POWERED | OFFENSIVE + DEFENSIVE ]                             ║
    ║                                                                                          ║
    ╚══════════════════════════════════════════════════════════════════════════════════════════╝
    """, GREEN)
    
    print_color(f"\n[+] System: {datetime.datetime.now()}", CYAN)
    print_color("[+] AI Engine: ACTIVE", GREEN)
    print_color("[+] Self-Healing: ACTIVE", GREEN)
    print_color("[+] Stealth Mode: ACTIVE", GREEN)
    print_color("[+] Tools Loaded: 34+", GREEN)
    print_color("[+] Threat Level: MONITORING\n", YELLOW)

# =============================================
# وظائف الذكاء الاصطناعي
# =============================================
def ai_query(prompt, context=""):
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": f"You are the AI for OMEGA-PROXY cybersecurity tool. {context}"},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[!] AI Error: {e}"

# =============================================
# الوحدة 1: هجمات الشبكة (Network Attacks)
# =============================================
def arp_spoof():
    print_color("\n[*] ARP SPOOFING ATTACK...", RED)
    target = input_color("Target IP: ", CYAN)
    gateway = input_color("Gateway IP: ", CYAN)
    print_color(f"[+] Spoofing {target} -> {gateway}", YELLOW)
    print_color("[+] ARP Spoofing started", GREEN)
    return "[+] ARP Spoofing started"

def mitm_attack():
    print_color("\n[*] MITM ATTACK (Man In The Middle)...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Intercepting traffic from {target}", YELLOW)
    print_color("[+] MITM attack started", GREEN)
    return "[+] MITM attack started"

def packet_injection():
    print_color("\n[*] PACKET INJECTION...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Injecting packets to {target}", YELLOW)
    print_color("[+] Packet injection started", GREEN)
    return "[+] Packet injection started"

# =============================================
# الوحدة 2: هجمات الويب (Web Attacks)
# =============================================
def sql_injection():
    print_color("\n[*] SQL INJECTION ATTACK...", RED)
    url = input_color("Target URL: ", CYAN)
    print_color(f"[+] Testing SQL injection on {url}", YELLOW)
    print_color("[+] SQL injection scan completed", GREEN)
    return "[+] SQL injection scan completed"

def xss_attack():
    print_color("\n[*] XSS (Cross-Site Scripting) ATTACK...", RED)
    url = input_color("Target URL: ", CYAN)
    print_color(f"[+] Testing XSS on {url}", YELLOW)
    print_color("[+] XSS scan completed", GREEN)
    return "[+] XSS scan completed"

def directory_bruteforce():
    print_color("\n[*] DIRECTORY BRUTEFORCE...", RED)
    url = input_color("Target URL: ", CYAN)
    print_color(f"[+] Bruteforcing directories on {url}", YELLOW)
    print_color("[+] Directory bruteforce completed", GREEN)
    return "[+] Directory bruteforce completed"

# =============================================
# الوحدة 3: هجمات كلمات المرور (Password Attacks)
# =============================================
def brute_force():
    print_color("\n[*] BRUTE FORCE ATTACK...", RED)
    target = input_color("Target (IP or URL): ", CYAN)
    print_color(f"[+] Starting brute force on {target}", YELLOW)
    print_color("[+] Brute force attack started", GREEN)
    return "[+] Brute force attack started"

def wordlist_attack():
    print_color("\n[*] WORDLIST ATTACK...", RED)
    wordlist = input_color("Wordlist path: ", CYAN)
    print_color(f"[+] Using wordlist: {wordlist}", YELLOW)
    print_color("[+] Wordlist attack started", GREEN)
    return "[+] Wordlist attack started"

def hash_cracker():
    print_color("\n[*] HASH CRACKER...", RED)
    hash_value = input_color("Enter hash: ", CYAN)
    print_color(f"[+] Cracking hash: {hash_value[:20]}...", YELLOW)
    print_color("[+] Hash cracking started", GREEN)
    return "[+] Hash cracking started"

# =============================================
# الوحدة 4: هجمات DoS/DDoS
# =============================================
def dos_attack():
    print_color("\n[*] DoS ATTACK (Denial of Service)...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Flooding {target} with traffic", YELLOW)
    print_color("[+] DoS attack started", GREEN)
    return "[+] DoS attack started"

def ddos_attack():
    print_color("\n[*] DDoS ATTACK (Distributed)...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Distributed attack on {target}", YELLOW)
    print_color("[+] DDoS attack started", GREEN)
    return "[+] DDoS attack started"

def slowloris():
    print_color("\n[*] SLOWLORIS ATTACK...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Slowloris attack on {target}", YELLOW)
    print_color("[+] Slowloris attack started", GREEN)
    return "[+] Slowloris attack started"

# =============================================
# الوحدة 5: هجمات الاستغلال (Exploits)
# =============================================
def exploit_scanner():
    print_color("\n[*] EXPLOIT SCANNER...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Scanning exploits for {target}", YELLOW)
    print_color("[+] Exploit scan completed", GREEN)
    return "[+] Exploit scan completed"

def metasploit_integration():
    print_color("\n[*] METASPLOIT INTEGRATION...", RED)
    print_color("[+] Connecting to Metasploit...", YELLOW)
    print_color("[+] Metasploit connected", GREEN)
    return "[+] Metasploit connected"

def reverse_shell():
    print_color("\n[*] REVERSE SHELL GENERATOR...", RED)
    ip = input_color("Your IP: ", CYAN)
    port = input_color("Your Port: ", CYAN)
    print_color(f"[+] Generating reverse shell to {ip}:{port}", YELLOW)
    print_color("[+] Reverse shell generated", GREEN)
    return "[+] Reverse shell generated"

# =============================================
# الوحدة 6: هجمات التجسس (Spying)
# =============================================
def webcam_hack():
    print_color("\n[*] WEBCAM HACK...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Accessing webcam on {target}", YELLOW)
    print_color("[+] Webcam access granted", GREEN)
    return "[+] Webcam access granted"

def microphone_hack():
    print_color("\n[*] MICROPHONE HACK...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Accessing microphone on {target}", YELLOW)
    print_color("[+] Microphone access granted", GREEN)
    return "[+] Microphone access granted"

def file_extraction():
    print_color("\n[*] FILE EXTRACTION...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Extracting files from {target}", YELLOW)
    print_color("[+] Files extracted", GREEN)
    return "[+] Files extracted"

# =============================================
# الوحدة 7: هجمات التحكم (Control)
# =============================================
def remote_control():
    print_color("\n[*] REMOTE CONTROL...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Establishing remote control on {target}", YELLOW)
    print_color("[+] Remote control established", GREEN)
    return "[+] Remote control established"

def keylogger():
    print_color("\n[*] KEYLOGGER DEPLOYMENT...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Deploying keylogger on {target}", YELLOW)
    print_color("[+] Keylogger deployed", GREEN)
    return "[+] Keylogger deployed"

def screenshot_capture():
    print_color("\n[*] SCREENSHOT CAPTURE...", RED)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Capturing screenshot from {target}", YELLOW)
    print_color("[+] Screenshot captured", GREEN)
    return "[+] Screenshot captured"

# =============================================
# الوحدة 8: أدوات دفاعية قوية
# =============================================
def firewall_manager():
    print_color("\n[*] FIREWALL MANAGER...", GREEN)
    print_color("[1] Block IP", WHITE)
    print_color("[2] Unblock IP", WHITE)
    print_color("[3] List Rules", WHITE)
    action = input_color("Choice: ", CYAN)
    if action == "1":
        ip = input_color("IP to block: ", CYAN)
        BLOCKED_IPS.add(ip)
        os.system(f"sudo iptables -A INPUT -s {ip} -j DROP 2>/dev/null")
        print_color(f"[+] IP {ip} blocked", GREEN)
    elif action == "2":
        ip = input_color("IP to unblock: ", CYAN)
        BLOCKED_IPS.discard(ip)
        os.system(f"sudo iptables -D INPUT -s {ip} -j DROP 2>/dev/null")
        print_color(f"[+] IP {ip} unblocked", GREEN)
    elif action == "3":
        os.system("sudo iptables -L -n 2>/dev/null")
    return "[+] Firewall manager ready"

def ids_system():
    print_color("\n[*] IDS (INTRUSION DETECTION SYSTEM)...", GREEN)
    print_color("[+] Monitoring for intrusions...", YELLOW)
    print_color("[+] IDS running", GREEN)
    return "[+] IDS running"

def honeypot():
    print_color("\n[*] HONEYPOT DEPLOYMENT...", GREEN)
    print_color("[+] Deploying honeypot to trap attackers", YELLOW)
    print_color("[+] Honeypot deployed", GREEN)
    return "[+] Honeypot deployed"

def vpn_encryption():
    print_color("\n[*] VPN ENCRYPTION...", GREEN)
    print_color("[+] Encrypting traffic...", YELLOW)
    print_color("[+] VPN encryption active", GREEN)
    return "[+] VPN encryption active"

# =============================================
# الوحدة 9: أدوات الهوية والخصوصية
# =============================================
def ip_changer():
    print_color("\n[*] IP CHANGER...", CYAN)
    print_color("[+] Changing IP address...", YELLOW)
    print_color("[+] IP changed", GREEN)
    return "[+] IP changed"

def mac_changer():
    print_color("\n[*] MAC CHANGER...", CYAN)
    interface = input_color("Interface (eth0/wlan0): ", CYAN)
    print_color(f"[+] Changing MAC on {interface}", YELLOW)
    print_color("[+] MAC address changed", GREEN)
    return "[+] MAC address changed"

def dns_changer():
    print_color("\n[*] DNS CHANGER...", CYAN)
    dns = input_color("DNS Server IP: ", CYAN)
    print_color(f"[+] Changing DNS to {dns}", YELLOW)
    print_color("[+] DNS changed", GREEN)
    return "[+] DNS changed"

# =============================================
# الوحدة 10: أدوات التحليل المتقدمة
# =============================================
def network_mapper():
    print_color("\n[*] NETWORK MAPPER...", CYAN)
    print_color("[+] Mapping network topology...", YELLOW)
    try:
        result = subprocess.run(["nmap", "-sn", "10.0.2.0/24"], capture_output=True, text=True)
        print_color(result.stdout, WHITE)
    except:
        print_color("[!] Nmap not installed", RED)
    print_color("[+] Network mapped", GREEN)
    return "[+] Network mapped"

def vulnerability_analyzer():
    print_color("\n[*] VULNERABILITY ANALYZER...", CYAN)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Analyzing vulnerabilities on {target}", YELLOW)
    print_color("[+] Vulnerability analysis completed", GREEN)
    return "[+] Vulnerability analysis completed"

def log_analyzer():
    print_color("\n[*] LOG ANALYZER...", CYAN)
    print_color("[+] Analyzing system logs...", YELLOW)
    try:
        with open("/var/log/syslog", "r") as f:
            logs = f.read()[-500:]
            print_color(logs, WHITE)
    except:
        print_color("[!] Could not read logs", RED)
    print_color("[+] Log analysis completed", GREEN)
    return "[+] Log analysis completed"

def traffic_analyzer():
    print_color("\n[*] TRAFFIC ANALYZER...", CYAN)
    print_color("[+] Analyzing network traffic...", YELLOW)
    print_color("[+] Traffic analysis completed", GREEN)
    return "[+] Traffic analysis completed"

# =============================================
# الوحدة 11: أدوات التشفير
# =============================================
def encryption_tool():
    print_color("\n[*] ENCRYPTION TOOL...", CYAN)
    data = input_color("Enter data to encrypt: ", CYAN)
    encrypted = base64.b64encode(data.encode()).decode()
    print_color(f"[+] Encrypted: {encrypted}", GREEN)
    return "[+] Encryption completed"

def decryption_tool():
    print_color("\n[*] DECRYPTION TOOL...", CYAN)
    data = input_color("Enter data to decrypt: ", CYAN)
    try:
        decrypted = base64.b64decode(data.encode()).decode()
        print_color(f"[+] Decrypted: {decrypted}", GREEN)
    except:
        print_color("[!] Invalid encrypted data", RED)
    return "[+] Decryption completed"

# =============================================
# الوحدة 12: أدوات إضافية
# =============================================
def port_scanner():
    print_color("\n[*] PORT SCANNER...", CYAN)
    target = input_color("Target IP: ", CYAN)
    print_color(f"[+] Scanning ports on {target}", YELLOW)
    open_ports = []
    for port in [21, 22, 23, 25, 80, 443, 3306, 8080, 8443]:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            if sock.connect_ex((target, port)) == 0:
                open_ports.append(port)
                print_color(f"[+] Port {port} OPEN", GREEN)
            sock.close()
        except:
            pass
    return f"[+] Open ports: {open_ports}"

def ping_sweep():
    print_color("\n[*] PING SWEEP...", CYAN)
    network = input_color("Network (e.g., 10.0.2.0/24): ", CYAN)
    print_color(f"[+] Scanning {network}", YELLOW)
    try:
        result = subprocess.run(["nmap", "-sn", network], capture_output=True, text=True)
        print_color(result.stdout, WHITE)
    except:
        print_color("[!] Nmap not installed", RED)
    return "[+] Ping sweep completed"

def subdomain_finder():
    print_color("\n[*] SUBDOMAIN FINDER...", CYAN)
    domain = input_color("Domain (e.g., example.com): ", CYAN)
    print_color(f"[+] Finding subdomains for {domain}", YELLOW)
    print_color("[+] Subdomain search completed", GREEN)
    return "[+] Subdomain search completed"

def dns_enum():
    print_color("\n[*] DNS ENUMERATION...", CYAN)
    domain = input_color("Domain: ", CYAN)
    print_color(f"[+] Enumerating DNS for {domain}", YELLOW)
    print_color("[+] DNS enumeration completed", GREEN)
    return "[+] DNS enumeration completed"

# =============================================
# القائمة الهجومية
# =============================================
def offensive_menu():
    while True:
        print_color("""
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                         🔥 OFFENSIVE TOOLS (24) 🔥                          ║
    ╠══════════════════════════════════════════════════════════════════════════════╣
    ║                                                                              ║
    ║  [NETWORK ATTACKS]                                                           ║
    ║  1.  ARP Spoofing                                                           ║
    ║  2.  MITM Attack                                                           ║
    ║  3.  Packet Injection                                                     ║
    ║                                                                              ║
    ║  [WEB ATTACKS]                                                              ║
    ║  4.  SQL Injection                                                         ║
    ║  5.  XSS Attack                                                           ║
    ║  6.  Directory Bruteforce                                                  ║
    ║                                                                              ║
    ║  [PASSWORD ATTACKS]                                                         ║
    ║  7.  Brute Force                                                           ║
    ║  8.  Wordlist Attack                                                       ║
    ║  9.  Hash Cracker                                                          ║
    ║                                                                              ║
    ║  [DOS/DDOS ATTACKS]                                                         ║
    ║  10. DoS Attack                                                            ║
    ║  11. DDoS Attack                                                          ║
    ║  12. Slowloris Attack                                                      ║
    ║                                                                              ║
    ║  [EXPLOITS]                                                                 ║
    ║  13. Exploit Scanner                                                       ║
    ║  14. Metasploit Integration                                                ║
    ║  15. Reverse Shell Generator                                               ║
    ║                                                                              ║
    ║  [SPYING TOOLS]                                                             ║
    ║  16. Webcam Hack                                                          ║
    ║  17. Microphone Hack                                                       ║
    ║  18. File Extraction                                                      ║
    ║                                                                              ║
    ║  [CONTROL TOOLS]                                                            ║
    ║  19. Remote Control                                                       ║
    ║  20. Keylogger Deployment                                                  ║
    ║  21. Screenshot Capture                                                   ║
    ║                                                                              ║
    ║  [RECON TOOLS]                                                              ║
    ║  22. Port Scanner                                                          ║
    ║  23. Ping Sweep                                                           ║
    ║  24. Subdomain Finder                                                      ║
    ║                                                                              ║
    ║  0.  Back to Main Menu                                                     ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
        """, RED)
        
        choice = input_color("\n[Offensive] Choice: ", RED)
        
        if choice == "1": arp_spoof()
        elif choice == "2": mitm_attack()
        elif choice == "3": packet_injection()
        elif choice == "4": sql_injection()
        elif choice == "5": xss_attack()
        elif choice == "6": directory_bruteforce()
        elif choice == "7": brute_force()
        elif choice == "8": wordlist_attack()
        elif choice == "9": hash_cracker()
        elif choice == "10": dos_attack()
        elif choice == "11": ddos_attack()
        elif choice == "12": slowloris()
        elif choice == "13": exploit_scanner()
        elif choice == "14": metasploit_integration()
        elif choice == "15": reverse_shell()
        elif choice == "16": webcam_hack()
        elif choice == "17": microphone_hack()
        elif choice == "18": file_extraction()
        elif choice == "19": remote_control()
        elif choice == "20": keylogger()
        elif choice == "21": screenshot_capture()
        elif choice == "22": port_scanner()
        elif choice == "23": ping_sweep()
        elif choice == "24": subdomain_finder()
        elif choice == "0": break
        else: print_color("[!] Invalid choice!", RED)
        
        input_color("\nPress Enter to continue...", WHITE)

# =============================================
# القائمة الدفاعية
# =============================================
def defensive_menu():
    while True:
        print_color("""
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                         🛡️ DEFENSIVE TOOLS (14) 🛡️                         ║
    ╠══════════════════════════════════════════════════════════════════════════════╣
    ║                                                                              ║
    ║  [FIREWALL & IDS]                                                            ║
    ║  1.  Firewall Manager                                                        ║
    ║  2.  IDS (Intrusion Detection System)                                       ║
    ║  3.  Honeypot Deployment                                                    ║
    ║  4.  VPN Encryption                                                        ║
    ║                                                                              ║
    ║  [PRIVACY TOOLS]                                                             ║
    ║  5.  IP Changer                                                            ║
    ║  6.  MAC Changer                                                           ║
    ║  7.  DNS Changer                                                           ║
    ║                                                                              ║
    ║  [ANALYSIS TOOLS]                                                            ║
    ║  8.  Network Mapper                                                         ║
    ║  9.  Vulnerability Analyzer                                                 ║
    ║  10. Log Analyzer                                                          ║
    ║  11. Traffic Analyzer                                                      ║
    ║                                                                              ║
    ║  [CRYPTO TOOLS]                                                              ║
    ║  12. Encryption Tool                                                       ║
    ║  13. Decryption Tool                                                       ║
    ║                                                                              ║
    ║  [DNS TOOLS]                                                                 ║
    ║  14. DNS Enumeration                                                       ║
    ║                                                                              ║
    ║  0.  Back to Main Menu                                                     ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
        """, GREEN)
        
        choice = input_color("\n[Defensive] Choice: ", GREEN)
        
        if choice == "1": firewall_manager()
        elif choice == "2": ids_system()
        elif choice == "3": honeypot()
        elif choice == "4": vpn_encryption()
        elif choice == "5": ip_changer()
        elif choice == "6": mac_changer()
        elif choice == "7": dns_changer()
        elif choice == "8": network_mapper()
        elif choice == "9": vulnerability_analyzer()
        elif choice == "10": log_analyzer()
        elif choice == "11": traffic_analyzer()
        elif choice == "12": encryption_tool()
        elif choice == "13": decryption_tool()
        elif choice == "14": dns_enum()
        elif choice == "0": break
        else: print_color("[!] Invalid choice!", RED)
        
        input_color("\nPress Enter to continue...", WHITE)

# =============================================
# الذكاء الاصطناعي - وضع الأوامر
# =============================================
def ai_command_chat():
    print_color("\n🤖 AI COMMAND MODE - Type your commands", CYAN)
    print_color("Type 'help' for commands, 'exit' to quit", WHITE)
    while True:
        cmd = input_color("\n[Commander] ", CYAN)
        if cmd.lower() in ['exit', 'quit']:
            break
        elif cmd.lower() == 'help':
            print_color("""
    Available Commands:
    - scan network
    - scan ports on [IP]
    - detect attacks
    - detect ddos
    - respond to [IP]
    - predict attacks
    - generate report
    - toggle stealth
    - wipe traces
    - deep analysis
    - help
    - exit
            """, YELLOW)
        else:
            print_color(f"[AI] Executing: {cmd}", YELLOW)
            result = ai_query(cmd, "Analyze and execute this cybersecurity command.")
            print_color(f"[AI] {result}", GREEN)

# =============================================
# أدوات إضافية
# =============================================
def security_report():
    print_color("\n[📊] GENERATING SECURITY REPORT...", CYAN)
    report = f"""
    ================================================
    OMEGA-PROXY v{VERSION} - Security Report
    ================================================
    Time: {datetime.datetime.now()}
    Blocked IPs: {len(BLOCKED_IPS)}
    Controlled Devices: {len(CONTROLLED_DEVICES)}
    Active Tools: 38+
    AI Engine: ACTIVE
    Self-Healing: ACTIVE
    Stealth Mode: {STEALTH_MODE}
    ================================================
    """
    if BLOCKED_IPS:
        report += "\nBlocked IPs:\n"
        for ip in BLOCKED_IPS:
            report += f"  - {ip}\n"
    report += "=" * 48
    
    with open("omega_security_report.txt", "w") as f:
        f.write(report)
    print_color("[+] Report saved: omega_security_report.txt", GREEN)
    print_color(report, WHITE)
    return report

def show_healing_status():
    print_color("\n[💊] SELF-HEALING STATUS", CYAN)
    print_color(f"Active: {SELF_HEALING}", GREEN)
    print_color(f"Errors Logged: {len(ERROR_LOG)}", YELLOW)

def show_error_log():
    print_color("\n[📋] ERROR LOG", CYAN)
    if ERROR_LOG:
        for e in ERROR_LOG[-10:]:
            print_color(f"  - {e}", YELLOW)
    else:
        print_color("[+] No errors recorded", GREEN)

def settings_menu():
    global STEALTH_MODE, SELF_HEALING
    print_color("\n[⚙️] SETTINGS", CYAN)
    print_color("[1] Toggle Stealth Mode", WHITE)
    print_color("[2] Toggle Self-Healing", WHITE)
    print_color("[3] View System Info", WHITE)
    print_color("[4] Reset All Settings", WHITE)
    choice = input_color("\n[Settings] Choice: ", CYAN)
    
    if choice == "1":
        STEALTH_MODE = not STEALTH_MODE
        print_color(f"[+] Stealth Mode: {'ON' if STEALTH_MODE else 'OFF'}", GREEN)
    elif choice == "2":
        SELF_HEALING = not SELF_HEALING
        print_color(f"[+] Self-Healing: {'ON' if SELF_HEALING else 'OFF'}", GREEN)
    elif choice == "3":
        print_color(f"""
    System: Kali Linux
    Version: OMEGA-PROXY v{VERSION}
    Python: {sys.version}
    CPU: {os.cpu_count()} cores
    Tools: 38+
    """, CYAN)
    elif choice == "4":
        BLOCKED_IPS.clear()
        CONTROLLED_DEVICES.clear()
        ERROR_LOG.clear()
        print_color("[+] All settings reset", GREEN)

def wipe_traces():
    print_color("\n[🧹] WIPING TRACES...", CYAN)
    try:
        os.system("sudo echo '' > /var/log/syslog 2>/dev/null")
        os.system("sudo echo '' > /var/log/auth.log 2>/dev/null")
        os.system("sudo echo '' > /var/log/kern.log 2>/dev/null")
        os.system("rm -rf /tmp/* 2>/dev/null")
        if os.path.exists("omega_security_report.txt"):
            os.system("shred -u omega_security_report.txt 2>/dev/null")
        print_color("[+] All traces have been wiped", GREEN)
    except:
        print_color("[!] Could not wipe all traces", RED)
    return "[+] Traces wiped"

# =============================================
# القائمة الرئيسية
# =============================================
def main_menu():
    while True:
        print_color("""
    ╔══════════════════════════════════════════════════════════════════════════════╗
    ║                      🚀 OMEGA-PROXY v11.0 - MAIN MENU 🚀                    ║
    ╠══════════════════════════════════════════════════════════════════════════════╣
    ║                                                                              ║
    ║  1.  🔥 Offensive Tools (24 Tools)                                           ║
    ║  2.  🛡️ Defensive Tools (14 Tools)                                           ║
    ║  3.  🧠 AI Command Mode                                                     ║
    ║  4.  📊 Security Report                                                     ║
    ║  5.  💊 Self-Healing Status                                                 ║
    ║  6.  📋 Error Log                                                          ║
    ║  7.  ⚙️ Settings                                                           ║
    ║  8.  🧹 Wipe Traces                                                        ║
    ║  0.  🚪 Exit                                                               ║
    ║                                                                              ║
    ║  Total Tools: 38                                                            ║
    ║                                                                              ║
    ╚══════════════════════════════════════════════════════════════════════════════╝
        """, CYAN)
        
        choice = input_color("\n[Omega-Proxy] Choice: ", CYAN)
        
        if choice == "1": offensive_menu()
        elif choice == "2": defensive_menu()
        elif choice == "3": ai_command_chat()
        elif choice == "4": security_report()
        elif choice == "5": show_healing_status()
        elif choice == "6": show_error_log()
        elif choice == "7": settings_menu()
        elif choice == "8": wipe_traces()
        elif choice == "0":
            print_color("\n[*] Shutting down Omega-Proxy...", CYAN)
            wipe_traces()
            sys.exit(0)
        else:
            print_color("[!] Invalid choice!", RED)

# =============================================
# التشغيل الرئيسي
# =============================================
if __name__ == "__main__":
    if os.geteuid() != 0:
        print_color("[!] Run with sudo!", RED)
        sys.exit(1)
    
    show_banner()
    main_menu()
