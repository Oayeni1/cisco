import ipaddress

def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

print(is_valid_ip("192.168.1.1"))  # True
print(is_valid_ip("10.0.0.256"))   # False
print(is_valid_ip("abc.def.1.2"))  # False