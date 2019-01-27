'''
Identifiers

\d = any number

\D = anything but a number

\s = space

\S = anything but a space

\w = any character

\W = anything but a character

. = any character excpet a newline

\b = the whitespace around words

\. = a period


Modifiers

{1,3} = we're expecting 1-3

+ = Match 1 or more 

? = Matches 0 or 1

* = Match 0 or more

$ = Matches the end of a string

^ = matching the beginning of a string

| = matches either or 

[] = range or "variance"

{x} = expecting x amount 


White Space characters

\n = newline

\s = space

\t = tab

\e = escape

\f = form feed 

\r = return

DONT'T FORGET!

. + * ? [] $ ^ () {} | \ 


'''


import re 

exampleString = '''
Jessica is 15 years old, and Daniel is 27 years old.
Edward is 97, and his grandfather, Oscar, is 102.
'''

ages = re.findall(r'\d{1,3}',exampleString)
names = re.findall(r'[A-Z][a-z]*',exampleString)

print(ages)
print(names)

ageDict = {}

x = 0
for eachName in names:
    ageDict[eachName] = ages[x]
    x+=1

print(ageDict)