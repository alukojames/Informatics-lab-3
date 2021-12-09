# Isu number = 336205
# 336205 % 4 = 1

import re

vowel, consonant = "aeiou", "bcdfghjklmnpqrstvwxyz"
pattern = rf"\b[{consonant}]*([{vowel}])(?:[{consonant}]*\1*)*\b"
texts = ["This is the first text of the second additional task.",
         "Russia is a very large country",
         "November is the eleventh month of the year.",
         "A joke is meant to be funny.",
         "This is very random."]

for checked in texts:
    for i in sorted([matchObj.group()
    for matchObj in re.finditer(pattern, checked, flags=re.I)], key=len):
        print(i)
    print()