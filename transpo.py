# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:53:31 2019

@author: dell
"""
   
def split_len(seq, length):
   return [seq[i:i + length] for i in range(0, len(seq), length)]
def encode(key, plaintext):
   order = {
      int(val): num for num, val in enumerate(key)
   }
ciphertext = ''

 for index in sorted(order.keys()):
    for part in split_len(plaintext, len(key)):
      try:ciphertext += part[order[index]]
      except IndexError:
            continue

 
 return ciphertext
print(encode('3214', 'HELLO'))