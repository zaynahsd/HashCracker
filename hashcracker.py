import hashlib
import argparse

#------------------------------------CLI Setup--------------------------------------------------------
parser = argparse.ArgumentParser(description="Simple Hash Cracker")
parser.add_argument("--type", required=True, choices=["md5", "sha1", "sha256", "sha512"], help="Hash type to crack.")
parser.add_argument("--hash", required=True, help="The target hash to crack.")
parser.add_argument("--wordlist", required=True, help="Path to the wordlist")
parser.add_argument("--save", action="store_true", help="Save successful matches a file.")
args = parser.parse_args()

hash_type = args.type.lower()
target_hash = args.hash.strip()
wordlist = args.wordlist

expected_lengths = {
"md5": 32,
"sha1": 40,
"sha256": 64,
"sha512": 128,
}

if len(target_hash) != expected_lengths[hash_type]:
    print(f"[!]Warning. The hash entered does not match the expected length for {hash_type}")

#------------------------------------Hash Cracking Setup--------------------------------------------------------

try:

    match_found = False 

    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f: 
        for count, line in enumerate(f, 1):
            word = line.strip() 
            if not word: 
                continue
            

            #Hash the current word
            if hash_type == "md5": 
                hashed_word = hashlib.md5(word.encode()).hexdigest()
            elif hash_type == "sha1":
                hashed_word = hashlib.sha1(word.encode()).hexdigest()
            elif hash_type == "sha256":
                hashed_word = hashlib.sha256(word.encode()).hexdigest()
            elif hash_type == "sha512":
                hashed_word = hashlib.sha512(word.encode()).hexdigest()
            print(f"Trying: {word} -> {hashed_word}")

            #Compares hashed word to target hash
            if hashed_word == target_hash: 
                print (f"[+] Match found: {word}") 
                match_found = True



                #Saves match if requested
                if args.save:
                    with open("cracked_hashes.txt" , "a") as out:
                        out.write(f"Hash Type: {hash_type.upper()}\n")
                        out.write(f"Target Hash: {target_hash}\n")
                        out.write(f"Cracked word: {word}\n")
                        out.write(f"-" * 40 + "\n")

                break
            
    if not match_found:
        print(f"[-] No match found in the wordlist.") 

#------------------------------------Error Handling--------------------------------------------------------
except FileNotFoundError: 
    print(f"[-] Wordlist not found at: {wordlist}")
except Exception as e:
    print(f"[!] An error occurred: {e}")

