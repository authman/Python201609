import re




def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    return [word for word in words if re.search(regex, word)]

regex1 =r"v"
regex2 =r"ss"
regex3 =r"e$"
regex4 =r"b.b"
regex5 =r"b.+b"
regex6 =r"b.*b"
regex7 =r"a.*e.*i.*o.*u"
regex8 =r"\b[regular expression]+\b"
regex9 =r"(.)\1"

print get_matching_words(regex9)
