# print the game instruction
import random
while True:
    user_choice = (input("Enter your choice (rock | paper | scissor): ")).lower()
    print("Ur Choice is : "+user_choice)
    if user_choice not in ['rock','paper','sicssor']:
        print("Plzz Enter a valid choice")
    else:
        comp_choice = random.choice(['rock','paper','sicssor'])
        print("comp Choice is : "+comp_choice)
        result = None
        if((user_choice == 'rock' or comp_choice == 'sicssor') or 
           (user_choice == 'sicssor' or comp_choice == 'rock')):
            result = 'rock'
        elif((user_choice == 'paper' or comp_choice == 'rock') or 
           (user_choice == 'rock' or comp_choice == 'paper')):
            result = 'paper'
        else:
            result = 'sicssor'
            
        print(f"\t{user_choice}\n\t  v/s\n\t{comp_choice}")
        
        if user_choice == comp_choice:
            print("<== Draw ==>")
        elif result == user_choice:
            print("<== User Wins ==>");
        else:
            print("<== Computer Wins==>");
        
    ans = input("Do you wanna play more: ")
    if ans == 'n' or ans == 'N':
        break