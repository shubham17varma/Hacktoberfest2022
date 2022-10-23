# Python code to implement
# Vigenere Cipher

def encryption(message, key): 
  encryptionmessage = [] 
  for i in range(len(message)): 
    x = (ord(message[i]) +ord(key[i])) % 26
    x += ord('A') 
    encryptionmessage.append(chr(x)) 
  return("" . join(encryptionmessage)) 

def decryption(encryptionmessage, key): 
  orginalmessage = [] 
  for i in range(len(encryptionmessage)): 
    x = (ord(encryptionmessage[i]) - ord(key[i]) + 26) % 26
    x += ord('A') 
    orginalmessage.append(chr(x)) 
  return("" . join(orginalmessage)) 

def generateKey(message, key): 
  key = list(key) 
  if len(message) == len(key): 
    return(key) 
  else: 
    for i in range(len(message) -len(key)): 
      key.append(key[i % len(key)]) 
  return("" . join(key)) 

if __name__ == "__main__": 
  message = input("Enter the message: ")
  key = input("Enter the key: ")
  key = generateKey(message, key) 
  encryptionmessage = encryption(message,key) 
  print("Encrypted message is:", encryptionmessage) 
  print("Decrypted message is:", decryption(encryptionmessage, key)) 
  
# This code is contributed
# by Shubham Anil Varma
