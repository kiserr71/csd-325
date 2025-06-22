#Robert Kiser
#06/22/25
#CSD325
#Module 4.2 Assignment

import csv
from datetime import datetime

from matplotlib import pyplot as plt

def high_temp(dates, highs):
# Plot the high temperatures using a red line.
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')

    # Format plot.
    plt.title("Daily high temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()

def low_temp(dates, lows):
# Plot the low temperatures using a blue line.
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')

    # Format plot.
    plt.title("Daily low temperatures - 2018", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    
    plt.show()


def main():
    program_continue = True
    #Sets the testing variable for the main program loop.
    
    filename = 'sitka_weather_2018_simple.csv'
    #Sets the file name of our data file to the 'filename' variable.
    
    print("Welcome to Sitka Weather Graphing!")
    print()
    #Greeting.

    while(program_continue):
    #Main program loop.
        
        temp_select = input("Please enter 1 if you wish to see high tempes" \
                            "2 to see low temps, or anything else to exit.")
        print()
        #Simple menu selection. Anything other than '1' or '2' exits the loop.
        
        if temp_select == '1':
            with open(filename) as f:
            #This line needs to run every time the user makes a selection since
            #it closes the file after the 'with' statement ends.
                reader = csv.reader(f)
                header_row = next(reader)
                dates, highs = [], []
                for row in reader:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    dates.append(current_date)
                    high = int(row[5])
                    #Accesses the next value in the 'TMAX' column.
                    highs.append(high)
                
            high_temp(dates, highs)
            #Calls function that plots the high temperatues and passes 'dates'
            #and 'highs'.

        elif temp_select == '2':
            with open(filename) as f:
                reader = csv.reader(f)
                header_row = next(reader)
                dates, lows = [], []
                for row in reader:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    dates.append(current_date)
                    low = int(row[6])
                    #Accesses the next value in the 'TMIN' column.
                    lows.append(low)

            low_temp(dates, lows)
            #Calls function that plots the low temperatures and passes 'dates'
            #and 'lows'.

        else:
            print("Thank you for using Sitka Weather Graphing!")
            #Exit statement.
            
            program_continue = False
            #Changes the testing variable to 'False', ending the program.
            
if __name__ == '__main__':
    main()
