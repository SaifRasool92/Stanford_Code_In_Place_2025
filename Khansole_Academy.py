import random

def main():
    print("Khansole Academy")
    
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    
    print(f"What is {num1} + {num2}?")
    
    try:
        your_ans = int(input("Your answer: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    answer = num1 + num2

    if your_ans == answer:
        print("Correct!")
    else:
        print("Incorrect.")
        print(f"The expected answer is {answer}")

if __name__ == '__main__':
    main()
