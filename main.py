# dictionary_search.py

import hashlib
encoded_password = "29f040a682fa9e198c90a9dab3acb8ca"
filein = open("common_passwords.txt")

for line in filein:
   words = line.split()

   for word in words:
    # Your code to: 
    # 1) encode word and then
    binary_word = word.encode("UTF-8")

    encrypted_password = hashlib.md5(binary_word).hexdigest()
    # 2) compare encoded word to encoded password
    # should go here.
    if encoded_password == encrypted_password:
      print("The password is "+word)

     
filein.close()