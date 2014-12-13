import string

def answer(names):
    scratchList = []
    splitName = [list(name) for name in names]
    for name in splitName:
        nameValue = 0
        for character in name:
            letterValue = string.ascii_lowercase.index(character.lower()) + 1
            nameValue = nameValue + letterValue
        scratchList.append([nameValue, "".join(name)])
    finalList = sorted(scratchList)
    for pair in finalList:
        del pair[0]
    finalList = [i[0] for i in finalList]
    return finalList[::-1]


answer(["abcdefg", "vi"])




