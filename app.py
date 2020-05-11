import json
from difflib import get_close_matches
data = json.load(open('data.json'))


def translate(word):
    update = word.lower()
    if update in data:
        return data[update]
    elif len(get_close_matches(update, data.keys())) > 0:
        answer = input(f"Do you mean {get_close_matches(update, data.keys())[0]} instead?. Press Y if yes or N for no.: ")
        if answer == 'Y'.lower():
            return data[get_close_matches(update, data.keys())[0]]
        elif answer == 'N'.lower():
            return 'The word is doesn\'t exist. Please double check.'
        else:
            return 'We did n\'t understand your entry.'

    else:
        return 'The word is donen\'t exist. Please double check.'


print(translate(input('Enter your word: ')))
