#Robert Kiser
#CSD 325
#06/03/25
#Module 1.3 Assignment

def countdown(bottles):
#Function performs the countdown based on user input.
    while(bottles > 1):
        print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.')
        print(f'Take one down and pass it around, {bottles - 1} bottle(s) of beer ' \
        'on the wall.')
        print()
        bottles -= 1
    else:
        print(f'{bottles} bottle of beer on the wall, {bottles} bottle of beer.')
        print(f'Take one down and pass it around, {bottles - 1} bottles of beer on the wall.')
            

def main():
    test = 0
    while (test == 0):
        try:
            bottles = int(input("Enter the number of bottles: "))
            print()
        except:
            print('Invalid input. Please enter a number.')
            print()
        else:
            if (bottles < 1):
                print('Please choose a number greater than 0')
                print()
            else:
                test += 1
    else:
        countdown(bottles)
        
    print()
    print("Time to buy more bottles of beer.")

if __name__ == '__main__':
    main()
