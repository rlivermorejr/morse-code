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
    ui = input(
        'Select 1 to decode a morse-code sequence\nor 2 to decode a binary-sequence to morse code: ')
    try:
        if ui == '1':
            mor = input('Please enter the morse code to decode: ')
            morse = decode_morse(mor)
            print(morse)
        if ui == '2':
            print('Sorry, still working on the bits function. Try decoding some morse!')
            # bit = input('Please enter the bits to decode: ')
            # output = decode_bits(bit)
            # print(output)
    except KeyError:
        print("Syntax is incorrect!")
