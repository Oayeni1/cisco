def is_valid_acl_rule_simple(acl_rule):
    acl_rule = acl_rule.strip().lower()
    
    if not acl_rule:
        return False  # empty rule
    
    # Must start with permit or deny
    if not (acl_rule.startswith("permit") or acl_rule.startswith("deny")):
        return False
    
    # Must contain a valid protocol
    if not any(proto in acl_rule for proto in ["ip", "tcp", "udp", "icmp"]):
        return False
    
    return True
acl1 = "permit tcp 192.168.1.0 0.0.0.255 any eq 80"
acl2 = "deny icmp 10.0.0.0 0.0.0.255 any"
acl3 = "allow ip any any"  # invalid
acl4 = ""  # empty

print(is_valid_acl_rule_simple(acl1))  # True
print(is_valid_acl_rule_simple(acl2))  # True
print(is_valid_acl_rule_simple(acl3))  # False
print(is_valid_acl_rule_simple(acl4))  # False