import re

s = "aAbBcCd"

x = re.split("[A-Z]", s)

print(x)