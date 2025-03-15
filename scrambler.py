import random
word_list = ["python", "developer", "computer", "science", "keyboard", "monitor", "language", "programming", "software", "hardware"]

selected_word = random.choice(word_list)
#print(selected_word)
worded = list(selected_word)  
random.shuffle(worded)  
scrambled_word = "".join(worded) 

print("Scrambled word:", scrambled_word)

user_inp=input('enter what you think the word is')
print(user_inp)

if user_inp==selected_word:
    print('correct!')

else:
    print('wrong!!','the correct words was', selected_word)
