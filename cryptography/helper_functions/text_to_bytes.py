def str_to_bytes(some_string: str) -> bytes:
    return some_string.encode('utf-8')

def bytes_to_str(some_bytes: bytes) -> str:
    return some_bytes.decode('utf-8')

def bytes_to_bits(some_bytes: bytes) -> str:
    """Converts a string to its binary representation in bits."""
    return ' '.join(f'{byte:08b}' for byte in some_bytes)

# Example usage:
def main():
    message = "Hello World!"
    message_bytes = str_to_bytes(message)    
    message_from_bytes = bytes_to_str(message_bytes)
    binary_view_of_bytes = bytes_to_bits(message_bytes)

    print(f"Message before conversion {message}")
    print(f"Bytes {message_bytes}")
    print(f"Binary {binary_view_of_bytes}")
    print(f"Message {message_from_bytes}")

if __name__ == "__main__":
    main()