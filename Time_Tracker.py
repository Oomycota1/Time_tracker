

# This is a simple program to help the user tract his time and earning per day
# This program creates a csv file named as Log_book

#let's import some modules we may need
import datetime
import time
import csv
format = '%Y-%m-%d %H:%M:%S'


#Since this has been designed for Nana,let's set up some login details for Nana
# let's set his username to Nana and password to 1234
username = "Nana"
password = "1234"


#This helps Nana to login into his account
def login() :
    userInput = input("What is your username?")

    if userInput == username:
       userInput = input("Please enter your password:")
       if userInput == password:
           print("Welcome",username,"!")
       else:
           print("Oops! That is a wrong password!Try again!")
           login()
    else:
        print("Oops! Username is Invalid!")
        print("Please note that this is case sensitive. Let's try again")
        login()       
login()
    

# Let's create a function which gets the users start time

def begin():
    # If the user is ready to start, we get the start time from the system
    # else,we call the begin function again
    ready_to_start = input("Are you ready to start now? Please enter 'yes'or 'no':")
    if ready_to_start == 'yes':
         start_time = time.strftime(format)
         print("This is your start time for today",start_time,"Don't forget to clock out when you close.")   
    else:
         print("Try again when you are ready")
         begin()
begin()


# Let's get the start time and resave into a new vaiable called start
# This would be used in calculating his earnings
start_time = time.strftime(format)
start = datetime.datetime.strptime(start_time,format)


# let's create another function to get the users end time
def finish():
    end_time = input("Have you closed now? Please enter 'yes'or 'no':")
    if end_time == 'yes':
        end_time = time.strftime(format)
        print("Today's end time:",end_time)
    else:
        print("Oops! Come back when you close!")
        finish()
finish()


#let's help him identify the task he worked on
task = input("Which task did you work on?(task number or description)")


#Let's get the closing time and resave into a new vaiable called end
# This would be used in calculating his earnings
end_time = time.strftime(format)
end = datetime.datetime.strptime(end_time,format)


# We can now calculate his earnings with the calc function and save it into a CSV file

def calc():
    
    time_difference = end-start
    secs = time_difference.seconds
    total_hours = secs/3600
    hourly_rate = 5.0
    daily_earning = total_hours*hourly_rate
    print("Good Job! Your total worktime is", total_hours,"hours and your total earning for today is",daily_earning,"$ for working on",task )
    return total_hours,daily_earning


# to get the data into a CSV file to be for future use  
total_hours,daily_earning = calc()   
with open('Log_book.csv','a',newline='') as f:
    fieldnames = ['Task','Start Date and Time','End date and Time','Total hours worked','Daily Earning']
    writer = csv.DictWriter(f,fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({'Task':task,'Start Date and Time':start,'End date and Time':end,'Total hours worked':total_hours,'Daily Earning':daily_earning})      
    f.close()
 
print("Your earnings have been saved into your Log Book.Thank You!")
print("SEE YOU NEXT TIME.....BYE!!")
login()      

#End
