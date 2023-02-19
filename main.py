import json

INPUT_FILE_PATH = "en_us.json"
OUTPUT_FILE_PATH = "la_pig.json"
VOWELS = "AEIOUaeiou"
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def pigLatin(word):
    if word[0] in VOWELS:
        # vowels dont go to the end of the word
        return word + "hay"
    else:
        if (
            ((word[0] in "cptswCPTSW") and (word[1] in "hH"))
            or ((word[0] in "kK") and (word[1] in "nN"))
            or ((word[0] in "wW") and (word[1] in "rR"))
        ):
            # handle initial diagraphs
            leadingConsonant = word[:2]
            word = word[2:]
            if leadingConsonant.istitle():
                word = word.title()
            word += leadingConsonant.lower() + "ay"
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
    pig_latin_language = {}
    with open(INPUT_FILE_PATH, "r") as input_file:
        english_language = json.load(input_file)
    for key, value in english_language.items():
        if key == "language.name":
            pig_latin_language["language.name"] = "Pig Latin"
        elif key == "language.region":
            pig_latin_language["language.region"] = "Pigland"
        elif key == "language.code":
            pig_latin_language["language.code"] = "la_pig"
        else:
            pig_latin_language[key] = parseString(value)
    with open(OUTPUT_FILE_PATH, "w") as output_file:
        json.dump(
            pig_latin_language,
            output_file,
            sort_keys=False,
            indent=4,
            separators=(",", ": "),
        )
