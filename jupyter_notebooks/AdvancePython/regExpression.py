import re

def Main():
    line = "I think I understand regex"
    matchResult = re.match(r"think", line, re.M|re.I) # "I think I understand regex" will be a match. it has to be exact
    if matchResult :
        print( "Match found:", matchResult.group())
    else :
        print (" No match was found")

    searchResult = re.search(r"think", line, re.M| re.I)
    if searchResult :
        print("search Result :" , searchResult.group())
    else:
        print("Nothing found in search")

if __name__ == '__main__':
    Main()
