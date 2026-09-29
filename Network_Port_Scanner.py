import socket
import ipaddress
import concurrent.futures
from datetime import datetime

def is_port_open(target, port, timeout=1):
    """
    Check if a specific port is open on a target host
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((target, port))
            return True
    except:
        return False

def scan_ports(target, start_port=1, end_port=1024):
    """
    Scan a range of ports on a target host
    """
    open_ports = []
    print(f"\nScanning {target} from port {start_port} to {end_port}...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(is_port_open, target, port): port 
                  for port in range(start_port, end_port + 1)}
        
        for future in concurrent.futures.as_completed(futures):
            port = futures[future]
            if future.result():
                open_ports.append(port)
                try:
                    service = socket.getservbyport(port)
                except:
                    service = "unknown"
                print(f"🔍 Port {port} is open (service: {service})")
    
    return open_ports

def scan_network(network_prefix, start_host=1, end_host=254):
    """
    Scan a range of hosts in a network
    """
    active_hosts = []
    print(f"\nScanning network {network_prefix}.0/24 from host {start_host} to {end_host}...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(is_host_active, f"{network_prefix}.{host}"): host 
                  for host in range(start_host, end_host + 1)}
        
        for future in concurrent.futures.as_completed(futures):
            host = futures[future]
            ip = f"{network_prefix}.{host}"
            if future.result():
                active_hosts.append(ip)
                print(f"🖥️  Host {ip} is active")
    
    return active_hosts

def is_host_active(ip, timeout=1):
    """
    Check if a host is active by attempting to connect to common ports
    """
    common_ports = [22, 80, 443]  # SSH, HTTP, HTTPS
    
    try:
        # First try ICMP ping (may be blocked)
        socket.gethostbyaddr(ip)
        return True
    except:
        # If ping is blocked, try common ports
        for port in common_ports:
            if is_port_open(ip, port, timeout):
                return True
        return False

def validate_ip(target):
    """
    Validate the target IP address or hostname
    """
    try:
        ipaddress.ip_address(target)
        return target
    except ValueError:
        try:
            return socket.gethostbyname(target)
        except socket.gaierror:
            print(f"Invalid target: {target}")
            return None

def main():
    print("\n" + "="*50)
    print("Network and Port Scanner Tool")
    print("="*50)
    print("\nLegal Disclaimer: Use this tool only on networks you own or have permission to scan.\n")
    
    while True:
        print("\n[1] Scan a single host for open ports")
        print("[2] Scan a network for active hosts")
        print("[3] Exit")
        
        choice = input("\nSelect an option (1-3): ")
        
        if choice == "1":
            target = input("\nEnter target IP/hostname: ")
            validated_target = validate_ip(target)
            if validated_target:
                print(f"\nTarget: {validated_target}")
                start_port = int(input("Start port (default 1): ") or 1)
                end_port = int(input("End port (default 1024): ") or 1024)
                
                start_time = datetime.now()
                open_ports = scan_ports(validated_target, start_port, end_port)
                duration = datetime.now() - start_time
                
                if open_ports:
                    print(f"\n✅ Found {len(open_ports)} open ports on {validated_target}")
                else:
                    print(f"\n❌ No open ports found on {validated_target}")
                print(f"Scan completed in {duration.total_seconds():.2f} seconds")
        
        elif choice == "2":
            network_prefix = input("\nEnter network prefix (e.g., 192.168.1): ")
            try:
                host_range = input("Enter host range (e.g., 1-100 or leave blank for 1-254): ")
                if host_range:
                    start_host, end_host = map(int, host_range.split('-'))
                else:
                    start_host, end_host = 1, 254
                    
                start_time = datetime.now()
                active_hosts = scan_network(network_prefix, start_host, end_host)
                duration = datetime.now() - start_time
                
                if active_hosts:
                    print(f"\n✅ Found {len(active_hosts)} active hosts on {network_prefix}.0/24")
                else:
                    print(f"\n❌ No active hosts found on {network_prefix}.0/24")
                print(f"Scan completed in {duration.total_seconds():.2f} seconds")
            except ValueError:
                print("Invalid host range format. Please use format like '1-100'.")
        
        elif choice == "3":
            print("\nExiting...\n")
            break
        
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

