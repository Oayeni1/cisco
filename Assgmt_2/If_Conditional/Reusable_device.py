def is_device_reachable(ping_output):
    """
    Determine if a Cisco device is reachable based on ping output.
    Returns True if at least one reply received, False otherwise.
    """

    # Convert to lowercase for case-insensitive search
    output = ping_output.lower()

    # Check for success rate line
    if "success rate" in output:
        # Extract the percentage using string splitting
        try:
            # Example: "Success rate is 100 percent (5/5)"
            start = output.find("success rate is") + len("success rate is")
            end = output.find("percent", start)
            success_percent = int(output[start:end].strip())
            return success_percent > 0
        except ValueError:
            return False
    else:
        # Fallback: check for '!' characters (successful replies)
        return "!" in output
ping_success = """
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.1.1, timeout is 2 seconds:
!!!!!
Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/3 ms
"""

ping_fail = """
Type escape sequence to abort.
Sending 5, 100-byte ICMP Echos to 192.168.1.2, timeout is 2 seconds:
.....
Success rate is 0 percent (0/5)
"""

print(is_device_reachable(ping_success))  # True
print(is_device_reachable(ping_fail))     # False