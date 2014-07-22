#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 21, 2014

@author: anroco

How to convert bytes to hex in python?

¿Cómo convertir bytes to hexadecimal en python?
'''

import binascii

#create a bytes object.
b = b'hello world'
print(b)

#generates a bytes object with the hexadecimal representation of the binary
#data. Every byte of data is converted into the corresponding 2-digit hex
#representation.
b_hex = binascii.hexlify(b)
print(type(b_hex))
print(b_hex)
