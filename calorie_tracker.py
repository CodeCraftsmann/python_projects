tracker={
    
}

value_list=[]
for values in tracker.values():
    value_list.append(values)



while True:

    value_list=[]
    for values in tracker.values():
        value_list.append(values)

    print(
    """
    Do you wanna:
    1. Update calorie tracker?
    2. View your total calories?
    3. Delete something?
    4. Exit the Programme?

    enter the corresponding Index Number(1,2,3 or 4)

    """
)

    opening_prompt=int(input())
    
    if opening_prompt==4:
        break

    else:
        if opening_prompt==1:
    
            print('what did you eat?')
            food_tracker=input()

            print('how much calories was it')
            calorie_tracker=int(input())

            tracker[food_tracker]=calorie_tracker
            print(tracker)

        
        elif opening_prompt==2:

            print(f'your total colrie are {sum(value_list)}')

        elif opening_prompt==3:
   
            print('please enter the name of ood to be deleted')
            deleted=input()

            if deleted in tracker:
                del tracker[deleted]

            else:
                print('please enter correct food')

        else:
            print("Invalid input! Please enter 1, 2, 3, or 4.")

        

        


