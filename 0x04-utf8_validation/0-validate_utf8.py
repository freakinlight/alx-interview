#!/usr/bin/python3
"""
This module defines a method to validate UTF-8 encoding.
"""


def validUTF8(data):
    num_bytes = 0

    # Masks to check the bits of the leading byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        mask = 1 << 7
        if num_bytes == 0:
            while mask & num:
                num_bytes += 1
                mask >>= 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num & mask1 and not (num & mask2)):
                return False
        num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    data = [65]  # ASCII 'A' -> True
    print(validUTF8(data))

    data = [
        80, 121, 116, 104, 111, 110, 32, 105,
        115, 32, 99, 111, 111, 108, 33
    ]
    print(validUTF8(data))  # 'Python is cool!' -> True

    data = [229, 65, 127, 256]  # Incorrect sequence -> False
    print(validUTF8(data))
