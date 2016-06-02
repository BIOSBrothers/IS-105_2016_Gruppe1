mapping = {
    "0": "X",
    "10": "Y",
    "11": "Z"
    }
binary = {
    "X": "0",
    "Y": "10",
    "Z": "11"
    }
 
def analyse_string(string):
 
    translation = []
    placeholderstring = ""
 
    for letter in string:
        try:
            placeholderstring += letter
            translation.append(mapping[placeholderstring])
            placeholderstring = ""
        except:
            print("not x")
            placeholderstring = letter
 
    return translation
 
def convert_string(string):
 
    translation = []
    placeholderstring = ""
 
    for letter in string:
        try:
            
            translation.append(binary[letter])
            
        except:
            print("not a letter")
            
 
    return translation
 
 
if __name__ == "__main__":
    print(analyse_string("00101001100000"))
    
if __name__ == "__main__":
    print(convert_string("XXXYZZ"))    