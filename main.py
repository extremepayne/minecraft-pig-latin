VOWELS = "AEIOUaeiou"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def pigLatin(word):
    if word[0] in VOWELS:
        return word + "hay"
    else:
        leadingConsonant = word[0]
        word = word[1:]
        if leadingConsonant.isupper():
            word = word.title()
        word += leadingConsonant.lower() + "ay"
        return word


def parseString(string):
    outString = ""
    currentWord = ""
    index = 0
    for character in string:
        if index >= len(string) - 1:
            if (character in LETTERS) and (currentWord != ""):
                currentWord += character
                currentWord = pigLatin(currentWord)
                outString += currentWord
                currentWord = ""
            else:
                outString += character
        else:
            if (character in LETTERS) and (string[index + 1] in LETTERS):
                currentWord += character
            elif (
                (character in LETTERS)
                and (not (string[index + 1] in LETTERS))
                and (currentWord != "")
            ):
                currentWord += character
                currentWord = pigLatin(currentWord)
                outString += currentWord
                currentWord = ""
            else:
                outString += character
        index += 1
    return outString


if __name__ == "__main__":
    # print("doing 'Done'")
    # print(pigLatin("Done"))
    # print("Doing 'off'")
    # print(pigLatin("off"))
    # print("Doing 'remote'")
    # print(pigLatin("remote"))
    # print("Doing 'button'")
    # print(pigLatin("button"))
    print("Parsing 'Reset %s button'")
    print(parseString("Reset %s button"))
