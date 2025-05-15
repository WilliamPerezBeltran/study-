"""
MD5 hash in Python
Cryptographic hashes are used in day-day life like in digital signatures, message authentication codes, manipulation detection, fingerprints, checksums (message integrity check), hash tables, password storage and much more. They are also used in sending messages over network for security or storing messages in databases.

There are many hash functions defined in the “hashlib” library in python.
This article deals with explanation and working of MD5 hash.

MD5 Hash
This hash function accepts sequence of bytes and returns 128 bit hash value, usually used to check data integrity but has security issues.

Functions associated :

encode() : Converts the string into bytes to be acceptable by hash function.
digest() : Returns the encoded data in byte format.
hexdigest() : Returns the encoded data in hexadecimal format.
The below code demonstrates the working of MD5 hash accepting bytes and output as bytes.

filter_none
edit
play_arrow

brightness_4
Python 3 code to demonstrate the  
working of MD5 (byte - byte) 


"""  
import hashlib 
  
# encoding GeeksforGeeks using md5 hash 
# function  
result = hashlib.md5(b'GeeksforGeeks') 
  
# printing the equivalent byte value. 
print("The byte equivalent of hash is : ", end ="") 
print(result.encode()) 
print(result.digest()) 
print(result.hexdigest()) 

