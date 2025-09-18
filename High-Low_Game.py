import random

NUM_ROUNDS = 5
#constant
"""
1.assign random to computer and generate random num for user,print "your num"
2.user to respond higher or lower{code?}
3.build logic incorrect correct
4.for loop 5 times
5.scoring update + final msg
"""
def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    #4milestone
    your_score=0
    for i in range (NUM_ROUNDS):
        print(f"Round {i+1}")
        #1milestone
        comp_num=random.randint(1,100)
        your_num=random.randint(1,100)
        print(f"Your number is {your_num}")
        #2milestone
        user_choice=input("Do you think your number is higher or lower than the computer's?: ")
        
        #3milestone
        higher_correct=user_choice=="higher"and your_num>comp_num
        lower_correct=user_choice=="lower"and your_num<comp_num
        if higher_correct or lower_correct:
            print(f"You were right! The computer's number was {comp_num}")
            
            your_score= your_score+1
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")
    # 5  milestone scoring
        print(f"Your score is now {your_score}")
        print()
    print("Thanks for playing!")





if __name__ == "__main__":
    main()
