binary = {
    "A" : "000",
    "B" : "001",
    "C" : "110",
    "D" : "11",
    "E" : "101",
    "F" : "01"
}
letters = {
    "000" : "A",
    "001" : "B",
    "110" : "C",
    "11" : "D",
    "101" : "E",
    "01" : "F"
}

def huffmanDecode (dictionary, text):
    res = ""
    while text:
        for k in dictionary:
            if text.startswith(k):
                res += dictionary[k]
                text = text[len(k):]
    return res


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
    print(huffmanDecode(letters, "0000011101110101"))
    
if __name__ == "__main__":
        print(convert_string("ABCDEF"))