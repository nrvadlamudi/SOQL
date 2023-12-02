# Using flask, we can create a web application that will allow us to execute SQL queries.


from flask import Flask, render_template, request
import pyodbc
import re
import random
from string import ascii_letters

app = Flask(__name__)

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
            wordmatched = re.findall(word, string, flags=re.IGNORECASE)
            for i in range(len(wordmatched)):
                wordmatched = re.search(word, string, flags=re.IGNORECASE)
                RandomPlace = random.randint(
                    1, len(word) - 1
                )  # "hi!" >>> ["h","i","!"] >> "h/**/i!" or "hi/**/!" !neeed to make it also output it as "h/**/i/**/!"
                listofchr = [char for char in wordmatched[0]]

                newword = ""
                for i, c in enumerate(listofchr):
                    if i == RandomPlace:
                        newword += "/**/"
                    newword += c

                resault = re.compile(re.escape(word.lower()), re.IGNORECASE)
                string = resault.sub(newword, string, 1)
    return string


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        user_input = request.form["user_input"]
        user_input = ManipulateInput(user_input)
        # Using pyodbc to connect to SQL Server
        import pyodbc

        # Connect to SQL Server
        conn = pyodbc.connect(
            "Driver={SQL Server};"
            "Server=DESKTOP-NCA7QV0;"
            "Database=AdventureWorks2022;"
            "Trusted_Connection=yes;"
        )

        # Create a cursor
        cursor = conn.cursor()

        # Execute an obfuscated sql query
        cursor.execute(user_input)

        # Fetch the data
        for row in cursor:
            print(row)

        # Close the connection
        conn.close()
        return render_template("result.html", user_input=user_input)


if __name__ == "__main__":
    app.run(debug=True)
