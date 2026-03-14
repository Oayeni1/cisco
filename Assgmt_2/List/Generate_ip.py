# Since Python has a built-in module, will be making use of that.
import ipaddress

def generate_ips_from_subnet(subnet):
    network = ipaddress.ip_network(subnet, strict=False)
    
    # hosts() automatically excludes network and broadcast
    return [str(ip) for ip in network.hosts()]


# Example usage
subnet = "192.168.1.0/30"
ip_list = generate_ips_from_subnet(subnet)

print("Usable IP addresses:")
for ip in ip_list:
    print(ip)