#!/usr/bin/python3
#Reference from Yoshino blog

enc = b'\x0bPPS\r\x0b\x02\x0f\x12\r\x03_G\t\x08yb}v+--*+*8=W,>'

x = "hjlgyjgyj10hadanvbwdmkw00OUONBADANKHM;IMMBMZCNihaillm"

i = enc[0]

dec = ''
for c in enc[1:]:
    dec += chr(c ^ ord(x[i]))
    i = (i + 1) % 79

flag = 'GrabCON{%s}' % dec
print(flag)