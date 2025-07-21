#Robert Kiser
#07/20/25
#CSD325
#Module 8 Assignment

import json

def display(file_data):
#file_data is a list of dictionaries so we need to loop through the list to
#display everything.
    
    for item in file_data:
        f_name = item["F_Name"]
        l_name = item["L_Name"]
        student_ID = item["Student_ID"]
        email = item["Email"]
        print(f'{l_name}, {f_name}: ID = {student_ID}, Email = {email}')

def main():

    with open ('student.json', 'r') as x:
        file_data = json.load(x)
    #Opens the 'student.json' file, stores it into the 'file_data' variable,
    #and closes the 'student.json' file.
        
    display(file_data)

    print()
    print('This is the original student list.')

    new_entry = {"F_Name": "Robert", 
             "L_Name": "Kiser", 
             "Student_ID": 34210, 
             "Email": "robkiser@my365.bellevue.edu"}
    #Stores the data for the new student into the variable 'new_entry' as a
    #dictionary.

    file_data.append(new_entry)
    #Appends the contents of 'new_entry' to the list of dictionaries in
    #'file_data'.

    print()
    display(file_data)

    print()
    print('This is the updated student list.')

    with open ('student.json', 'w') as y:
        json.dump(file_data, y)
    #Opens the 'student.json' file, overwrites its contents with the contents
    #of the 'file_data' variable, now containing our new student, and closes
    #the 'student.json' file.

    print()
    print('The student.json file has been updated.')

    

if __name__ == '__main__':
    main()





