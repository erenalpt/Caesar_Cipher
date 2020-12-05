def enc(cWords, keys):
    result = "" 
    cWords = cWords.upper()
    for i in range(len(cWords)):
        a = cWords[i]
        #https://www.geeksforgeeks.org/ord-function-python/
        result += chr((ord(a) + keys-65) % 26 + 65) 

    return result

def dec(cWords, keys):
    result = ""
    for i in cWords:
        a=chr(ord(i)-keys)
        result += a

    return result
