

def code():
    table = {}
    for i in range (0, 127):
        table[i] = chr(i)
    return table

def encode(message):
    table = code()
    string = ""
    code_for_string = []
    for byte in message:
        symbol = byte
        if (string + symbol) in table.values():
            string = string + symbol
        else:
            for k,v in table.iteritems():
                if v == string:
                    code_for_string.append(k)
            table[max(table.keys())+1] = string + symbol
            string = symbol
    for k,v in table.iteritems():
        if v == string:
            code_for_string.append(k)
    print table
    return code_for_string
    

def test():
    test_message = "to be or not to be"
    print encode(test_message)
    
test() 


def decode(numbers):
    
f = open("D:\Skole\IT\IS-105\Python prosjekter\sindre.txt", mode='r')
print f.read(1)
f.close()