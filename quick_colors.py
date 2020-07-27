import re
import sys

with open(sys.argv[1], 'r') as f:
    css = f.read()

print(set(re.findall(
    r': *#([a-fA-f0-9]{6})', css
)))
