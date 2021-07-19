import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search_word(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len(get_close_matches(word , data.keys())) > 0:
        user_reply = input("\nDid you mean %s instead? Enter Y/N : " % get_close_matches(word , data.keys())[0])
        while True:
            if user_reply not in ["Y" , "N" , "y" , "n"]:
                user_reply = input("\nNot a valid input. Please enter a valid input (Y/N) : ")
            else:
                if user_reply == "Y" or user_reply == "y":
                    return data[get_close_matches(word , data.keys())[0]]
                else:
                    return "The word doesn't exist. Please double check!!!!"
    else:
        return "The word doesn't exist. Please double check!!!!"

while True:
    user_input = input("\nEnter the word : ")
    output = search_word(user_input)

    print("\nWord entered : ", user_input,"\n")
    print("Output : \n")

    if isinstance(output,list):
        j=1
        for i in output:
            print(j,")",i)
            j=j+1
    else:
        print(output)
    response = input("\nDo you want to continue further (Y/N) : ")
    if response not in ["Y" , "N" , "y" , "n"]:
        response = input("\nNot a valid input. Please enter a valid input (Y/N) : ")
    else:
        if response == "y" or response == "Y":
            continue
        else:
            print("\nThank you :)")
            break

