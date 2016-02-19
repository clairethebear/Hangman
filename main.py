# Game of hang man that will play against the computer to try and figure out a word before the hang man has been drawn out
import random
import hangman_matrix

class Game(object):
    pass

class Player(Game):
    pass

holder = [[' ' for i in range(10)] for j in range(20)]
database_words = ["Claire", "Dave", "Bernardo", "Dearbhaile"]
secret_word = random.choice(database_words).lower()
count = 0
incorrect_count = 0

correct_guesses = []
# Make functio hint OOO so that hint can inherit from the function but then
# just add the response when needed.
# return_hint = ''

def check_response(response):
    for x in secret_word:
        if response in x:
            current_correct_letter = response
            correct_guesses.append(response)
            print_correct_guesses(correct_guesses)
            return_hint = print_correct_guesses(correct_guesses)
            return return_hint, current_correct_letter

def print_correct_guesses(correct_guesses):
    for letters in correct_guesses:
        hint(secret_word, correct_guesses)
        return_hint  = hint(secret_word, correct_guesses)
    return return_hint

def hint(secret_word, response):
    hint = []
    word_count = len(secret_word)

    for i in secret_word:
        hint.append('-')
    for y in response:
        hint[secret_word.index(y)] = y
    hint_string = "".join(hint)
    return hint_string


while (count < 7):
   response = raw_input("Have a guess:")
   response = response.lower()
   count = count + 1

   if response in correct_guesses:
        print 'You have already chosen this word: ' + response
        count = count - 1
   else:
       if check_response(response) is None:
           print 'Nope the letter ' + response + ' is incorrect'
           incorrect_count = incorrect_count + 1
           holder = hangman_matrix.hangman_matrix(incorrect_count, holder)
           for i in holder:
             print i
       else:
           if check_response(response)[0] == secret_word:
               print "You win! Game Over"
               break
           else:
               for i in holder:
                 print i
               print check_response(response)
               print 'You have just selected ' +check_response(response)[0]
               print 'You have ' + str(7 - count)
