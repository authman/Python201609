import re

def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

	return [word for word in words if re.search(regex, word)]

print "1:"
print get_matching_words(r".*v.*")

print "2:"
print get_matching_words(r".*ss.*")

print "3:"
print get_matching_words(r".*e$")

print "4:"
print get_matching_words(r".*b.b.*")

print "5:"
print get_matching_words(r".*b.+b.*")

print "6:"
print get_matching_words(r".*b.*b.*")

print "7:"
print get_matching_words(r".*a.*e.*i.*o.*u.*")

print "8:"
print get_matching_words(r"[regulaxpsion]")

print "9:"
print get_matching_words(r"(.)\1")