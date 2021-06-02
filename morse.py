#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Morse Code Decoder

"Dot" – is 1 time unit long.
"Dash" – is 3 time units long.
Pause between dots and dashes in a character – is 1 time unit long.
Pause between characters inside a word – is 3 time units long.
Pause between words – is 7 time units long.
"""
__author__ = """
Russell Livermore
Jae Early
JT Maupin
John Anderson
Jackson Detke
"""

from morse_dict import MORSE_2_ASCII
# dot smallest sequence of 1's

# loop through and count the 1's
# stop at 0 then start loop again
# counting each group of 1's and comparing
# compare to time_unit

# bits does not work. bit converters online don't match


def decode_bits(bits):
    count = 0
    counts = []
    prev_bit = "1"
    morse = ""
    for time in bits.strip("0"):
        if time != prev_bit:
            counts.append(count)
            count = 0
            prev_bit = time
        count += 1
    counts.append(count)

    multiplier = min(counts)
    for index, new in enumerate(counts):
        if index % 2 == 0:
            if new//multiplier == 1:
                morse += "."
            if new//multiplier == 3:
                morse += "-"
        else:
            if new//multiplier == 7:
                morse += "   "
            if new//multiplier == 3:
                morse += " "
    return morse


def decode_morse(morse):
    morse_code = ""
    new_morse = morse.split("  ")
    for word in new_morse:
        morse2 = word.split()
        for char in morse2:
            morse_code += MORSE_2_ASCII[char]
        morse_code += " "
    return morse_code.strip()


# def test_basic_letters(morse):
#     return decode_morse(morse)


if __name__ == '__main__':
    ui = input('Enter morse to decode: ')
    try:
        morse = decode_morse(ui)
        print(morse)
    except KeyError:
        print("Morse syntax is incorrect!")
