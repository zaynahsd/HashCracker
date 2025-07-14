# HashCracker
HashCracker written in Python. Supports the following Hash Types: **MD5, SHA1, SHA256, and SHA512**.

**Using HashCracker**

1. Download the HashCracker.py file.
   
2. Make note of where you store the Hashcracker.py file. Open up the terminal and navigate to that path where the HashCracker is saved.

3. Run the following command from the path where you downloaded the hashcracker: 
   **python hashcracker.py --type** *Hash Type* **--hash** *Hash* **--wordlist** *path to wordlist* 

   Example:
   
   **python hashcracker.py --type SHA256 --hash 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 --wordlist /Users/Guest/wordlist.txt**

5. If you want to save the output to a file, append the --save flag at the end of your command like so:
   
     **python hashcracker.py --type** *Hash Type* **--hash** *Hash* **--wordlist** *path to wordlist* **--save**


   
