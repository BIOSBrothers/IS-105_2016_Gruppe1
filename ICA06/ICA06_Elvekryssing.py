# -*- coding: utf-8 -*-

entity = ['kylling', 'rev', 'korn']
path = []

# Definerer hvem som kan spise hvem
def eats(x, y):
    if x == 'kylling' and y == 'korn':
        return True
    elif x == 'rev' and y == 'kylling':
        return True
    else:
        return False

# Definerer om en par trygt kan bli forlatt på den ene siden av elven
# uten tilsyn fra en myding person.
def safe_pair(x, y):
    if eats(x, y) or eats(y, x):
        return False
    else:
        return True

# Returnerer tilstanden av symbolet som er i dictionary al. Den returnerer
# dens verdi og men ingen refereranse til det, så det kan brukes til testing men kan ikke modifiseres.
# Hvis symbolet ikke er en del av listen returnerer den nil.
def state_of(who, state):
    try:
        return state[who]
    except KeyError:
        state[who] = False
        return False

# Verfiserer om tilstanden definert som dictionary er trygg. Hvis kylling er på samme side som man,
# da er vi trygge. Hvis ikke, om korn eller rev også er på dan andre siden, da er vi ikke trygge.
def safe_state(state):
    if state_of('man', state) == state_of('kylling', state):
        return True
    elif state_of('kylling', state) == state_of('rev', state):
        return False
    elif state_of('kylling', state) == state_of('korn', state):
        return False
    else:
        return True
    
# Flytter ett objekt fra den ene siden til den andre tilstands al.
# Det er en list mutator. Alle objektene sine posisjoner er definert med 0 og 1,
# så en bevegelse flytter den nåværende posisjonen med 1. Head-tape eksempelet.
# Så retunerer den listen.
def move(who, state):
    if state[who] == 'left':
        state[who] = 'right'
    else:
        state[who] = 'left'
    return state

# Tester om tilstanden har nådd målet. Målet er å få alle
# fire objektene over på den andre siden.
def goal_reach(state):
    if not state:
        return False
    return (state_of('man', state)=='right' and
            state_of('kylling', state)=='right' and
            state_of('rev', state)=='right' and
            state_of('korn',state)=='right')

# Sjekker om child er en trygg tilstand å bevege seg inn i, og hvis det det er,
# legg det til i listen med tilstander.
def check_add_child(child, list_states):
    if safe_state(child):
        list_states.append(child)
    return list_states

def expand_states(state):
    children = []
    child = state.copy()
    # man kan bevege seg alene
    move('man', child)
    check_add_child(child, children)
    for ent in entity:
        # Flytt et objekt til samme side som man
        if state_of(ent, state) == state_of('man', state):
            child = state.copy()
            move('man', child)
            move(ent, child)
            check_add_child(child, children)
        #else:
        #print "unsafe state", child
    return children
# Søker etter løsning fra opprinnelige tilstand
def search_sol(state):
    path.append(state)
    next = state.copy()
    while next and not goal_reach(next):
        nl = expand_states(next)
        next = {}
        for child in nl:
            if not (child in path):
                next = child
                path.append(next)
                break
    return next

# Initialisering av globale verdier
initial_state = {}
initial_state['man'] = 'left'
for e in entity:
    initial_state[e] = 'left'
    
# Print opprinnelige tilstand
#{'korn': 'left', 'rev': 'left', 'kylling': 'left', 'man': 'left'}

# Konstruer hele løsniningen etter å ha evaluert de tidligere statements
print "Searching for a solution from the initial state:"
print search_sol(initial_state)

# Evalurer variable path for å se løsningen baklengs.
print "The full path is:"
for s in path:
    print s
