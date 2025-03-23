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


# def  brute_force(message, cle_n):
#     dict_force_brute = {}
#     for cle in range(1, cle_n + 1):
#         dict_force_brute[cle] = decrypt(message, cle)
#     print(dict_force_brute)
#
# brute_force("Jh ydlv d od slvflqh", 10)


def  frq_txt(message):
    dict_frq_txt = {}
    for char in message:
        if char not in dict_frq_txt:
            dict_frq_txt[char] = 1
        else:
            dict_frq_txt[char] += 1
    res = list(dict_frq_txt.items())
    res.sort(key=lambda x:x[1], reverse=True)
    print(res)

frq_txt("passe")





# import argparse
# parser = argparse.ArgumentParser()
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-t", "--text", help="message à encrypter ou decrypter")
# group.add_argument("-f", "--fichier", help="fichier à encrypter ou decrypter")
# parser.add_argument("-e", "--encrypt", help="encrypter", action="store_true")
# parser.add_argument("-c", "--cle", type=int, help="cle", required=True)
# parser.add_argument("-o", "--output", help="Sortie ecran ou fichier", action="store_true")
# args = parser.parse_args()
#
# if args.text:
#     texte_recu = args.text
#     print("encryption de message: ", args.text)
# elif args.fichier:
#     try:
#         with open(args.fichier, "r") as file:
#             texte_recu = file.read()
#             print(texte_recu)
#     except FileNotFoundError:
#         print("Fichier n'existe pas")
#         exit()
#
# if args.encrypt:
#     result = encrypt(texte_recu, args.cle)
# else:
#     result = decrypt(texte_recu, args.cle)
#
# if args.output:
#     with open("fichier.txt", "w") as f:
#         f.write(result)
# else:
#     print(result)
