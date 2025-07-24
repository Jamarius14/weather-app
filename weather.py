from datetime import datetime


current_datetime = datetime.now()

day_of_week_number = current_datetime.weekday()

day_of_week_name = current_datetime.strftime('%A')

workout = ""

if day_of_week_number == 0:
    workout = "Squat Day: Squat,Paused Squat,RDLs,Leg Press,ABS. "
elif day_of_week_number == 1:
    workout = "Cardio Day"
elif day_of_week_number == 2:
    workout = "Bench Day: Bench Press,Overhead Press,Incline dumbbell press,Barbell Rows,Dips,Face Pulls."
elif day_of_week_number == 3:
    workout = "Cardio Day"
elif day_of_week_number == 4:
    workout = "Deadlift Day: Deadlift,Block Pulls,Front Squat,Hamstring Curls,Plank."
elif day_of_week_number == 5:
    workout = "Rest Day"
elif day_of_week_number == 6:
    workout = "Rest Day"

print(f"Hello, today is {day_of_week_name}")
print(f"{workout},have a great workout!")
