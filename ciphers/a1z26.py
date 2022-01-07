"""
Convert a string of characters to a sequence of numbers
corresponding to the character's position in the alphabet.

https://www.dcode.fr/letter-number-cipher
http://bestcodes.weebly.com/a1z26.html
"""
from __future__ import annotations


def encode(plain: str) -> list[int]:
    """
    >>> encode("myname")
    [13, 25, 14, 1, 13, 5]
    """
    return [ord(elem) - 96 for elem in plain]
    """
    ord(elem) - 96 ... -> gets ascii value of every character in plaintext and subtracting 96, therefore getting its place in the alpabet (eg: ord(m) -> 109, ord(m-96) -> 13)
    [... for elem in plain] -> single line for loop iterating over the plaintext
    """


def decode(encoded: list[int]) -> str:
    """
    >>> decode([13, 25, 14, 1, 13, 5])
    'myname'
    """
    return "".join(chr(elem + 96) for elem in encoded)
    """
    "".join(...) -> converts list of substrings to single string (eg - ['m','y','n','a','m','e'] -> "myname")
    chr(elem+96) ... -> adds 96 to ascii value of every element in encoded list and converts ascii to character (so 1 becomes 97, ascii value for 'a')
    ... for elem in encoded -> single line for statement decoding every element "elem" in list of encoded characters "encoded"
    """


def main() -> None:
    encoded = encode(input("-> ").strip().lower())
    #encoding input
    print("Encoded: ", encoded)
    #printing encoded list
    print("Decoded:", decode(encoded))
    #calling decode function on encoded list and printing the decoded list


if __name__ == "__main__":
    main()
