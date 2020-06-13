import re

pattern = re.compile("AA")
m = pattern.search("CAA")
pat = re.search("asd", "Aasd")
print(m, pat)