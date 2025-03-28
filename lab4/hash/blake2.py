import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message)
    return blake2_hash.digest()

def main():
    text = input("Nhap chuoi van ban: ").encode('utf-8')
    hashed_text = blake2(text)
    
    print("Chuoi ban dau: ", text.decode('utf-8'))
    print("Ma bam BLAKE2: ", hashed_text.hex())
    
if __name__ == "__main__":
    main()