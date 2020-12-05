import sys
import sezarcrypt as crypt

try:
    
    f0 = sys.argv[0]
    f1 = sys.argv[1]
    word = sys.argv[2]
    keys = sys.argv[3]

    if len(sys.argv) > 2:

        if f1 == "-d":
            print(crypt.dec(word, int(keys)))
        elif f1 == "-e":
            print(crypt.enc(word, int(keys)))
        else:
            print("ERROR!")
    else:
        print("ERROR!")

except:
    print("""
    python sezar.py -d decryptedtext keyvalue
    python sezar.py -e encryptedtext keyvalue
    """)
