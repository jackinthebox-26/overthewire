new = 'etaoinshrdlcumgfwypbvkjxqz \n'

old = 'SJQUBNCGDZVWMYTXKELAFIOHRP \n'

found1file = open('key','r')
found1 = found1file.read()
print(found1)
newtext = ""
for i in found1:
    location = old.find(i)
    if i != ' ':
        newtext += new[location]
print(newtext)
