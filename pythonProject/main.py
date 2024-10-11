def caesarcipher(text_to_encrypt, shift_value):
    encrypted_text = ""
    for char in text_to_encrypt:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            new_codepoint = (ord(char) - ascii_offset + shift_value) % 26 + ascii_offset
            new_alphabet = chr(new_codepoint)
            encrypted_text += new_alphabet
        else:
            encrypted_text += char
    return encrypted_text


text_to_encrypt_user_input = input("please give your text to encrypt: ")
shift_value_user_input = int(input("please give your shift value: "))

print(caesarcipher(text_to_encrypt_user_input, shift_value_user_input))
