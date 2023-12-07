import random
import string
from string import ascii_letters
import re

commands = [
    "select",
    "from",
    "where",
    "insert",
    "into",
    "values",
    "update",
    "set",
    "delete",
    "drop",
    "create",
    "alter",
    "table",
    "database",
    "truncate",
    "order",
    "by",
    "asc",
    "desc",
    "limit",
    "like",
    "and",
    "or",
    "not",
    "between",
    "in",
    "is",
    "null",
]


def ManipulateInput_Inline(string):
    # Obfuscate user input
    for word in commands:
        if word in string.lower():
            #  find all that match the sql command
            wordmatched = re.findall(word, string, flags=re.IGNORECASE)
            for i in range(len(wordmatched)):
                wordmatched = re.search(word, string, flags=re.IGNORECASE)
                RandomPlace = random.randint(1, len(word) - 1)
                listofchr = [char for char in wordmatched[0]]

                newword = ""
                for i, c in enumerate(listofchr):
                    if i == RandomPlace:
                        newword += "/**/"
                    newword += c

                result = re.compile(re.escape(word.lower()), re.IGNORECASE)
                string = result.sub(newword, string, 1)
    return string


def ManipulateInput_Percent(user_input):
    # obfuscate user input with invalid percent encoding
    # for every word in the user input, add a random number of %'s to the word
    for word in commands:
        # split word into list of characters
        listofchr = [char for char in word]
        # for every character in the list
        for i, c in enumerate(listofchr):
            # add a random number of %'s to the character
            randomnumber = random.randint(0, 2)
            listofchr[i] = (randomnumber * "%") + c
        # join the list back into a string
        newword = "".join(listofchr)
        # replace the word with the new word
        result = re.compile(re.escape(word.lower()), re.IGNORECASE)
        user_input = result.sub(newword, user_input)

    return user_input


def to_hex(string):
    return "".join([hex(ord(c))[2:] for c in string])


def ManipulateInput_URL(user_input):
    # for each word in the user input, split each word into characters
    # generate a random number between 1 and len(listofchr)
    # replace random character with % + hex value of character for random number of characters
    user_input = user_input.lower()
    words = user_input.split()
    for word in words:
        # split word into list of characters
        listofchr = [char for char in word]
        random_subs = random.randint(1, len(listofchr))
        index_list = []
        for i in range(random_subs):
            random_index = random.randint(0, len(listofchr) - 1)
            while random_index in index_list:
                random_index = random.randint(0, len(listofchr) - 1)
            index_list.append(random_index)

            listofchr[random_index] = "%" + to_hex(listofchr[random_index])
        # join the list back into a string
        newword = "".join(listofchr)
        # replace the word with the new word
        result = re.compile(re.escape(word.lower()), re.IGNORECASE)
        user_input = result.sub(newword, user_input)

    return user_input


def ManipulateInput_Nesting(user_input):
    # obfuscate user input with nesting expressions
    # for every word in the user input that is a sql command
    # split the word into a list of characters
    # choose a random position in the list
    # add the duplicate of the word starting at the random position
    # join the list back into a string
    # replace the word with the new word
    for word in commands:
        if word in user_input.lower():
            # split word into list of characters
            listofchr = [char for char in word]
            # choose a random position in the list
            RandomPlace = random.randint(1, len(listofchr) - 1)
            # add the duplicate of the word starting at the random position
            listofchr.insert(RandomPlace, word)
            # join the list back into a string
            newword = "".join(listofchr)
            # replace the word with the new word
            result = re.compile(re.escape(word.lower()), re.IGNORECASE)
            user_input = result.sub(newword, user_input)
    return user_input


def ManipulateInput_Overflow(user_input):
    # obfuscate the user input by adding a high random number of characters to the statement
    # WAFS can crash when we add about 1000 characters to the statement
    # generate a random number between 1000 and 1500
    # generate a random string of that length
    # add the string to the user input
    # return the user input
    randomnumber = random.randint(1000, 1500)
    randomstring = "".join(
        random.choice(string.ascii_letters) for i in range(randomnumber)
    )
    user_input = user_input + randomstring
    return user_input
