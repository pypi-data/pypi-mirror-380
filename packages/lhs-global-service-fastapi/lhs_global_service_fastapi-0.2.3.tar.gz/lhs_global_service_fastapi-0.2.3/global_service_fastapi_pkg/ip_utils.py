import socket
import logging

# Hostname/IP detection
class MachineIPDetector:
    def get_info(self):
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
            logging.debug(f"Detected machine IP address: {ip_address}, hostname: {hostname}")
            return ip_address, hostname
        except Exception as e:
            logging.error(f"Error detecting machine IP/hostname: {e}")
            return "Unknown", "Unknown"
        
    def resolve_hostname(self,ip: str) -> str:
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            return hostname
        except Exception as e:
            logging.warning(f"Could not resolve hostname for IP {ip}: {e}")
            return "unknown"
        
    def get_real_client_ip(self,request):
        # FastAPI: request.headers is a case-insensitive dict-like object
        x_forwarded_for = request.headers.get("x-forwarded-for")
        if x_forwarded_for:
            return x_forwarded_for.split(',')[0].strip()
        # Fallback to request.client.host
        if hasattr(request, "client") and request.client:
            return request.client.host
        return ""
        
    