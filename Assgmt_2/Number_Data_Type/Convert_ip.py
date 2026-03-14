#128   64   32   16    8    4    2    1
# 2⁷   2⁶   2⁵   2⁴   2³   2²   2¹   2⁰

def binary_ip_to_decimal(binary_ip):
    # Split into 4 octets
    octets = binary_ip.split(".")
    
    # Convert each binary octet to decimal
    decimal_octets = [str(int(octet, 2)) for octet in octets]
    
    # Join back into full IP
    return ".".join(decimal_octets)


# Example usage
binary_ip = "11000000.10101000.00000001.00000001"
decimal_ip = binary_ip_to_decimal(binary_ip)

print("Binary IP:", binary_ip)
print("Decimal IP:", decimal_ip)