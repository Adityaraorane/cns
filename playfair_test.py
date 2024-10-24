def generate_key_table(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  
    key_table = []
    
    for char in key:
        if char not in key_table:
            key_table.append(char)
    
    for char in alphabet:
        if char not in key_table:
            key_table.append(char)
    
    return [key_table[i:i+5] for i in range(0, 25, 5)]

def find_position(key_table, letter):
    for row in range(5):
        for col in range(5):
            if key_table[row][col] == letter:
                return row, col
    return None

def encrypt_message(key_table, pairs):
    encrypted_message = []
    for digraph in pairs:
        row1, col1 = find_position(key_table, digraph[0])
        row2, col2 = find_position(key_table, digraph[1])
        
        if row1 == row2:
            encrypted_message.append(key_table[row1][(col1 + 1) % 5])
            encrypted_message.append(key_table[row2][(col2 + 1) % 5])
        elif col1 == col2:
            encrypted_message.append(key_table[(row1 + 1) % 5][col1])
            encrypted_message.append(key_table[(row2 + 1) % 5][col2])
        else:
            encrypted_message.append(key_table[row1][col2])
            encrypted_message.append(key_table[row2][col1])
    
    return ''.join(encrypted_message)

def decrypt_message(key_table, en_pairs):
    decrypted_message = []
    for digraph in en_pairs:
        row1, col1 = find_position(key_table, digraph[0])
        row2, col2 = find_position(key_table, digraph[1])
        
        if row1 == row2:
            decrypted_message.append(key_table[row1][(col1 - 1) % 5])
            decrypted_message.append(key_table[row2][(col2 - 1) % 5])
        elif col1 == col2:
            decrypted_message.append(key_table[(row1 - 1) % 5][col1])
            decrypted_message.append(key_table[(row2 - 1) % 5][col2])
        else:
            decrypted_message.append(key_table[row1][col2])
            decrypted_message.append(key_table[row2][col1])
    
    return ''.join(decrypted_message)

key = "OCTOBER"
pairs = ['AD', 'IT', 'YA']  
en_pairs = ['DF', 'KC', 'WF']  

key_table = generate_key_table(key)
encrypted_message = encrypt_message(key_table, pairs)
decrypted_message = decrypt_message(key_table, en_pairs)

print(f"Encrypted message: {encrypted_message}")
print(f"Decrypted message: {decrypted_message}")