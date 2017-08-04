# ARM by Ken Hall 8/4/2017
# Acronym reclamation module (ARM) creates a dictionary of acronyms for a txt file
# Requires one input argument: path to txt file contaning text to analyze

import sys
import re
import string
from pprint import pprint

filename = sys.argv[1]
f = open(filename,'r',encoding='UTF8')

# Build a dictionary of acronym substitutions. Any combination of captial
#  letters in parentheses will trigger an acronym pattern match search
acronym_def = re.compile(r'\([A-Z]+\)')
acronym_dict = {}
for line in f:
    #line = (c for c in line2 if 0 < ord(c) < 127)
    acronym_defs = acronym_def.findall(line)
    words = line.split()
    for item in acronym_defs:
        stripped_acronym = item[1:-1]
        i = len(stripped_acronym)
    #    print("i: ",i)
        first_letter = item[1]
        while i < len(words):
            ksub = re.sub(r'[^\w\s\(\)]','',words[i])
            words[i] = ksub
            #print(item)
        #    print(words[i])
            if words[i] == item:
            #    print("MATCH!")
                j = i - len(stripped_acronym)
            #    print("j: ",j)
                myphrase = ""
                while str(words[j][0]).lower() != str(first_letter).lower() and j < i:
                    #print("Words first letter: " + str(words[j][0]).lower() + " item first letter: " + str(first_letter).lower())
                    j += 1
                while j < i:
                    myphrase += (words[j]) + " "
                    j += 1
                myphrase2 = myphrase[:-1]
                if myphrase2 != "":
                    acronym_dict[stripped_acronym] = myphrase2
            #    print("Matched " + stripped_acronym + " to " + myphrase)
            i += 1
        #print(stripped_acronym)
print("\nAcronym Dictionary: ")
pprint(acronym_dict)

# Now, write a new file with all of the acronym substitutions in place
savename = filename[:-4] + "-ARMED.txt"
f2 = open(savename,'w')
f = open(filename,'r',encoding='UTF8')
for line in f:
    line2 = line
    for key in sorted(acronym_dict, key=len, reverse=True):
        line3 = re.sub(r'\([A-Z]+\)','',line2)
        line4 = re.sub(r'\s\.','.',line3)
        line5 = line4.replace(key,acronym_dict[key])
        line2 = line5
    f2.write(line2)

print("\n\nWrote \"" + savename + "\"")
