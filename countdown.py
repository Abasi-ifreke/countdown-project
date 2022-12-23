from datetime import datetime

user_goal = input ("enter your goal with a deadline and separate both values with ':'\nexample: 'learn python:23.12.2022'\n\n")  #accepts user input: the goal and the deadline
input_list = user_goal.split(":")   #the split is to separate both values in the list

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")   #format for writing date
todays_date = datetime.today()

count_down = deadline_date - todays_date
count_down_hours = int(count_down.total_seconds() / 60 / 60)   #conversion to hours

if deadline_date > todays_date:
    print (f"Dear user, the time left to achieve your goal; {goal}, is {count_down_hours} hours ({count_down.days} days)")
else:
    print ("Invalid deadline")
