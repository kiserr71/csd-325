#Robert Kiser
#CSD 325
#06/03/25
#Module 1.3 Assignment

def countdown(bottles):
#Function performs the countdown based on user input.
    
    while(bottles > 1):
    #Runs a loop that reduces the number of bottles remaining each iteration
    #until there is only 1 left.
        
        print(f'{bottles} bottles of beer on the wall, {bottles} bottles of beer.')
        print(f'Take one down and pass it around, {bottles - 1} bottle(s) of beer ' \
        'on the wall.')
        print()
        bottles -= 1
        
    else:
    #Displays the lyrics using the proper pluralization for a single bottle.
        
        print(f'{bottles} bottle of beer on the wall, {bottles} bottle of beer.')
        print(f'Take one down and pass it around, {bottles - 1} bottles of beer on the wall.')
            

def main():
#Main function
    
    test = 0
    #Creates a conditional variable for the input validation loop.
    
    while (test == 0):
        try:
        #This try-except-else block validates input, ensuring the user chooses
        #an integer.
            
            bottles = int(input("Enter the number of bottles: "))
            #By invoking the int() function, this produces an error if the user
            #does not enter an integer. If the error occurs, the "except" block
            #will run.
            
            print()
            
        except:
            
            print('Invalid input. Please enter a number.')
            print()
            
        else:
        #This block will run if the user enters any integer.
            
            if (bottles < 1):
            #This verifies the user selected an integer greater than 0. The
            #countdown() function will not function properly otherwise.
                
                print('Please choose a number greater than 0')
                print()
                
            else:
            #This iterates the test variable, ending the loop.
                test += 1
    else:
    #Runs the countdown() function upon the successful completion of the
    #input validation loop.
        
        countdown(bottles)
        
    print()
    print("Time to buy more bottles of beer.")

if __name__ == '__main__':
    main()
