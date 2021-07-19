import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

def search_word(word):
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % word)
    results = cursor.fetchall()
    if results:
        return results
    elif len(get_close_matches(word, ))
    else:
        return "The word doesn't exist. Please double check!!!!"


user_input = input("\nEnter the word : ")
user_input = user_input.lower()
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" % user_input)
results = cursor.fetchall()
if results:
    print (results)
else:
    search_word(user_input)