import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)
#will produce match as an object 

#starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
#start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach