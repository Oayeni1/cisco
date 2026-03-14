# Since Python has a built-in module, will be making use of that.
import ipaddress

def filter_private_ips(ip_list):
    private_ips = []

    for ip in ip_list:
        ip_obj = ipaddress.ip_address(ip)
        if ip_obj.is_private:
            private_ips.append(ip)

    return private_ips


# Example usage
ips = [
    "192.168.1.1",
    "8.8.8.8",
    "10.0.0.5",
    "172.20.10.3",
    "172.40.1.1",
    "1.1.1.1"
]

private_ips = filter_private_ips(ips)

print("Private IPs:")
for ip in private_ips:
    print(ip)