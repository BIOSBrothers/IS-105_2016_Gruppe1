import shelve
# Åpner shelve - gir den variabel fs og setter writeback til true
fs = shelve.open('filesystem.fs', writeback=True)
current_dir = []

def install(fs):
    # opretter root
    username = raw_input('What do you want your username to be? ')

    fs[""] = {"System": {}, "Users": {username: {}}}

def current_dictionary():
    # Returner en dictionary som representerer filene i current_dir
    d = fs[""]
    for key in current_dir:
        d = d[key]
    return d

# Metode for å printe ut innholdet i current_dictionary
def ls(args):
    print 'Contents of directory', "/" + "/".join(current_dir) + ':'
    for i in current_dictionary():
        print i

# Gå til direcktory
def cd(args):
    # Kun om den ikke er 0
    if len(args) != 1:
        print "Usage: cd <directory>"
        return
    # Hvis den er 0 så gi en feilmelding
    if args[0] == "..":
        if len(current_dir) == 0:
            print "Cannot go above root"
        else:
            current_dir.pop()
    elif args[0] not in current_dictionary():
        print "Directory " + args[0] + " not found"
    else:
        current_dir.append(args[0])
# Opprett et nytt directory
def mkdir(args):
    if len(args) != 1:
        print "Usage: mkdir <directory>"
        return
    # oprett et tomt directory ved nåværende posisjon og synkroniser den tilbake til shelve dictionary
    d = current_dictionary()[args[0]] = {}
    fs.sync()
    
    # print working directory
def pwd(args):
    d = current_dir
    print d[-1]
    
COMMANDS = {'ls' : ls, 'cd': cd, 'mkdir': mkdir, 'pwd' : pwd}

install(fs)

while True:
    raw = raw_input('> ')
    cmd = raw.split()[0]
    if cmd in COMMANDS:
        COMMANDS[cmd](raw.split()[1:])
# Bruke enter istedenfor exit så man kommer til dette punktet.
raw_input('Press the Enter key to shutdown...')