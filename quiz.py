#initialisong dictionary of the question mapped to the correct option
q_dict={
    'What is the capital of France?':'c',
    'Which planet is known as the Red Planet?':'b',
    'What is 5 + 7?':'c',
    'Which animal is known as the King of the Jungle?':'c',
    'What is the largest ocean on Earth?':'d'

}

#initialising set of options
options_list = [
    """a) Berlin
b) Madrid
c) Paris
d) Rome""",

    """a) Earth
b) Mars
c) Jupiter
d) Venus""",

    """a) 10
b) 11
c) 12
d) 13""",

    """a) Elephant
b) Tiger
c) Lion
d) Cheetah""",

    """a) Atlantic Ocean
b) Indian Ocean
c) Arctic Ocean
d) Pacific Ocean"""
]

counter=0
score=0
for quiz in q_dict:
    print(quiz)
    print(options_list[counter])
    user_ans=input('enter your option').strip().lower()
    if user_ans==q_dict[quiz]:
        score+=1
    counter+=1

print('congratulatons you scored!', score, 'out of ', len(q_dict))