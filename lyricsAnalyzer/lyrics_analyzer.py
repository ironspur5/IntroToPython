"""
Patrick Guha psg486
"""

import operator  # to sort dictionaries by values or keys

from helper2 import she_loves_you


def lyrics_to_frequency(lyrics):

    """ this function takes a list of the song lyrics
    and returns a dictionary with words as its keys 
    and frequency as its values"""

    myDict = {}

    # looks at words in lyrics and it is in there, increase the frequency count, else, add it to the dictionary
    for word in lyrics:

        if word in myDict:
            myDict[word] += 1

        else:
            myDict[word] = 1

    return myDict
    

def most_common_word(dictWords):

    """This function takes a dictionary of word frequency
    and returns the most common word in the song and its frequency packed in a tuple
    example: (['word1'], 15)
    """

    sortedDict = sorted(dictWords.items(), key=operator.itemgetter(1)) # sorts by value in ascending order

    return sortedDict[-1]  # sortedDict[] is a tuple already so just need to access last element (ascending order)


def words_only_once(dictWords):

    """This function takes a dictionary of word frequency
    and returns a list of tuples of words that occur only once in the song
    example: [(['word1'], 1),(['word2'],1),...] 
    """

    onlyOne = []  # list of future desired tuples

    sortedDict = sorted(dictWords.items(), key=operator.itemgetter(1))  # sorts by value as a list of tuples

    for key, value in sortedDict:

        if value == 1:
            myTuple = (key, value)  # created my own because I could not access things in sortedDict via an index
            onlyOne.append(myTuple)

    return onlyOne


def words_with_minimum_freq(dictWords, minTimes):

    """This function takes a dictionary of word frequency 
    and returns a list of tuples of words and their frequencies
    the words returned should have frequencies higher than the 
    "minTimes" argument"""

    # almost identical to function above just changed conditional statement for value, aka frequency

    greaterThanOrEqaulMin = []  # list of future desired tuples

    # sorts by value as a list of tuples
    # set it order in descending order (reverse=True) to match assignment description output
    sortedDict = sorted(dictWords.items(), key=operator.itemgetter(1), reverse=True)

    for key, value in sortedDict:

        if value >= minTimes:
            myTuple = (key, value)  # created my own because I could not access things using sortedDict
            greaterThanOrEqaulMin.append(myTuple)

    return greaterThanOrEqaulMin


# Sample run:
# do not run this part until you finish developing each function separately
def main():

    songDict=lyrics_to_frequency(she_loves_you)
    topWord=most_common_word(songDict)
    print(topWord)
    # finding the least common word
    leastWords=words_only_once(songDict)
    print(leastWords)
    # finding words that occur at least 5 times
    mostWords=words_with_minimum_freq(songDict, 5)
    print(mostWords)


if __name__ == '__main__':
    main()
