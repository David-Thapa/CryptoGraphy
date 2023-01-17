#Ceaser Cipher (Monoalphbetic Cipher)
import numpy as np

def Encryption(txt,key):
    Encrypt = txt + key - 65
    output = [chr(value + 65) for value in (Encrypt % 26)]
    return output

def Decryption(txt,key):
    Encrypt_txt = np.array([ord(value) for value in txt])
    Decrypt = Encrypt_txt - key - 65
    output = [chr(value + 65) for value in (Decrypt % 26)]
    return output

plain_txt = input('Enter you Full Name: ')
np_plain_txt = np.array([ord(value.upper()) for value in plain_txt if value != ' '])
print(np_plain_txt)
key = int(input('Enter a key: '))

#Encryption:
Encrypt = Encryption(np_plain_txt,key)
print("".join(Encrypt))

#Decryption:
Decrypt = Decryption(Encrypt,key)
print("".join(Decrypt))
