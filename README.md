# 🔍 Advanced Network Port Scanner

A high-performance, multi-threaded network port scanner with service detection and vulnerability assessment capabilities. Built for cybersecurity professionals and penetration testers.

## 🚀 Features

- **⚡ Multi-threaded Scanning** - Configurable thread count for optimal performance
- **🎯 Service Detection** - Identifies services running on open ports
- **📡 Banner Grabbing** - Attempts to fingerprint service versions
- **⚠️ Vulnerability Assessment** - Basic security analysis of discovered services
- **📊 Professional Reporting** - JSON export for further analysis
- **🔧 Flexible Configuration** - Customizable timeouts, port ranges, and thread counts
- **🛡️ Error Handling** - Robust handling of network errors and timeouts

## 📋 Requirements

- Python 3.6+
- No external dependencies (uses only standard library)

## 🛠️ Installation

1. Clone or download the scanner:
```bash
git clone <your-repo> port-scanner
cd port-scanner
```

2. Make it executable:
```bash
chmod +x scanner.py
```

## 💻 Usage

### Basic Scanning
```bash
# Scan common ports (1-1000)
python scanner.py 192.168.1.1

# Scan specific host
python scanner.py example.com
```

### Advanced Options
```bash
# Custom port range
python scanner.py target.com -p 1-65535

# Specific ports
python scanner.py 10.0.0.1 -p 22,80,443,8080

# Fast scan with custom settings
python scanner.py target.com -p 1-10000 -t 0.5 -T 200

# Generate detailed report
python scanner.py target.com -p 1-1000 -r
```

### Command Line Arguments

| Option | Description | Default |
|--------|-------------|---------|
| `target` | Target IP address or hostname | Required |
| `-p, --ports` | Port range (e.g., 1-1000, 80,443) | 1-1000 |
| `-t, --timeout` | Connection timeout in seconds | 1.0 |
| `-T, --threads` | Number of concurrent threads | 100 |
| `-r, --report` | Generate JSON report file | False |

## 📊 Sample Output

```
🚀 Advanced Port Scanner v2.0
📅 Scan started: 2024-08-26 15:30:45

🔍 Scanning example.com ports 1-1000
⚡ Using 100 threads for fast scanning
============================================================
PORT     STATE    SERVICE         BANNER
============================================================
[+]    22/tcp  OPEN   SSH             SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
[+]    80/tcp  OPEN   HTTP            HTTP/1.1 200 OK Server: nginx/1.18.0...
[+]   443/tcp  OPEN   HTTPS           
[+]  8080/tcp  OPEN   HTTP-Alt        

============================================================
✅ Scan completed in 12.34 seconds
🎯 Found 4 open ports on example.com

⚠️  SECURITY FINDINGS:
   • Port 22: SSH service detected - ensure strong authentication
```

## 📈 Performance Guidelines

| Target | Recommended Threads | Timeout | Expected Speed |
|--------|-------------------|---------|----------------|
| Internal Network | 200-500 | 0.1-0.5s | Very Fast |
| Internet Hosts | 50-100 | 1-2s | Fast |
| Slow/Distant Hosts | 20-50 | 2-5s | Moderate |

## 🔒 Service Detection

The scanner can identify these common services:

- **Web Services**: HTTP (80), HTTPS (443), HTTP-Alt (8080)
- **Remote Access**: SSH (22), Telnet (23), RDP (3389)
- **Email**: SMTP (25), POP3 (110), IMAP (143)
- **Databases**: MySQL (3306), PostgreSQL (5432), MongoDB (27017)
- **File Transfer**: FTP (21)
- **Other**: DNS (53), Redis (6379), Elasticsearch (9200)

## ⚠️ Vulnerability Checks

Basic security assessments include:
- Unencrypted protocols (Telnet, FTP)
- Exposed databases
- Remote desktop services
- Anonymous FTP access indicators

## 📄 Report Generation

When using the `-r` flag, detailed JSON reports are generated:

```json
{
  "target": "example.com",
  "scan_time": "2024-08-26T15:30:45.123456",
  "total_open_ports": 4,
  "open_ports": [
    {
      "port": 22,
      "service": "SSH",
      "banner": "SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1"
    }
  ],
  "vulnerabilities": [
    "Port 22: SSH service detected - ensure strong authentication"
  ]
}
```

## 🚨 Legal Notice

**IMPORTANT**: This tool is for educational purposes and authorized security testing only.

- ✅ **Authorized Use**: Your own networks, with written permission
- ❌ **Unauthorized Use**: Scanning networks without explicit permission
- ⚖️ **Legal Compliance**: Always comply with local laws and regulations
- 🛡️ **Responsible Disclosure**: Report vulnerabilities through proper channels

## 🔧 Troubleshooting

### Common Issues

**"Cannot resolve hostname"**
```bash
# Check DNS resolution
nslookup target.com
dig target.com
```

**Slow scanning performance**
```bash
# Reduce threads and increase timeout
python scanner.py target.com -T 50 -t 2
```

**Permission denied errors**
```bash
# Some systems require elevated privileges
sudo python scanner.py target.com
```

**Firewall blocking**
- Some firewalls may block or rate-limit port scans
- Try reducing thread count and increasing timeout
- Use different source ports or scan techniques

## 📚 Educational Value

This project demonstrates:
- **Network Programming**: Socket operations, TCP connections
- **Concurrency**: Threading and synchronization
- **Error Handling**: Robust exception management
- **Security Concepts**: Port scanning, service enumeration
- **Professional Development**: Clean code, documentation, CLI design

## 🤝 Contributing

Perfect for extending with additional features:
- UDP port scanning
- OS fingerprinting
- Advanced vulnerability checks
- GUI interface
- Integration with security frameworks

## 📞 Support

For questions or issues:
1. Check the troubleshooting section
2. Review command line options with `--help`
3. Verify target accessibility with basic tools (ping, nslookup)

---

**Built for cybersecurity education and authorized security testing** 🛡️
