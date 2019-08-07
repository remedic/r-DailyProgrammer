#!/usr/bin/env python

import string

# https://www.reddit.com/r/dailyprogrammer/comments/cmd1hb/20190805_challenge_380_easy_smooshed_morse_code_1/

code=".- -... -.-. -.. . ..-. --. .... .. .--- -.- .-.. -- -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."
code = code.split(" ")

d = {}

for i,letter in enumerate(list(string.ascii_lowercase)):
    d[letter]=code[i]

def smorse(string):
    output = ""
    for character in string:
        m = d[character]
        output += m
    return(output)

print(smorse("sos"))
