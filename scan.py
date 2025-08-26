#!/usr/bin/env python3
"""
Advanced Network Port Scanner with Service Detection
Shows threading, error handling, and network programming skills
"""

import socket
import threading
import argparse
import sys
from datetime import datetime
import json

class PortScanner:
    def __init__(self, target, timeout=1):
        self.target = target
        self.timeout = timeout
        self.open_ports = []
        self.lock = threading.Lock()
        
        # Common service mappings for impressive service detection
        self.services = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 143: "IMAP", 443: "HTTPS", 993: "IMAPS",
            995: "POP3S", 3389: "RDP", 5432: "PostgreSQL", 3306: "MySQL",
            1433: "MSSQL", 6379: "Redis", 27017: "MongoDB", 5000: "Flask/Docker",
            8080: "HTTP-Alt", 9200: "Elasticsearch", 11211: "Memcached"
        }
    
    def scan_port(self, port):
        """Scan individual port with banner grabbing"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(self.timeout)
                result = sock.connect_ex((self.target, port))
                
                if result == 0:  # Port is open
                    service = self.services.get(port, "Unknown")
                    banner = self.grab_banner(sock, port)
                    
                    with self.lock:
                        self.open_ports.append({
                            'port': port,
                            'service': service,
                            'banner': banner
                        })
                        print(f"[+] {port:5d}/tcp  OPEN   {service:15s} {banner}")
        
        except Exception as e:
            pass  # Silently ignore connection errors
    
    def grab_banner(self, sock, port):
        """Attempt to grab service banner for fingerprinting"""
        try:
            # Send appropriate probe based on service
            if port == 80 or port == 8080:
                sock.send(b"GET / HTTP/1.1\r\nHost: " + self.target.encode() + b"\r\n\r\n")
            elif port == 21:
                pass  # FTP sends banner automatically
            elif port == 22:
                pass  # SSH sends banner automatically
            else:
                sock.send(b"\r\n")
            
            banner = sock.recv(1024).decode('utf-8', errors='ignore').strip()
            return banner[:50] + "..." if len(banner) > 50 else banner
        
        except:
            return ""
    
    def scan_range(self, start_port, end_port, threads=100):
        """Threaded port scanning for speed"""
        print(f"\n🔍 Scanning {self.target} ports {start_port}-{end_port}")
        print(f"⚡ Using {threads} threads for fast scanning")
        print("=" * 60)
        print(f"{'PORT':<8} {'STATE':<8} {'SERVICE':<15} {'BANNER'}")
        print("=" * 60)
        
        # Create and start threads
        thread_list = []
        for port in range(start_port, end_port + 1):
            thread = threading.Thread(target=self.scan_port, args=(port,))
            thread_list.append(thread)
            thread.start()
            
            # Limit concurrent threads
            if len(thread_list) >= threads:
                for t in thread_list:
                    t.join()
                thread_list = []
        
        # Wait for remaining threads
        for thread in thread_list:
            thread.join()
    
    def vulnerability_check(self):
        """Basic vulnerability assessment based on open ports"""
        vulns = []
        
        for port_info in self.open_ports:
            port = port_info['port']
            service = port_info['service']
            
            # Common vulnerability patterns
            if port == 21 and "FTP" in service:
                vulns.append(f"Port {port}: FTP may allow anonymous access")
            elif port == 23 and "Telnet" in service:
                vulns.append(f"Port {port}: Telnet sends data in plaintext")
            elif port == 3389:
                vulns.append(f"Port {port}: RDP exposed - potential brute force target")
            elif port in [1433, 3306, 5432]:
                vulns.append(f"Port {port}: Database directly exposed to network")
        
        return vulns
    
    def generate_report(self):
        """Generate professional security assessment report"""
        report = {
            'target': self.target,
            'scan_time': datetime.now().isoformat(),
            'total_open_ports': len(self.open_ports),
            'open_ports': self.open_ports,
            'vulnerabilities': self.vulnerability_check()
        }
        
        # Save JSON report
        filename = f"scan_{self.target.replace('.', '_')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=2)
        
        return filename

def main():
    parser = argparse.ArgumentParser(description='Advanced Network Port Scanner')
    parser.add_argument('target', help='Target IP or hostname')
    parser.add_argument('-p', '--ports', default='1-1000', help='Port range (default: 1-1000)')
    parser.add_argument('-t', '--timeout', type=float, default=1.0, help='Connection timeout (default: 1.0)')
    parser.add_argument('-T', '--threads', type=int, default=100, help='Number of threads (default: 100)')
    parser.add_argument('-r', '--report', action='store_true', help='Generate JSON report')
    
    args = parser.parse_args()
    
    # Parse port range
    if '-' in args.ports:
        start_port, end_port = map(int, args.ports.split('-'))
    else:
        start_port = end_port = int(args.ports)
    
    # Validate target
    try:
        socket.gethostbyname(args.target)
    except socket.gaierror:
        print(f"❌ Error: Cannot resolve hostname '{args.target}'")
        sys.exit(1)
    
    # Start scanning
    print(f"🚀 Advanced Port Scanner v2.0")
    print(f"📅 Scan started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    scanner = PortScanner(args.target, args.timeout)
    start_time = datetime.now()
    
    scanner.scan_range(start_port, end_port, args.threads)
    
    scan_duration = (datetime.now() - start_time).total_seconds()
    
    # Results summary
    print("\n" + "=" * 60)
    print(f"✅ Scan completed in {scan_duration:.2f} seconds")
    print(f"🎯 Found {len(scanner.open_ports)} open ports on {args.target}")
    
    # Vulnerability assessment
    vulns = scanner.vulnerability_check()
    if vulns:
        print(f"\n⚠️  SECURITY FINDINGS:")
        for vuln in vulns:
            print(f"   • {vuln}")
    
    # Generate report if requested
    if args.report:
        report_file = scanner.generate_report()
        print(f"\n📄 Detailed report saved to: {report_file}")

if __name__ == "__main__":
    main()
