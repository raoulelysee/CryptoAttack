# Le code qui suit prend comme entrées un texte (clair) composé d’une suite de
# caractères ASCII [a-z] et d’une clé et qui retourne le texte chiffré via 
# le code de Cæsar.
def encrypt(list, cle):
    encrypt_message = ""
    for x in list:
        if ord(x) < 97 or ord(x) > 122:
            encrypt_message += x
            continue
        t = ord(x) - 97
        c = (t + cle)  % 26 
        encrypt_message += chr(c + 97)
    return encrypt_message      
            
d = "xy hdfoq 1ap"
print(encrypt(d,3))

# Le code qui suit prend comme entrées un texte chiffré et d’une clé et qui
# retourne le texte en clair via le code de Cæsar.
def decrypt(list, cle):
    decrypt_message = ""
    for y in list:
        if ord(y) < 97 or ord(y) > 122:
            decrypt_message += y
            continue
        a = ord(y) - 97
        b = (a - cle)  % 26 
        decrypt_message += chr(b + 97)
    return decrypt_message       
    
    
#g = "ab kgirt 1ds"
g = encrypt(d,3)
print(decrypt(g, 3))