def cidr_to_subnet_mask(cidr):
    # Number of bits set to 1
    ones = int(cidr.lstrip('/'))

    # Create a 32-bit binary mask with ones followed by zeros
    mask_bin = ('1' * ones).ljust(32, '0')

    # Split into 4 octets
    octets = [mask_bin[i:i+8] for i in range(0, 32, 8)]

    # Convert each octet to decimal
    decimal_octets = [str(int(octet, 2)) for octet in octets]

    # Join and return
    return '.'.join(decimal_octets)

# Example usage:
cidr = "/24"
subnet_mask = cidr_to_subnet_mask(cidr)
print(f"CIDR {cidr} => Subnet Mask: {subnet_mask}")