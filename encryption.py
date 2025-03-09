def encrypt(lst, cle):
    encrypt_mess = ""
    for x in lst:
        if ord(x) < 97 or ord(x) > 122:
            encrypt_mess += x
            continue
        #print(f'{x}: {ord(x)}')
        t = ord(x) - 97
        #print('t ='+ str(t))
        c = (t + cle)  % 26 
        #print('c =' + str(c)) 
        encrypt_mess += chr(c + 97)
    return encrypt_mess      
        ##encrypt_mess =  encrypt_mess + ord(x) + 2
            
d = "xy hdfoq 1ap"
print(encrypt(d,3))
   