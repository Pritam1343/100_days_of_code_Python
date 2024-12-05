import random
from hangman_words import word_list
from hangman_arts import HANGMANPICS

chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
for i in range(len(chosen_word)):
    placeholder+="_"
print(f"Word to guess: {placeholder}")
game_over=False
added_letters=[]
lives=6
while not game_over:
    print(f"**********************{lives}/6 LIVES LEFT**********************")
    final_string = ""
    guess = input("Guess the letter\n").lower()
    if guess in added_letters:
        print("Hey ! you have already guessed this letter")
    for letter in chosen_word:
        if (guess==letter):
            final_string+=letter
            added_letters.append(guess)
        elif letter in added_letters:
            final_string+=letter
        else:
            final_string+="_"

    print(final_string)
    if guess not in chosen_word:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
        if lives==0:
            game_over=True
            print(f"**********************IT WAS {chosen_word}! YOU LOSE ! **********************")


    if "_" not in final_string:
        game_over=True
        print("**********************YOU WIN !!**********************")

    print(HANGMANPICS[6-lives])


