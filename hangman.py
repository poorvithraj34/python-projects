import random
stages = [
'''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''',
'''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
'''
]
word_list=["poorvith","kishore","samrudh"]

lives=6


chosen_word=random.choice(word_list)
print(chosen_word)

paceholder=""
for lette in chosen_word:
    paceholder+="_"
print(paceholder)

game_over=False
correct_letters=[]
while not game_over:
    guess=input("Guess a letter:").lower()


    display=""

    for letter in chosen_word:
        if letter==guess:
            display+=letter
            if guess not in correct_letters:
                correct_letters.append(guess)

        elif letter in correct_letters:
            display += letter      

        
        else:
            display+="_"
    print(display)

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you loose")


    if "_" not in display:
        game_over=True
        print("you win")


    print(stages[6-lives])

