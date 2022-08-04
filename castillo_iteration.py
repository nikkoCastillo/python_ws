from ntpath import join
import string


def replace(origString, origSubString, newSubString):
    print("ORIGINAL STRING: " + origString)
    
    # convert the full original sentence to a list of words
    origString_list = list(origString.split(" "))
    
    # replacing the original sub string with the new substring (newSubString)
    for indexString in origString_list:
        if indexString.lower() == origSubString.lower():    # lowercase all character for case sensitivity
            tmpIndex = origString_list.index(indexString)
            origString_list[tmpIndex] = newSubString
    
    # reverting back the list of strings to a whole string using the  join() function
    newString = ' '.join(origString_list)

    # print new string(newString)
    print("NEW STRING: " + newString)


replace('The quick brown fox jumps over the lazy dog', 'quick', 'slow')