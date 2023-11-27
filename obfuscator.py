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



def ManipulateInput(string):
    # Obfuscate user input
    for word in commands:
        if word in string.lower():
            #  find all that match the sql command
            wordmatched=re.findall(word, string, flags=re.IGNORECASE)
            for i in range(len(wordmatched)):
                wordmatched=re.search(word, string, flags=re.IGNORECASE)
                RandomPlace = random.randint(1, len(word)-1)# "hi!" >>> ["h","i","!"] >> "h/**/i!" or "hi/**/!" !neeed to make it also output it as "h/**/i/**/!"
                listofchr = [char for char in wordmatched[0]]

                newword = ""
                for i, c in enumerate(listofchr):
                    if i == RandomPlace:
                        newword += "/**/"
                    newword += c

                resault = re.compile(re.escape(word.lower()), re.IGNORECASE)
                string=resault.sub(newword, string,1)
    return string