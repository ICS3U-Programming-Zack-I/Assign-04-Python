# Created by: Zack Isingoma
# Created on: 11th Jan 2022.
# a programm that lets users input
# 'q' to quit loop

def main():
    print("Use 'Q' to exit loop")
    while True:
        user_input = input("Enter any number: ")
        try:
            user_num = (user_input)
            if user_num != 'Q':
                print("Lets play again")
            elif user_num == 'Q':
                break
        except Exception:
            print("Invalid input")

    print("Thank you for playing")


if __name__ == "__main__":
    main()
