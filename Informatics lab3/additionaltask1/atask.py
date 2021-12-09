# Isu number = 336205
# 336205 % 6 = 1

import re

def Duplicate_text (text):
    pattern = re.compile(r"\b(\w+|\s+)\s+\1\b",re.IGNORECASE)
    while re.search(pattern,text):
        text = re.sub(pattern,r'\1',text)
    return text

print(Duplicate_text(input()))



