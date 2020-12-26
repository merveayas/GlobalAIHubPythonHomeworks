import random
    
def display_hangman(tries):
    stages = [ """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
               """,
               """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
               """,
               """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     
               """,
               """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
               """,
               """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
               """,
               """
                    --------
                    |      |
                    |      O
                    |     
                    |      
                    |     
               """,
               """
                    --------
                    |      |
                    |      
                    |     
                    |      
                    |     
               """                      
        ]
    return stages[tries]
 
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    name = input("What is your name? ")
    # Here the user is asked to enter the name first
 
    print("Welcome ", name)
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed the letter {}".format(guess))
            elif guess not in word:
                print("{} is not in the word.".format(guess))
                tries -= 1
            else:
                print("Good job")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word):
            if guess in guessed_words:
                print("You already guessed the word {}".format(guess))
            elif guess != word:
                print("{} is not the word.".format(guess))
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word

        else:
            print("Guess is not valid.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("Congrats!")
    else:
        print("Sorry.")

def main():
    words = ['computer', 'science', 'programming', 
         'python', 'mathematics'] 
 
    word = random.choice(words).upper()
    play(word)
    while input("Play Again? (Y/N): ").upper() == "Y":
        word = random.choice(words).upper()
        play(word)

main()

