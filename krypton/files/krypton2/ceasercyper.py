phrase ="OMQEMDUEQMEK" 
for key in range(26): 
    newphrase = ""
    for i in phrase:
        new = ord(i) + key
        if new > 90:
            new -= 26
        newphrase += chr(new)
    print(str(key) + " : " + newphrase)
