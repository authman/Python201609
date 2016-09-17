r1="v"
r2="ss"
r3="e$"
r4="b.b"
r5="b.+b"
r6="bb*"
r7="a.*e.*i.*o.*u.*"
r8= r"\b[regulaxpsion]+\b"
r9=r"([a-zA-Z])\1"






import re

def get_matching_words(regex):
 words = ["aimlessness", "assassin", "baby", "beekeeper","regular", "belladonna", "cannonball", "crybaby", "denver", "embra77ceable", "facetious",
          "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural",
          "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbear67able", "uni99on","r", "video77tape"]

 return [word for word in words if re.search(regex, word)]

print(get_matching_words(r9))




    
