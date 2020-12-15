import json
from difflib import get_close_matches


# @ parameter string
# @ returns definition for word parameter, from definitions dict
def search(word):

    if word in definitions:

        results(definitions[word])
    else:

        did_you_mean(get_close_matches(word, definitions.keys(), n=1), word)


# @ parameter string or list
# @description prints found definiton to enduser
def results(definitions):

    def display(x):

        for i in x:
            print(f'{i} \n')
    print("\n meaning: \n")
    display(definitions) if type(definitions) == list else print(definitions)


# @parameter {list} possible_match, {string} word
# @description displays potential match for word enduser is searching for.
def did_you_mean(possible_match, word):
    try:
        end_user_response = input(
        f'Did you mean {possible_match[0]} instead of {word} ? \n Enter Y/N. ')
        end_user_response = end_user_response.lower()

        if end_user_response == 'y' or end_user_response == 'yes':
            search(possible_match[0])
        elif end_user_response == 'n' or end_user_response == 'no':
            results('sorry, no match found')
    except Exception:
       print("Please, Enter a Word not an empty string")
       prompt_enduser()
    
def prompt_enduser(prompt_question = 'Enter Word: '):
    word = input(prompt_question)
    print('--------------------')
    search(word)

definitions = json.load(open('./data.json', 'r'))

prompt_enduser()



