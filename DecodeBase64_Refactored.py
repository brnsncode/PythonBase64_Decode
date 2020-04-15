#dDecode 15 rounds of base64 encoding.

#Decode 5 rounds of Base16
#Continue the rounds to decode Base32
#Continue the last 5 rounds of Base64 Encoding for a total of 15 rounds

import base64
import time

def b16Decode(textToDecode):
    decodedText = base64.b16decode(textToDecode)
    return decodedText

def b32Decode(textToDecode):
    decodedText = base64.b32decode(textToDecode)
    return decodedText

def b64Decode(textToDecode):
    decodedText = base64.b64decode(textToDecode)
    return decodedText

encodedFile = open("C:/Python/Learning/encodedflag.txt", "rb").read()

decode_Rounds = [1,2,3,4,5]

#Decode first 5 rounds of Base16 encoding
for layer in decode_Rounds:
        encodedFile = b16Decode(encodedFile)
        print(encodedFile)

#By re-using and re-assigning the 'encodedFile' variable, we are able to pass the values to next loop for further round decoding
for layer in decode_Rounds:
        encodedFile = b32Decode(encodedFile)
        print(encodedFile)

#Decode the last 5 rounds
for layer in decode_Rounds:
        encodedFile = b64Decode(encodedFile)
        print(encodedFile)