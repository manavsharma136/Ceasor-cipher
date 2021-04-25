# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 19:33:43 2019

@author: dell
"""

def encypt(text,s):
 result = ""
   # transverse the plain text
 for i in range(len(text)):
      char = text[i]
     
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
 return result

text = "the manav sHarma"
s = 3

print ("Plain Text : " + text)
#print ("Shift pattern : " + str(s))
print ("Cipher: " + encypt(text,s))