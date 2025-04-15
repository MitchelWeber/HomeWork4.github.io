def encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            ciphertext += chr(shifted)
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, shift):
    return encrypt(ciphertext, -shift)

def main():
    plaintext = input("Enter your full name: ")
    shift = int(input("Enter the shift key (1-25): "))
    encrypted_text = encrypt(plaintext, shift)
    print("Encrypted text:", encrypted_text)

    guess = int(input("Guess the key to decrypt: "))
    while guess != shift:
        print("Wrong key. Try again.")
        guess = int(input("Guess the key to decrypt: "))
    
    decrypted_text = decrypt(encrypted_text, guess)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
