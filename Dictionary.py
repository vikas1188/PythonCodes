import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    noun = w[0].upper() + w[1:]
    # print(noun)
    if w.upper() in data:
        return data[w.upper()]
    if noun in data:
        return data[noun]
    elif w in data:
        return data[w]
    elif len( get_close_matches( w, data.keys()) ) >0 :
        yn = input ("Did you mean %s instead ? Enter Y/y if Yes, or N/n if no: " % get_close_matches( w, data.keys())[0] )
        if yn in ['Y','y']:
            print("\nHere is/are the meaning: \n")
            return data[get_close_matches( w, data.keys())[0]]
        elif yn in ['N','n']:
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else :
        return "The word doesn't exist. Please double check it."

word = input ("Enter word: ")

output = translate(word)
print("\n")
if type(output) == list :
    for item in output:
        print( item)
    print("\n")
else :
    print (output + "\n")
