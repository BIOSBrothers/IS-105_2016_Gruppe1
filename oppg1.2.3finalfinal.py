def encode(string):
    pass

def dedecode():
    arrayofbytes = []
    with open ("sourcecode.txt") as f:
        linearray = f.readlines()
        for line in linearray:
            splitbyte = [line[i:i+8] for i in range(0, len(line), 8)]
            
            
        decodedmessage = ""
        
        for byte in splitbytes:
            decodedmessage += str(chr(int(byte, 2)))
            
        print (decodedmessage)
    
    if __name__== "__main__":
        decode()