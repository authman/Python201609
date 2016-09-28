# basic RegEx assignment

import re

q = [
 r'\w*?v\w*',                               #question 1
 r'\w*?s{2}\w*',                            #question 2
 r'\w*?e$',                                 #question 3
 r'\w*b.b\w*',                              #question 4
 r'\w*b.+b\w*',                             #question 5
 r'\w*b.*b\w*',                             #question 6
 r'\w*a\w*e\w*i\w*o\w*u\w*',                #question 7
 r'^[regulaxpsion]+[regulaxpsion]+$',       #question 8
 r'\w*(.)\1\w*'                             #question 9
]

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    # return [word for word in words if re.search(regex, word)]

    for i in range(len(words)):
        ken = re.search(regex,words[i])

        if ken:
            print 'found: ', ken.group()
        else:
            continue

for k in q:
    get_matching_words(k)
    print "~~~~~~~~~~~~~~~~~~~~"
